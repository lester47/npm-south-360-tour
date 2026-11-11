# -*- coding: utf-8 -*-
# v2 rooms: real NPM photos in vitrines / wall cases / touch screens, pedestals, museum labels, floor graphics.
import os, sys, asyncio, math, json
sys.path.insert(0, os.path.dirname(__file__))
import art
from content import ERAS, SLOTS
from gen_walls import THEMES, W, H, M, X, Y, mural
from real import REAL, SCRIPTS, MULTI, MAPS
from gen_assets import BADGES

REALDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'real')
FLOOR_TOP = H - 56            # y where the baseboard starts (floor line)
EXTRA = {
  'himalaya': dict(case='#efe7da', plinth='#cdbb9c', plinthTop='#ece0c8', frame='#5a1c16', mount='#e8dcc0'),
  'fishing': dict(case='#f1ece0', plinth='#ddd4c2', plinthTop='#f6f1e6', frame='#6b5a3e', mount='#e9e0c9'),
  'calligraphy': dict(case='#202832', plinth='#3d4856', plinthTop='#56657a', frame='#0d1117', mount='#ece3cc'),
  'tea': dict(case='#efe6d4', plinth='#7a5638', plinthTop='#94704e', frame='#4a3220', mount='#efe3c6'),
  'tiantuan': dict(case='#efe9f3', plinth='#5b4285', plinthTop='#7d62aa', frame='#1d1030', mount='#efe6d2'),
  'buddha': dict(case='#3a312a', plinth='#5a4b3e', plinthTop='#7a6655', frame='#1a1511', mount='#e6dcc4'),
}
LIGHT_INTERIOR = {'himalaya', 'fishing', 'tea', 'tiantuan'}


def img(pid):
    return 'file://' + os.path.join(REALDIR, pid + '.jpg')


def label(cx, top, title, sub, t, width=560):
    return (f'<div class="label" style="left:{cx-width/2}px;top:{top}px;width:{width}px;background:{t["labelBg"]};color:{t["label"]}">'
            f'<div class="lt">{title}</div><div class="ls">{sub}</div></div>')


def spot(cx, top, w, h, t, strength=1.0):
    return (f'<div class="beam" style="left:{cx-w/2}px;top:0;width:{w}px;height:{top+h}px;'
            f'background:linear-gradient(180deg,{t["spot"]} 0%,rgba(255,255,255,0) 100%);opacity:{0.55*strength}"></div>'
            f'<div class="spot" style="left:{cx-w}px;top:{top-120}px;width:{2*w}px;height:{h+240}px;'
            f'background:radial-gradient(ellipse 50% 50% at 50% 40%,{t["spot"]},rgba(0,0,0,0) 70%)"></div>')


def vitrine(cx, pid, title, sub, t, e, w=700):
    """Free-standing object: glass case on a pedestal; photo edges fade into the lit interior."""
    top, bot = Y(1.3), Y(-0.55)
    hgt = bot - top
    interior = ('radial-gradient(ellipse 70% 75% at 50% 45%,#f4f2ee 0%,#c9c6bf 60%,#8f8b84 100%)' if e['case'] != '#3a312a'
                and e['case'] != '#202832' else 'radial-gradient(ellipse 70% 75% at 50% 45%,#6e655c 0%,#3b332c 65%,#1d1814 100%)')
    s = spot(cx, top, w * 0.9, hgt, t, 1.2)
    s += f'<div class="floorshadow" style="left:{cx-w*0.62}px;top:{FLOOR_TOP-26}px;width:{w*1.24}px"></div>'
    s += (f'<div class="pedestal" style="left:{cx-w/2-10}px;top:{bot}px;width:{w+20}px;height:{FLOOR_TOP-bot}px;'
          f'background:linear-gradient(180deg,{e["plinthTop"]} 0,{e["plinthTop"]} 14px,{e["plinth"]} 15px,{e["plinth"]} 100%)"></div>')
    s += (f'<div class="vit" style="left:{cx-w/2}px;top:{top}px;width:{w}px;height:{hgt}px;background:{interior}">'
          f'<div class="toplight"></div>'
          f'<img class="obj" src="{img(pid)}">'
          f'<div class="glass"></div></div>')
    s += label(cx, bot + 40, title, sub, t, min(520, w - 20))
    return s


