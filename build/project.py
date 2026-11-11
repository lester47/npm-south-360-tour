# Project a cylindrical gallery wall strip into a 4096x2048 equirectangular panorama.
# Room: cylinder radius R, eye at origin, floor at -EYE, ceiling at +CEIL.
# Strip column x <-> yaw: x = (yaw+180)/360 * W  (pannellum convention, yaw 0 = image centre)
# Strip row y <-> wall height h: y = (CEIL - h) * PPM
import sys, json
import numpy as np
from PIL import Image, ImageFilter

R = 4.2
EYE = 1.6
CEIL = 2.4
OUT_W, OUT_H = 4096, 2048


def bilinear(img, xs, ys):
    """img HxWx3 float, xs/ys float arrays (x wraps horizontally, y clamps)."""
    H, W = img.shape[:2]
    x0 = np.floor(xs).astype(np.int64); y0 = np.floor(ys).astype(np.int64)
    fx = (xs - x0)[..., None]; fy = (ys - y0)[..., None]
    x1 = x0 + 1; y1 = y0 + 1
    x0 %= W; x1 %= W
    y0 = np.clip(y0, 0, H - 1); y1 = np.clip(y1, 0, H - 1)
    a = img[y0, x0]; b = img[y0, x1]; c = img[y1, x0]; d = img[y1, x1]
    return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy


