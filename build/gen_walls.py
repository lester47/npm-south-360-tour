# -*- coding: utf-8 -*-
# Build each room's cylindrical wall strip as an HTML page, screenshot it, then project to 360°.
import json, os, sys, asyncio
sys.path.insert(0, os.path.dirname(__file__))
import art
from content import ERAS, SLOTS, EGG_YAW

W, H, M = 8192, 1240, 600          # strip size and seam margin
PPM = H / 4.0                      # px per metre vertically (wall 4 m: -1.6 .. +2.4)
CEIL = 2.4


def X(yaw):
    return M + (yaw + 180) / 360 * W


def Y(h):
    return (CEIL - h) * PPM


THEMES = {
  'himalaya': dict(wall='#5e211b', wall2='#7a2e22', band='linear-gradient(#c9892b,#a8661a)', bay='#efe0c2', bayEdge='#c9a46a', label='#3b1a12', labelBg='#f3c766', spot='rgba(255,226,170,.55)', glass=False,
                   floor=(118, 84, 60), floor2=(140, 100, 70), floor_style='wood', ceiling=(58, 30, 26), cove=(255, 205, 140), reflect=.25, mural='mountains'),
  'fishing': dict(wall='#e7e1d2', wall2='#d8d0bd', band='linear-gradient(#9fb3ad,#7d958f)', bay='#f6f1e4', bayEdge='#b8a982', label='#2d3a3a', labelBg='#ffffff', spot='rgba(255,246,220,.6)', glass=False,
                  floor=(152, 132, 108), floor2=(170, 150, 122), floor_style='wood', ceiling=(205, 200, 188), cove=(255, 244, 220), reflect=.18, mural='ink'),
  'calligraphy': dict(wall='#1c222a', wall2='#252d37', band='linear-gradient(#2d7dd2,#1b4f8a)', bay='#10161d', bayEdge='#2d7dd2', label='#e8f4ff', labelBg='#2d7dd2', spot='rgba(120,190,255,.30)', glass=False,
                      floor=(60, 64, 70), floor2=(72, 76, 84), floor_style='tile', ceiling=(24, 28, 34), cove=(120, 180, 255), lamp=(200, 230, 255), reflect=.32, mural='grid'),
  'tea': dict(wall='#a87b50', wall2='#946943', band='linear-gradient(#5a3b22,#3e2816)', bay='#f4ead2', bayEdge='#6b4a2f', label='#3b2a1c', labelBg='#f2c14e', spot='rgba(255,236,190,.5)', glass=True,
              floor=(110, 78, 52), floor2=(128, 92, 62), floor_style='wood', ceiling=(80, 58, 40), cove=(255, 220, 160), reflect=.2, mural='wood'),
  'tiantuan': dict(wall='#2a1846', wall2='#3b2160', band='linear-gradient(#ff6fb1,#7b5cff)', bay='#f6eedf', bayEdge='#ffd76a', label='#2a1846', labelBg='#ffd76a', spot='rgba(255,200,240,.45)', glass=True,
                   floor=(46, 34, 66), floor2=(60, 44, 84), floor_style='tile', ceiling=(30, 20, 46), cove=(255, 140, 210), lamp=(255, 230, 250), reflect=.35, mural='stage'),
  'buddha': dict(wall='#3a302a', wall2='#463a32', band='linear-gradient(#c79a3b,#8a6a20)', bay='#241d18', bayEdge='#c79a3b', label='#2b2118', labelBg='#e2b247', spot='rgba(255,214,140,.42)', glass=True,
                 floor=(70, 60, 52), floor2=(84, 72, 62), floor_style='tile', ceiling=(36, 30, 26), cove=(255, 200, 120), reflect=.28, mural='lotus'),
}