def wallcase(cx, inner, title, sub, t, e, w=600, top=None, bot=None):
    top = Y(1.45) if top is None else top
    bot = Y(-0.85) if bot is None else bot
    s = spot(cx, top, w, bot - top, t)
    s += (f'<div class="wallcase" style="left:{cx-w/2}px;top:{top}px;width:{w}px;height:{bot-top}px;border-color:{e["frame"]}">'
          f'{inner}<div class="glass"></div></div>')
    s += label(cx, bot + 26, title, sub, t)
    return s


def painting_inner(pid, e):
    return (f'<div class="mount" style="background:{e["mount"]}"><div class="roller"></div>'
            f'<img class="pic" src="{img(pid)}"><div class="roller b"></div></div>')


def screen(cx, pid, title, sub, t, e, starry=False):
    w, hgt = 680, 470
    top = Y(0.15) - hgt / 2 - 40
    s = spot(cx, top, w, hgt, t, 0.8)
    bg = ('radial-gradient(ellipse at 70% 20%,#3a2a7a 0,#0a1030 60%)' if starry else '#0d1520')
    s += f'<div class="stand" style="left:{cx-14}px;top:{top+hgt}px;height:{FLOOR_TOP-top-hgt}px"></div>'
    s += f'<div class="standfoot" style="left:{cx-120}px;top:{FLOOR_TOP-18}px"></div>'
    s += (f'<div class="screen" style="left:{cx-w/2}px;top:{top}px;width:{w}px;height:{hgt}px;background:{bg}">'
          f'<img class="scr" src="{img(pid)}" style="{"box-shadow:0 0 50px rgba(140,170,255,.55);filter:saturate(1.1) brightness(1.05)" if starry else ""}">'
          + (f'<div class="stars"></div>' if starry else '') + f'<div class="scrglow"></div></div>')
    s += label(cx, top + hgt + 70, title, sub, t, 520)
    return s


def panel(cx, svg_markup, title, t, e):
    w, hgt = 780, 620
    top = Y(0.15) - hgt / 2
    s = spot(cx, top, w, hgt, t, 0.8)
    s += (f'<div class="panel" style="left:{cx-w/2}px;top:{top}px;width:{w}px;height:{hgt}px;background:{t["bay"]};border-color:{t["bayEdge"]}">'
          f'<div class="art">{svg_markup}</div></div>')
    s += label(cx, top + hgt + 26, title, '展覽說明板', t)
    return s


def scripts_case(cx, title, t, e):
    w = 860; top, bot = Y(1.35), Y(-0.85)
    inner = '<div class="quad">'
    for pid, ch, who in SCRIPTS:
        inner += (f'<div class="q"><div class="qm" style="background:{e["mount"]}"><img src="{img(pid)}"></div>'
                  f'<div class="qc"><b>{ch}</b>{who}</div></div>')
    inner += '</div>'
    return wallcase(cx, inner, title, '篆・隸・楷・草｜國立故宮博物院藏', t, e, w=w, top=top, bot=bot)



def photo_inner(pid):
    return f'<div class="mat"><img class="pic" src="{img(pid)}"></div>'


def multi_vitrine(cx, items, title, sub, t, e):
    w, top, bot = 760, Y(1.3), Y(-0.55)
    hgt = bot - top
    dark = e['case'] in ('#3a312a', '#202832')
    interior = ('radial-gradient(ellipse 70% 75% at 50% 45%,#6e655c 0%,#3b332c 65%,#1d1814 100%)' if dark else
                'radial-gradient(ellipse 70% 75% at 50% 45%,#f4f2ee 0%,#c9c6bf 60%,#8f8b84 100%)')
    s = spot(cx, top, w * 0.9, hgt, t, 1.2)
    s += f'<div class="floorshadow" style="left:{cx-w*0.62}px;top:{FLOOR_TOP-26}px;width:{w*1.24}px"></div>'
    s += (f'<div class="pedestal" style="left:{cx-w/2-10}px;top:{bot}px;width:{w+20}px;height:{FLOOR_TOP-bot}px;'
          f'background:linear-gradient(180deg,{e["plinthTop"]} 0,{e["plinthTop"]} 14px,{e["plinth"]} 15px,{e["plinth"]} 100%)"></div>')
    cells = ''.join(f'<div class="mc"><img src="{img(p)}"><span style="color:{"#f3ead6" if dark else "#2b2622"}">{c}</span></div>' for p, c in items)
    s += (f'<div class="vit" style="left:{cx-w/2}px;top:{top}px;width:{w}px;height:{hgt}px;background:{interior}">'
          f'<div class="toplight"></div><div class="multi">{cells}</div><div class="glass"></div></div>')
    s += label(cx, bot + 40, title, sub, t, 600)
    return s