def render(strip_path, out_path, theme):
    strip = np.asarray(Image.open(strip_path).convert('RGB')).astype(np.float32) / 255.0
    SH, SW = strip.shape[:2]
    PPM = SH / (EYE + CEIL)
    blur = np.asarray(Image.open(strip_path).convert('RGB').filter(ImageFilter.GaussianBlur(10))).astype(np.float32) / 255.0

    v = (np.arange(OUT_H) + 0.5) / OUT_H
    u = (np.arange(OUT_W) + 0.5) / OUT_W
    pitch = (0.5 - v) * np.pi            # +pi/2 top
    yaw = (u - 0.5) * 2 * np.pi          # -pi..pi
    P, Y = np.meshgrid(pitch, yaw, indexing='ij')
    out = np.zeros((OUT_H, OUT_W, 3), np.float32)

    sx = (Y / (2 * np.pi) + 0.5) * SW    # strip column for this yaw
    h = R * np.tan(P)                    # height where the ray meets the wall
    wall = (h <= CEIL) & (h >= -EYE)
    out[wall] = bilinear(strip, sx[wall], ((CEIL - h[wall]) * PPM))

    # ---------- floor ----------
    fl = h < -EYE
    r = EYE / np.tan(-P[fl])                   # horizontal distance of floor hit
    fx_ = r * np.sin(Y[fl]); fz_ = r * np.cos(Y[fl])
    base = np.array(theme['floor'], np.float32) / 255.0
    base2 = np.array(theme.get('floor2', theme['floor']), np.float32) / 255.0
    # planks / tiles
    if theme.get('floor_style', 'wood') == 'wood':
        plank = np.floor(fx_ / 0.32)
        tone = (np.sin(plank * 12.9898) * 43758.5453) % 1.0
        grain = 0.5 + 0.5 * np.sin(fz_ * 9.0 + np.sin(fx_ * 3.1 + plank) * 2.0)
        col = base[None] * (0.86 + 0.14 * tone[:, None]) * (0.94 + 0.06 * grain[:, None])
        seam = (np.abs(((fx_ / 0.32) % 1.0) - 0.5) > 0.485)
        col[seam] *= 0.82
    else:
        tx = np.floor(fx_ / 0.9); tz = np.floor(fz_ / 0.9)
        tone = (np.sin(tx * 12.9898 + tz * 78.233) * 43758.5453) % 1.0
        col = (base[None] * (1 - tone[:, None] * 0.25) + base2[None] * tone[:, None] * 0.25)
        seam = (np.abs((fx_ / 0.9) % 1.0 - 0.5) > 0.492) | (np.abs((fz_ / 0.9) % 1.0 - 0.5) > 0.492)
        col[seam] *= 0.86
    # reflection of the wall in a polished floor
    hw = -2 * EYE + EYE * R / np.maximum(r, 1e-3)      # mirrored wall height
    refl_ok = (hw >= -EYE) & (hw <= CEIL) & (r < R)
    refl = np.zeros_like(col)
    refl[refl_ok] = bilinear(blur, sx[fl][refl_ok], (CEIL - hw[refl_ok]) * PPM)
    k = theme.get('reflect', 0.22) * np.clip((r / R) ** 2.5, 0, 1)
    col = col * (1 - k[:, None]) + refl * k[:, None]
    # floor graphic (top-down RGBA decal covering [-R, R]^2)
    if theme.get('decal'):
        dec = np.asarray(Image.open(theme['decal']).convert('RGBA')).astype(np.float32) / 255.0
        D = dec.shape[0]
        u = (fx_ + R) / (2 * R) * D; v = (R - fz_) / (2 * R) * D
        ok = (u >= 0) & (u < D - 1) & (v >= 0) & (v < D - 1)
        rgba = np.zeros((u.shape[0], 4), np.float32)
        x0 = np.floor(u[ok]).astype(int); y0 = np.floor(v[ok]).astype(int)
        fxw = (u[ok] - x0)[:, None]; fyw = (v[ok] - y0)[:, None]
        rgba[ok] = (dec[y0, x0] * (1 - fxw) + dec[y0, x0 + 1] * fxw) * (1 - fyw) + (dec[y0 + 1, x0] * (1 - fxw) + dec[y0 + 1, x0 + 1] * fxw) * fyw
        a = rgba[:, 3:4] * 0.92
        col = col * (1 - a) + rgba[:, :3] * a
    # spotlight pools near the exhibits, darker towards the wall base, vignette in the centre
    pools = np.zeros_like(r)
    for sy in theme['slots'] + [0.0, 180.0]:
        a = np.radians(sy)
        px, pz = (R * 0.72) * np.sin(a), (R * 0.72) * np.cos(a)
        d2 = (fx_ - px) ** 2 + (fz_ - pz) ** 2
        pools += np.exp(-d2 / 0.9)
    col *= (0.80 + 0.28 * np.clip(pools, 0, 1))[:, None]
    edge = np.clip((R - r) / 0.18, 0, 1)
    col *= (0.55 + 0.45 * edge)[:, None]
    col *= (0.88 + 0.12 * np.clip(r / 2.0, 0, 1))[:, None]
    col[r > R] = col[r > R] * 0.4
    out[fl] = col

    # ---------- ceiling ----------
    ce = h > CEIL
    r = (CEIL) / np.tan(P[ce])
    cx_ = r * np.sin(Y[ce]); cz_ = r * np.cos(Y[ce])
    cbase = np.array(theme['ceiling'], np.float32) / 255.0
    col = np.repeat(cbase[None], r.shape[0], 0)
    # coffered ring + radial beams
    ring = np.exp(-((r - R * 0.62) ** 2) / 0.004)
    col = col * (1 - 0.25 * ring[:, None]) + 0.0
    beams = (np.abs(((np.degrees(Y[ce]) + 180) % 30) - 15) > 14.6) & (r < R * 0.62)
    col[beams] *= 0.8
    # track lights aimed at exhibits
    lamp = np.zeros_like(r)
    for sy in theme['slots'] + [0.0, 180.0, -15, 15]:
        a = np.radians(sy)
        lx, lz = (R * 0.62) * np.sin(a), (R * 0.62) * np.cos(a)
        lamp += np.exp(-((cx_ - lx) ** 2 + (cz_ - lz) ** 2) / 0.006)
    glow = np.array(theme.get('lamp', (255, 236, 200)), np.float32) / 255.0
    col = col * (1 - np.clip(lamp, 0, 1)[:, None]) + glow[None] * np.clip(lamp, 0, 1)[:, None]
    # cove light where ceiling meets the wall
    cove = np.clip((r - (R - 0.35)) / 0.35, 0, 1)
    cglow = np.array(theme.get('cove', (255, 230, 190)), np.float32) / 255.0
    col = col * (1 - 0.6 * cove[:, None]) + cglow[None] * 0.6 * cove[:, None]
    col[r > R] = cglow * 0.7
    # central skylight disc
    sky = np.clip(1 - r / 0.9, 0, 1) ** 1.5
    col = col * (1 - 0.5 * sky[:, None]) + np.array([1, 0.98, 0.94])[None] * 0.5 * sky[:, None]
    out[ce] = col

    img = Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))
    img.save(out_path, quality=86, optimize=True, progressive=True)
    return out_path


if __name__ == '__main__':
    strip, out, theme_json = sys.argv[1], sys.argv[2], sys.argv[3]
    render(strip, out, json.loads(theme_json))
    print('wrote', out)