def mural(kind, t):
    """Background band along the top of the wall."""
    if kind == 'mountains':
        pts = []
        import random
        rnd = random.Random(2)
        x = 0
        while x < W + 2 * M:
            pts.append(f'{x},{120 + rnd.uniform(-70, 40):.0f}')
            x += rnd.uniform(140, 300)
        return f'<svg class="mural" width="{W+2*M}" height="220" viewBox="0 0 {W+2*M} 220"><polygon points="0,220 {" ".join(pts)} {W+2*M},220" fill="#8a3a2a" opacity=".55"/></svg>'
    if kind == 'ink':
        import random
        rnd = random.Random(4)
        s = ''
        for k in range(3):
            x = 0; pts = []
            while x < W + 2 * M:
                pts.append(f'{x},{150 - k * 30 + rnd.uniform(-60, 40):.0f}')
                x += rnd.uniform(160, 340)
            s += f'<polygon points="0,260 {" ".join(pts)} {W+2*M},260" fill="#6f7f7a" opacity="{.10 + k*.05:.2f}"/>'
        return f'<svg class="mural" width="{W+2*M}" height="260" viewBox="0 0 {W+2*M} 260">{s}</svg>'
    if kind == 'stage':
        beams = ''
        for i, yaw in enumerate([-170, -120, -70, -20, 20, 70, 120, 170]):
            c = ['#ff6fb1', '#7b5cff', '#5ce1ff', '#ffd76a'][i % 4]
            x = X(yaw)
            beams += f'<polygon points="{x-30},0 {x+30},0 {x+260},{H} {x-260},{H}" fill="{c}" opacity=".10"/>'
        return f'<svg class="mural" width="{W+2*M}" height="{H}" viewBox="0 0 {W+2*M} {H}">{beams}</svg>'
    if kind == 'lotus':
        s = ''
        for i in range(0, W + 2 * M, 220):
            s += f'<g transform="translate({i} 130)" opacity=".18">' + ''.join(f'<ellipse rx="16" ry="44" transform="rotate({a})" fill="#c79a3b"/>' for a in (-50, -25, 0, 25, 50)) + '</g>'
        return f'<svg class="mural" width="{W+2*M}" height="220" viewBox="0 0 {W+2*M} 220">{s}</svg>'
    if kind == 'grid':
        s = ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#2d7dd2" stroke-opacity=".07" stroke-width="2"/>' for x in range(0, W + 2 * M, 80))
        s += ''.join(f'<line x1="0" y1="{y}" x2="{W+2*M}" y2="{y}" stroke="#2d7dd2" stroke-opacity=".07" stroke-width="2"/>' for y in range(0, H, 80))
        return f'<svg class="mural" width="{W+2*M}" height="{H}" viewBox="0 0 {W+2*M} {H}">{s}</svg>'
    if kind == 'wood':
        s = ''.join(f'<rect x="{x}" y="0" width="3" height="{H}" fill="#6b4a2f" opacity=".35"/>' for x in range(0, W + 2 * M, 120))
        return f'<svg class="mural" width="{W+2*M}" height="{H}" viewBox="0 0 {W+2*M} {H}">{s}</svg>'
    return ''


def bay(cx, svg_markup, label, t, w=820, hgt=720, cy=None, glass=None):
    cy = Y(0.15) if cy is None else cy
    glass = t['glass'] if glass is None else glass
    left, top = cx - w / 2, cy - hgt / 2
    g = f'<div class="spot" style="left:{cx-520}px;top:{top-260}px;width:1040px;height:{hgt+420}px;background:radial-gradient(ellipse 50% 55% at 50% 30%,{t["spot"]},rgba(0,0,0,0) 70%)"></div>'
    g += f'<div class="bay" style="left:{left}px;top:{top}px;width:{w}px;height:{hgt}px;background:{t["bay"]};border-color:{t["bayEdge"]}">'
    g += f'<div class="art">{svg_markup}</div>'
    if glass:
        g += '<div class="glass"></div>'
    g += '</div>'
    g += f'<div class="label" style="left:{cx-260}px;top:{top+hgt+22}px;color:{t["label"]};background:{t["labelBg"]}">{label}</div>'
    return g