def multi_wall(cx, items, title, sub, t, e):
    inner = '<div class="pair">' + ''.join(
        f'<div class="pc"><div class="mount" style="background:{e["mount"]}"><img class="pic" src="{img(p)}"></div><span>{c}</span></div>'
        for p, c in items) + '</div>'
    return wallcase(cx, inner, title, sub, t, e, w=860)


def map_inner(routes, base='asia-satellite', W_=1440, H_=720):
    svg = f'<svg viewBox="0 0 {W_} {H_}" class="mapsvg" preserveAspectRatio="none">'
    seen = {}
    for r in routes:
        pts = [(x * W_, y * H_) for _, (x, y) in r]
        d = 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts)
        svg += f'<path d="{d}" fill="none" stroke="#ffd23f" stroke-width="9" stroke-dasharray="26 14" stroke-linecap="round"/>'
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        a = math.degrees(math.atan2(y2 - y1, x2 - x1))
        svg += f'<path d="M0 -18 L34 0 L0 18 Z" fill="#ffd23f" transform="translate({x2:.0f} {y2:.0f}) rotate({a:.0f})"/>'
        for name, (x, y) in r:
            seen[name] = (x * W_, y * H_)
    for name, (x, y) in seen.items():
        svg += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="14" fill="#e63b2e" stroke="#fff" stroke-width="5"/>'
        svg += (f'<text x="{x+22:.0f}" y="{y-16:.0f}" font-size="50" font-weight="900" fill="#fff" stroke="#000" stroke-width="10" '
                f'paint-order="stroke" font-family="Noto Sans CJK TC">{name}</text>')
    svg += '</svg>'
    return f'<div class="mapbox" style="aspect-ratio:{W_}/{H_}"><img class="mapimg" src="{img(base)}">{svg}</div>'


def exhibit(cx, h, fn, t, e):
    hid = h['id']
    if hid == 'c-scripts':
        return scripts_case(cx, h['title'], t, e)
    if hid in MAPS:
        return wallcase(cx, (map_inner(MAPS[hid], 'asia-satellite-him', 1200, 720) if hid == 'h-route' else map_inner(MAPS[hid])), h['title'], '底圖：NASA Blue Marble 衛星影像（公有領域）', t, e, w=900, top=Y(1.15), bot=Y(-0.75))
    if hid in MULTI:
        kind, items, line = MULTI[hid]
        sub = f'{line}｜國立故宮博物院藏'
        return multi_vitrine(cx, items, h['title'], sub, t, e) if kind == 'object' else multi_wall(cx, items, h['title'], sub, t, e)
    if hid in REAL:
        pid, kind, name = REAL[hid]
        sub = name if '｜' in name else f'{name}｜國立故宮博物院藏'
        if kind == 'photo':
            return wallcase(cx, photo_inner(pid), h['title'], sub, t, e, w=820, top=Y(1.2), bot=Y(-0.8))
        if kind == 'object':
            return vitrine(cx, pid, h['title'], sub, t, e)
        if kind == 'painting':
            return wallcase(cx, painting_inner(pid, e), h['title'], sub, t, e)
        if kind == 'screen':
            return screen(cx, pid, h['title'], sub, t, e, starry=(hid == 'c-qianwen'))
    return panel(cx, fn(), h['title'], t, e)


def title_wall(era, t, room):
    cx = X(0)
    s = spot(cx, Y(1.6), 1500, 900, t, 1.0)
    s += f'<div class="title-wrap" style="left:{cx-820}px;top:{Y(1.35)}px;width:1640px">{room["title"]()}'
    s += f'<div class="t-intro">{era["intro"].split("轉動畫面")[0]}</div>'
    s += '<div class="t-note">示意場景，非故宮實景｜圖片：國立故宮博物院 Open Data（CC0）、大都會藝術博物館、NASA、Wikimedia Commons，出處見各說明牌</div></div>'
    return s


def room_html(era):
    rid = era['id']; t = THEMES[rid]; e = EXTRA[rid]; room = art.ROOMS[rid]
    hs = [h for h in era['hotspots'] if 'egg' not in h['id']]
    egg = [h for h in era['hotspots'] if 'egg' in h['id']][0]
    body = mural(t['mural'], t)
    for i, fn in enumerate(room['exhibits']):
        body += exhibit(X(SLOTS[i]), hs[i], fn, t, e)
    body += title_wall(era, t, room)
    for ex in (X(-180), X(180)):
        if egg['id'] in REAL:
            pid, kind, name = REAL[egg['id']]
            sub = name if '｜' in name else f'{name}｜國立故宮博物院藏'
            if kind == 'painting':
                body += wallcase(ex, painting_inner(pid, e), egg['title'].replace('彩蛋：', '彩蛋・'), sub, t, e, w=470)
            else:
                body += vitrine(ex, pid, egg['title'].replace('彩蛋：', '彩蛋・'), sub, t, e, w=540)
        else:
            w, hgt = 560, 470; top = Y(0.45) - hgt / 2
            body += spot(ex, top, w, hgt, t, 0.7)
            body += (f'<div class="panel" style="left:{ex-w/2}px;top:{top}px;width:{w}px;height:{hgt}px;background:{t["bay"]};border-color:{t["bayEdge"]}">'
                     f'<div class="art">{room["egg"]()}</div></div>')
            body += label(ex, top + hgt + 26, egg['title'].replace('彩蛋：', '彩蛋・'), '展覽說明板', t, 480)
    css = f'''
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W+2*M}px;height:{H}px;overflow:hidden}}
body{{position:relative;font-family:'Noto Sans CJK TC',sans-serif;
 background:
  url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .07 0'/></filter><rect width='400' height='400' filter='url(%23n)'/></svg>"),
  linear-gradient(180deg,rgba(0,0,0,.28) 0,rgba(0,0,0,0) 110px),
  linear-gradient(180deg,{t['wall2']} 0%,{t['wall']} 30%,{t['wall']} 78%,{t['wall2']} 100%);}}
.mural{{position:absolute;left:0;top:0}}
.band{{position:absolute;left:0;width:100%}}
.beam,.spot{{position:absolute;pointer-events:none}}
.beam{{clip-path:polygon(44% 0,56% 0,100% 100%,0 100%);filter:blur(6px)}}
.vit{{position:absolute;border:3px solid rgba(255,255,255,.55);border-bottom:none;overflow:hidden;box-shadow:0 0 0 2px rgba(0,0,0,.25),0 30px 60px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center}}
.toplight{{position:absolute;left:0;right:0;top:0;height:16px;background:linear-gradient(#fffbea,#e9e2cf);box-shadow:0 6px 30px rgba(255,248,220,.9)}}
.obj{{width:96%;height:90%;object-fit:contain;margin-top:20px;-webkit-mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 72%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 72%,transparent 100%)}}
.glass{{position:absolute;inset:0;pointer-events:none;background:linear-gradient(112deg,rgba(255,255,255,0) 22%,rgba(255,255,255,.22) 30%,rgba(255,255,255,0) 38%,rgba(255,255,255,0) 62%,rgba(255,255,255,.12) 66%,rgba(255,255,255,0) 71%)}}
.pedestal{{position:absolute;box-shadow:inset 0 -30px 40px rgba(0,0,0,.25),inset 10px 0 20px rgba(255,255,255,.08)}}
.floorshadow{{position:absolute;height:40px;border-radius:50%;background:radial-gradient(ellipse,rgba(0,0,0,.45),rgba(0,0,0,0) 70%)}}
.wallcase{{position:absolute;border:14px solid;border-radius:4px;background:linear-gradient(#2a221c,#16110d);box-shadow:inset 0 0 50px rgba(0,0,0,.6),0 24px 50px rgba(0,0,0,.4);display:flex;align-items:center;justify-content:center;overflow:hidden}}
.mount{{position:relative;height:92%;max-width:92%;padding:34px 26px;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 30px rgba(0,0,0,.5)}}
.mount .pic{{max-height:100%;max-width:100%;display:block;box-shadow:0 0 0 2px rgba(80,60,30,.35)}}
.roller{{position:absolute;left:-10px;right:-10px;top:-6px;height:16px;border-radius:8px;background:linear-gradient(#7a5434,#3e2816)}}
.roller.b{{top:auto;bottom:-8px;height:20px}}
.screen{{position:absolute;border:18px solid #111418;border-radius:16px;box-shadow:0 0 60px rgba(90,170,255,.35),0 24px 50px rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;overflow:hidden}}
.scr{{max-width:82%;max-height:78%;position:relative;z-index:1}}
/*s*/.stars{{position:absolute;inset:0;background-image:radial-gradient(2px 2px at 8% 12%,#fff,transparent),radial-gradient(2px 2px at 20% 80%,#fff,transparent),radial-gradient(3px 3px at 92% 18%,#fff,transparent),radial-gradient(2px 2px at 85% 88%,#fff,transparent),radial-gradient(2px 2px at 50% 6%,#fff,transparent),radial-gradient(2px 2px at 4% 55%,#fff,transparent),radial-gradient(2px 2px at 96% 60%,#fff,transparent)}}
.scrglow{{position:absolute;inset:0;background:linear-gradient(160deg,rgba(255,255,255,.12),rgba(255,255,255,0) 40%)}}
.stand{{position:absolute;width:28px;background:linear-gradient(90deg,#2a2f36,#4a525c,#2a2f36)}}
.standfoot{{position:absolute;width:240px;height:18px;border-radius:9px;background:#22272d}}
.panel{{position:absolute;border:6px solid;border-radius:6px;box-shadow:0 18px 40px rgba(0,0,0,.35);overflow:hidden;display:flex;align-items:center;justify-content:center}}
.panel .art{{width:92%}} .panel .art svg{{width:100%;height:auto;display:block}}
.label{{position:absolute;text-align:left;padding:12px 20px 12px 26px;border-radius:4px;box-shadow:0 8px 20px rgba(0,0,0,.35);border-left:10px solid rgba(0,0,0,.25)}}
.label .lt{{font-size:40px;font-weight:900;line-height:1.2}}
.label .ls{{font-size:23px;font-weight:500;opacity:.8;margin-top:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.mat{{background:#f7f4ec;padding:22px;box-shadow:0 12px 30px rgba(0,0,0,.5);max-width:92%;max-height:90%;display:flex}}
.mat .pic{{max-width:100%;max-height:100%;display:block}}
.multi{{display:flex;gap:18px;align-items:flex-end;justify-content:center;width:94%;height:86%;margin-top:24px}}
.mc{{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}}
.mc img{{max-width:100%;max-height:82%;object-fit:contain;-webkit-mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 70%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 70%,transparent 100%)}}
.mc span{{font-size:30px;font-weight:900;margin-top:6px}}
.pair{{display:flex;gap:26px;height:90%;width:94%}}
.pc{{flex:1;display:flex;flex-direction:column;align-items:center;gap:10px;min-width:0}}
.pc .mount{{height:86%;padding:16px}} .pc span{{color:#ffd76a;font-size:34px;font-weight:900}}
.mapbox{{position:relative;width:96%;aspect-ratio:2/1}}
.mapimg{{width:100%;height:100%;display:block}}
.mapsvg{{position:absolute;inset:0;width:100%;height:100%}}
.quad{{display:flex;gap:22px;height:90%;align-items:stretch}}
.q{{display:flex;flex-direction:column;align-items:center;gap:10px}}
.qm{{flex:1;padding:14px 10px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px rgba(0,0,0,.5)}}
.qm img{{max-height:100%;max-width:160px;display:block}}
.qc{{color:#f3e7c9;font-size:26px}} .qc b{{font-size:44px;margin-right:6px;color:#ffd76a}}
.title-wrap{{position:absolute;text-align:center}}
.title-plate .t-kicker{{font-size:48px;font-weight:700;letter-spacing:6px}}
.title-plate .t-main{{font-size:190px;line-height:1.15;font-weight:900;letter-spacing:18px}}
.title-plate .t-sub{{font-size:64px;font-weight:700;letter-spacing:8px;margin-top:6px}}
.title-plate .t-date{{font-size:44px;margin-top:22px;letter-spacing:4px;opacity:.85}}
.t-intro{{margin:34px auto 0;max-width:1300px;font-size:36px;line-height:1.7;color:{t['label'] if rid in LIGHT_INTERIOR and rid!='himalaya' and rid!='tiantuan' else '#f3ead6'};opacity:.92}}
.t-note{{margin-top:26px;font-size:26px;opacity:.7;color:{'#3a3226' if rid in ('fishing','tea') else '#f3ead6'}}}
'''
    bands = f'<div class="band" style="top:0;height:28px;background:{t["band"]}"></div>'
    bands += f'<div class="band" style="top:{H-56}px;height:56px;background:{t["band"]};filter:brightness(.6)"></div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{bands}{body}</body></html>'