def room_html(era):
    rid = era['id']; t = THEMES[rid]; room = art.ROOMS[rid]
    hs = [h for h in era['hotspots'] if 'egg' not in h['id']]
    egg = [h for h in era['hotspots'] if 'egg' in h['id']][0]
    body = mural(t['mural'], t)
    for i, fn in enumerate(room['exhibits']):
        body += bay(X(SLOTS[i]), fn(), hs[i]['title'], t)
    # title wall
    cx = X(0)
    body += f'<div class="spot" style="left:{cx-900}px;top:{Y(2.2)}px;width:1800px;height:900px;background:radial-gradient(ellipse 50% 50% at 50% 35%,{t["spot"]},rgba(0,0,0,0) 72%)"></div>'
    body += f'<div class="title-wrap" style="left:{cx-800}px;top:{Y(1.2)}px;width:1600px">{room["title"]()}</div>'
    # easter egg on the back wall (drawn twice so it wraps across the seam)
    for ex in (X(-180), X(180)):
        body += bay(ex, room['egg'](), egg['title'].replace('彩蛋：', '彩蛋・'), t, w=560, hgt=470, cy=Y(0.45), glass=False)
    css = f'''
@font-face{{font-family:x}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W+2*M}px;height:{H}px;overflow:hidden}}
body{{position:relative;font-family:'Noto Sans CJK TC',sans-serif;
 background:
  linear-gradient(180deg,rgba(255,255,255,.10) 0,rgba(255,255,255,0) 90px),
  linear-gradient(180deg,{t['wall2']} 0%,{t['wall']} 30%,{t['wall']} 80%,{t['wall2']} 100%);}}
.mural{{position:absolute;left:0;top:0}}
.band{{position:absolute;left:0;width:100%;}}
.spot{{position:absolute;pointer-events:none}}
.bay{{position:absolute;border:6px solid;border-radius:10px;box-shadow:inset 0 0 60px rgba(0,0,0,.25),0 18px 40px rgba(0,0,0,.35);overflow:hidden;display:flex;align-items:center;justify-content:center}}
.bay .art svg{{width:100%;height:auto;display:block}}
.bay .art{{width:92%}}
.glass{{position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,0) 30%,rgba(255,255,255,.16) 38%,rgba(255,255,255,0) 46%,rgba(255,255,255,0) 60%,rgba(255,255,255,.10) 64%,rgba(255,255,255,0) 70%)}}
.label{{position:absolute;width:520px;text-align:center;font-weight:900;font-size:40px;padding:10px 16px;border-radius:12px;box-shadow:0 6px 16px rgba(0,0,0,.3)}}
.title-wrap{{position:absolute;text-align:center}}
.title-plate .t-kicker{{font-size:48px;font-weight:700;letter-spacing:6px}}
.title-plate .t-main{{font-size:190px;line-height:1.15;font-weight:900;letter-spacing:18px}}
.title-plate .t-sub{{font-size:64px;font-weight:700;letter-spacing:8px;margin-top:6px}}
.title-plate .t-date{{font-size:44px;margin-top:26px;letter-spacing:4px;opacity:.85}}
'''
    bands = f'<div class="band" style="top:0;height:28px;background:{t["band"]}"></div>'
    bands += f'<div class="band" style="top:{H-56}px;height:56px;background:{t["band"]};filter:brightness(.6)"></div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{bands}{body}</body></html>'


async def shoot(pages, outdir):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = await b.new_page(viewport={'width': W + 2 * M, 'height': H}, device_scale_factor=1)
        for rid, html in pages:
            path = os.path.join(outdir, f'wall_{rid}.html')
            open(path, 'w', encoding='utf-8').write(html)
            await pg.goto('file://' + path)
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(outdir, f'wallfull_{rid}.png'), clip={'x': M, 'y': 0, 'width': W, 'height': H})
            print('shot', rid)
        await b.close()


if __name__ == '__main__':
    outdir = os.path.abspath(sys.argv[1])
    only = sys.argv[2:] or [e['id'] for e in ERAS]
    os.makedirs(outdir, exist_ok=True)
    pages = [(e['id'], room_html(e)) for e in ERAS if e['id'] in only]
    asyncio.run(shoot(pages, outdir))
    from project import render
    for rid, _ in pages:
        t = dict(THEMES[rid]); t['slots'] = SLOTS
        render(os.path.join(outdir, f'wallfull_{rid}.png'), os.path.join(outdir, f'pano_{rid}.jpg'), t)
        print('pano', rid)