def floor_decal(era, path, D=2400):
    """Top-down floor graphic: centre medallion with the room badge, station numbers in front of each case."""
    from PIL import Image, ImageDraw, ImageFont
    from project import R
    t = THEMES[era['id']]; ch, c1, c2 = BADGES[era['id']]
    im = Image.new('RGBA', (D, D), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    s = D / (2 * R)
    def P(x, z): return (D / 2 + x * s, D / 2 - z * s)
    fb = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
    fs = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Black.ttc'
    if not os.path.exists(fb): fb = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
    def hexrgb(h, a=255): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) + (a,)
    cx, cy = P(0, 0)
    for rr, wdt, a in [(1.05, 10, 200), (0.98, 3, 160), (0.62, 0, 0)]:
        if wdt: d.ellipse([cx - rr * s, cy - rr * s, cx + rr * s, cy + rr * s], outline=hexrgb(c1, a), width=wdt)
    d.ellipse([cx - 0.6 * s, cy - 0.6 * s, cx + 0.6 * s, cy + 0.6 * s], fill=hexrgb(c1, 215))
    d.ellipse([cx - 0.53 * s, cy - 0.53 * s, cx + 0.53 * s, cy + 0.53 * s], outline=hexrgb(c2, 220), width=5)
    f = ImageFont.truetype(fs if os.path.exists(fs) else fb, int(0.62 * s))
    d.text((cx, cy), ch, font=f, fill=hexrgb(c2, 235), anchor='mm')
    # dotted guide ring + numbered markers
    for k in range(120):
        a = 2 * math.pi * k / 120; x, y = P(1.75 * math.sin(a), 1.75 * math.cos(a))
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=hexrgb(c1, 120))
    fn = ImageFont.truetype(fb, int(0.3 * s))
    for i, yaw in enumerate(SLOTS):
        a = math.radians(yaw); r0 = 2.35
        tile = Image.new('RGBA', (int(0.7 * s), int(0.7 * s)), (0, 0, 0, 0)); td = ImageDraw.Draw(tile)
        w_ = tile.size[0]
        td.ellipse([4, 4, w_ - 4, w_ - 4], fill=hexrgb(c1, 225), outline=hexrgb(c2, 255), width=6)
        td.text((w_ / 2, w_ / 2), str(i + 1), font=fn, fill=hexrgb(c2, 255), anchor='mm')
        tile = tile.rotate(-yaw, resample=Image.BICUBIC, expand=True)
        x, y = P(r0 * math.sin(a), r0 * math.cos(a))
        im.alpha_composite(tile, (int(x - tile.size[0] / 2), int(y - tile.size[1] / 2)))
    im.save(path)


async def shoot(pages, outdir):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': W + 2 * M, 'height': H}, device_scale_factor=1)
        for rid, html in pages:
            path = os.path.join(outdir, f'wall2_{rid}.html')
            open(path, 'w', encoding='utf-8').write(html)
            await pg.goto('file://' + path); await pg.wait_for_timeout(500)
            await pg.screenshot(path=os.path.join(outdir, f'wall2full_{rid}.png'), clip={'x': M, 'y': 0, 'width': W, 'height': H})
            print('shot', rid, flush=True)
        await b.close()


if __name__ == '__main__':
    outdir = os.path.abspath(sys.argv[1]); only = sys.argv[2:] or [e['id'] for e in ERAS]
    os.makedirs(outdir, exist_ok=True)
    eras = [e for e in ERAS if e['id'] in only]
    asyncio.run(shoot([(e['id'], room_html(e)) for e in eras], outdir))
    from project import render
    for e in eras:
        rid = e['id']; dec = os.path.join(outdir, f'floor_{rid}.png'); floor_decal(e, dec)
        th = dict(THEMES[rid]); th['slots'] = SLOTS; th['decal'] = dec
        render(os.path.join(outdir, f'wall2full_{rid}.png'), os.path.join(outdir, f'pano2_{rid}.jpg'), th)
        print('pano', rid, flush=True)
