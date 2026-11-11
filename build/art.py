# -*- coding: utf-8 -*-
# Original flat-vector illustrations for every exhibit (viewBox 0 0 700 560).
# All drawings are stylised interpretations made for this lesson, not reproductions.

DEFS = '''
<defs>
  <filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#000" flood-opacity=".35"/></filter>
  <filter id="soft"><feGaussianBlur stdDeviation="2"/></filter>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff1b8"/><stop offset=".35" stop-color="#e2b247"/><stop offset=".7" stop-color="#a8741c"/><stop offset="1" stop-color="#f3cf6b"/></linearGradient>
  <linearGradient id="bronze" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c79a5b"/><stop offset=".5" stop-color="#8a5a2b"/><stop offset="1" stop-color="#5a3a1c"/></linearGradient>
  <linearGradient id="jade" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e9f5df"/><stop offset=".5" stop-color="#b9d9b0"/><stop offset="1" stop-color="#86b48a"/></linearGradient>
  <linearGradient id="jadeg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6fbf73"/><stop offset=".55" stop-color="#cfe8c4"/><stop offset="1" stop-color="#f6f8ee"/></linearGradient>
  <linearGradient id="ivory" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff9ea"/><stop offset=".6" stop-color="#efe0bd"/><stop offset="1" stop-color="#d6c095"/></linearGradient>
  <linearGradient id="lacq" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e2463a"/><stop offset=".6" stop-color="#b3221c"/><stop offset="1" stop-color="#7d1410"/></linearGradient>
  <linearGradient id="porc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d9dde0"/><stop offset=".35" stop-color="#ffffff"/><stop offset="1" stop-color="#c9ced3"/></linearGradient>
  <linearGradient id="bamboo" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e9c78f"/><stop offset=".6" stop-color="#c3955a"/><stop offset="1" stop-color="#8f6435"/></linearGradient>
  <linearGradient id="paper" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4ead2"/><stop offset="1" stop-color="#e8d9b5"/></linearGradient>
  <linearGradient id="silk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#efe3c4"/><stop offset="1" stop-color="#ddc99e"/></linearGradient>
  <linearGradient id="clay" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a5634a"/><stop offset=".6" stop-color="#7a3d2a"/><stop offset="1" stop-color="#55281b"/></linearGradient>
  <linearGradient id="black" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4a3a30"/><stop offset=".5" stop-color="#1c1410"/><stop offset="1" stop-color="#3a2a20"/></linearGradient>
  <linearGradient id="celadon" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b9cfa0"/><stop offset=".6" stop-color="#7f9a5f"/><stop offset="1" stop-color="#55703f"/></linearGradient>
  <linearGradient id="screen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1b2e"/><stop offset="1" stop-color="#1b3554"/></linearGradient>
  <linearGradient id="stone" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b9b2a5"/><stop offset=".6" stop-color="#8f877a"/><stop offset="1" stop-color="#6e675c"/></linearGradient>
  <radialGradient id="halo"><stop offset="0" stop-color="#fff3c4" stop-opacity=".95"/><stop offset=".7" stop-color="#f1c45c" stop-opacity=".55"/><stop offset="1" stop-color="#f1c45c" stop-opacity="0"/></radialGradient>
  <radialGradient id="foam"><stop offset="0" stop-color="#ffffff"/><stop offset=".8" stop-color="#eef3e6"/><stop offset="1" stop-color="#cfdcb8"/></radialGradient>
  <pattern id="waves" width="40" height="20" patternUnits="userSpaceOnUse"><path d="M0 15 Q10 5 20 15 T40 15" fill="none" stroke="#6b8fa3" stroke-width="2"/></pattern>
</defs>
'''


def svg(inner, w=700, h=560, extra=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {extra}>{DEFS}{inner}</svg>'


# ---------------------------------------------------------------- shared pieces
def scroll(x, y, w, h, inner, roller='#5a3b22', mount='#d8c7a0'):
    """Hanging scroll: mounting, painting area (inner drawn in local coords 0..w,0..h)."""
    return f'''
<g filter="url(#sh)">
  <rect x="{x-18}" y="{y-60}" width="{w+36}" height="{h+130}" fill="{mount}" rx="3"/>
  <rect x="{x-24}" y="{y-72}" width="{w+48}" height="14" fill="{roller}" rx="7"/>
  <rect x="{x-30}" y="{y+h+62}" width="{w+60}" height="18" fill="{roller}" rx="9"/>
  <line x1="{x+w/2}" y1="{y-72}" x2="{x+w/2}" y2="{y-110}" stroke="#3b2a1a" stroke-width="3"/>
  <svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
    <rect width="{w}" height="{h}" fill="url(#silk)"/>{inner}
  </svg>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#8b6d43" stroke-width="2"/>
</g>'''


def ink_mountains(w, h, base, n=3, seed=1, col='#5d6b6a'):
    import random
    rnd = random.Random(seed)
    out = ''
    for k in range(n):
        y0 = base - k * h * 0.12
        pts = [(0, h)]
        x = 0
        while x <= w:
            pts.append((x, y0 - rnd.uniform(0.05, 0.28) * h * (1 - k * 0.2)))
            x += rnd.uniform(w * 0.12, w * 0.25)
        pts.append((w, y0 - rnd.uniform(0.05, 0.2) * h)); pts.append((w, h))
        d = 'M' + ' L'.join(f'{a:.0f} {b:.0f}' for a, b in pts) + ' Z'
        op = 0.18 + 0.16 * (n - k) / n
        out += f'<path d="{d}" fill="{col}" opacity="{op:.2f}"/>'
    return out


def boat(x, y, s=1.0, fisher=True, net=False, rod=False, col='#3d3326'):
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += f'<path d="M-60 0 Q0 22 60 0 L50 -6 Q0 8 -50 -6 Z" fill="{col}"/>'
    if fisher:
        g += f'<circle cx="8" cy="-34" r="7" fill="{col}"/><path d="M-4 -40 L8 -50 L20 -40 Z" fill="#7a6a4a"/>'
        g += f'<path d="M2 -27 L16 -27 L20 -4 L-2 -4 Z" fill="{col}"/>'
    if rod:
        g += '<path d="M16 -24 Q60 -70 110 -60" fill="none" stroke="#3d3326" stroke-width="2"/><line x1="110" y1="-60" x2="112" y2="10" stroke="#3d3326" stroke-width="1"/>'
    if net:
        g += '<path d="M14 -24 Q40 -50 70 -10 Q50 10 20 2" fill="rgba(80,70,50,.18)" stroke="#5a4c34" stroke-width="1.5" stroke-dasharray="3 3"/>'
    return g + '</g>'


def figure(x, y, s=1.0, robe='#c24a3a', face='#f2d2b0', hat=None, sitting=False):
    g = f'<g transform="translate({x} {y}) scale({s})">'
    if sitting:
        g += f'<path d="M-26 0 Q-30 -40 -14 -56 L14 -56 Q30 -40 26 0 Z" fill="{robe}"/>'
    else:
        g += f'<path d="M-22 0 L-16 -60 L16 -60 L22 0 Z" fill="{robe}"/>'
    g += f'<circle cx="0" cy="-72" r="14" fill="{face}"/>'
    if hat:
        g += f'<path d="M-22 -78 L0 -96 L22 -78 Z" fill="{hat}"/>'
    g += '<path d="M-5 -72 a1.6 1.6 0 1 0 0.1 0 M5 -72 a1.6 1.6 0 1 0 0.1 0" fill="#3a2a20"/><path d="M-5 -65 Q0 -61 5 -65" stroke="#7a3b2a" stroke-width="1.6" fill="none"/>'
    return g + '</g>'


# ================================================================ 1. HIMALAYA
def him_mountain():
    peaks = ''
    xs = [60, 140, 220, 300, 380, 470, 560, 640]
    hs = [180, 260, 210, 330, 250, 300, 220, 170]
    d = 'M20 430 ' + ' '.join(f'L{x} {430-h}' + (f' L{x+40} {430-h*0.55}' if i < len(xs)-1 else '') for i, (x, h) in enumerate(zip(xs, hs))) + ' L680 430 Z'
    snow = ''.join(f'<path d="M{x-22} {430-h+38} L{x} {430-h} L{x+22} {430-h+38} L{x+8} {430-h+30} L{x} {430-h+44} L{x-8} {430-h+30} Z" fill="#fff"/>' for x, h in zip(xs, hs))
    return svg(f'''
<rect x="20" y="430" width="660" height="70" rx="8" fill="#5b3a2a" filter="url(#sh)"/>
<rect x="30" y="440" width="640" height="50" fill="#7c5a3d"/>
<path d="{d}" fill="#7d8c96" filter="url(#sh)"/>
<path d="{d}" fill="url(#stone)" opacity=".55"/>{snow}
<path d="M300 100 L300 60" stroke="#c0392b" stroke-width="3"/><path d="M300 60 L330 70 L300 80 Z" fill="#c0392b"/>
<text x="350" y="530" font-size="30" text-anchor="middle" fill="#5e211b" font-family="Noto Sans CJK TC" font-weight="700">約 2,500 公里・平均海拔 6,000 公尺以上</text>
<g font-family="Noto Sans CJK TC" font-size="22" fill="#fff" font-weight="700">
<text x="70" y="470">南亞次大陸</text><text x="520" y="470">青藏高原</text></g>''')


def him_ganges():
    return svg(scroll(160, 70, 380, 380, f'''
<rect width="380" height="380" fill="#f3e2b8"/>
<circle cx="300" cy="70" r="36" fill="#f39c45" opacity=".85"/>
<path d="M0 250 Q90 220 190 250 T380 240 L380 380 L0 380 Z" fill="#7fb0b9"/>
<path d="M0 270 Q100 245 190 270 T380 262" stroke="#d6edf0" stroke-width="3" fill="none"/>
<path d="M0 310 Q100 290 200 312 T380 300" stroke="#d6edf0" stroke-width="2" fill="none"/>
<g transform="translate(110 250)"><rect x="-40" y="-20" width="80" height="20" fill="#d9b178"/><path d="M-32 -20 Q0 -95 32 -20 Z" fill="#efd7a5" stroke="#a87c43" stroke-width="2"/><rect x="-4" y="-110" width="8" height="22" fill="#a87c43"/><circle cx="0" cy="-114" r="7" fill="#e2b247"/></g>
<g fill="#5f8f4a"><path d="M250 250 q10 -60 0 -110 q-10 50 0 110"/><path d="M250 160 q-30 -10 -50 10 q30 -2 50 -10 q30 -10 50 10 q-30 -2 -50 -10"/></g>
{''.join(f'<g transform="translate({x} {y})"><ellipse rx="22" ry="7" fill="#4f8a55"/><path d="M-10 0 Q-6 -24 0 -26 Q6 -24 10 0 Z" fill="#f0a6b8"/><path d="M-4 -2 Q0 -22 4 -2 Z" fill="#fbd3dc"/></g>' for x, y in [(60,320),(170,340),(300,330),(330,360)])}
''', mount='#c9a46a'))


def him_route():
    return svg(f'''
<rect x="40" y="40" width="620" height="440" rx="18" fill="#efe1c3" stroke="#8a6a3d" stroke-width="6" filter="url(#sh)"/>
<path d="M60 380 Q200 330 300 360 T640 330 L640 470 L60 470 Z" fill="#cfe0b0"/>
<path d="M60 200 L640 200 L640 60 L60 60 Z" fill="#e6dccb"/>
<path d="M70 300 L150 170 L200 240 L260 130 L320 230 L380 120 L440 220 L500 140 L560 230 L630 170 L630 300 Z" fill="#9aa5ab"/>
<path d="M248 150 L260 130 L272 150 Z M368 140 L380 120 L392 140 Z M488 160 L500 140 L512 160 Z" fill="#fff"/>
<path d="M120 430 C200 400 230 330 270 280 S330 200 390 150 S470 100 560 95" fill="none" stroke="#c0392b" stroke-width="7" stroke-dasharray="18 10" stroke-linecap="round"/>
<path d="M548 80 L580 95 L548 110 Z" fill="#c0392b"/>
<g font-family="Noto Sans CJK TC" font-weight="700" font-size="24" fill="#4a3220">
<text x="90" y="455">恆河平原</text><text x="190" y="330">喀什米爾</text><text x="300" y="300">尼泊爾</text><text x="470" y="80">西藏高原（雪域）</text></g>
<circle cx="120" cy="430" r="10" fill="#c0392b"/><circle cx="560" cy="95" r="10" fill="#c0392b"/>''')


def him_thangka():
    def mandala(cx, cy, r):
        s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f2c14e" stroke="#7a1d12" stroke-width="3"/>'
        s += f'<circle cx="{cx}" cy="{cy}" r="{r*0.82}" fill="#2a5d8f"/>'
        s += f'<rect x="{cx-r*0.55}" y="{cy-r*0.55}" width="{r*1.1}" height="{r*1.1}" fill="#c0392b" stroke="#f2c14e" stroke-width="3"/>'
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            s += f'<rect x="{cx+dx*r*0.55-r*0.12}" y="{cy+dy*r*0.55-r*0.12}" width="{r*0.24}" height="{r*0.24}" fill="#f2c14e"/>'
        s += f'<circle cx="{cx}" cy="{cy}" r="{r*0.32}" fill="#1f7a5c" stroke="#f2c14e" stroke-width="3"/>'
        s += f'<circle cx="{cx}" cy="{cy}" r="{r*0.14}" fill="#fff4cc"/>'
        for k in range(8):
            import math
            a = k * math.pi / 4
            s += f'<circle cx="{cx+math.cos(a)*r*0.23:.1f}" cy="{cy+math.sin(a)*r*0.23:.1f}" r="{r*0.05:.1f}" fill="#f2c14e"/>'
        return s
    inner = '<rect width="340" height="420" fill="#a82418"/>'
    inner += '<rect x="10" y="10" width="320" height="400" fill="none" stroke="#f2c14e" stroke-width="3"/>'
    inner += mandala(90, 110, 70) + mandala(250, 110, 70) + mandala(90, 290, 70) + mandala(250, 290, 70)
    inner += ''.join(f'<path d="M{x} 400 L{x} 210 Q{x} 196 {x+8} 196" stroke="#f2c14e" stroke-width="4" fill="none"/>' for x in (20, 168, 316))
    inner += '<path d="M10 380 Q60 360 110 380 T210 380 T330 380" stroke="#4f9a6a" stroke-width="4" fill="none"/>'
    return svg(f'''
<g filter="url(#sh)"><rect x="160" y="20" width="380" height="520" fill="#2d6a9f"/><rect x="172" y="34" width="356" height="460" fill="#f2c14e"/>
<svg x="180" y="44" width="340" height="420" viewBox="0 0 340 420">{inner}</svg>
<rect x="150" y="10" width="400" height="16" fill="#5a3b22" rx="8"/><rect x="146" y="530" width="408" height="20" fill="#5a3b22" rx="10"/></g>''')


def him_newar():
    pig = [('#c0392b', '朱砂'), ('#2a5d8f', '青金石'), ('#1f7a5c', '孔雀石'), ('#e2b247', '金')]
    pots = ''.join(f'<g transform="translate({140+i*140} 410)"><ellipse rx="52" ry="18" fill="#6b4a2f"/><ellipse cy="-6" rx="46" ry="14" fill="{c}"/><text y="52" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="24" font-weight="700" fill="#4a3220">{n}</text></g>' for i, (c, n) in enumerate(pig))
    people = ''.join(figure(110 + i * 96, 300, 1.15, robe=['#7d3c98', '#c0392b', '#1f618d', '#b9770e', '#117a65', '#922b21'][i], hat=None) for i in range(6))
    return svg(f'''
<rect x="40" y="40" width="620" height="300" rx="16" fill="#f5e6c8" stroke="#8a6a3d" stroke-width="5" filter="url(#sh)"/>
<path d="M60 230 L170 120 L250 200 L340 100 L430 190 L520 110 L640 230" fill="none" stroke="#9aa5ab" stroke-width="6"/>
<text x="350" y="90" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="900" font-size="34" fill="#7a1d12">加德滿都谷地 ➜ 西藏俄寺</text>
{people}{pots}
<path d="M560 260 L640 180" stroke="#6b4a2f" stroke-width="6"/><path d="M640 180 l10 -14 l6 6 z" fill="#2a2a2a"/>''')


def him_king():
    return svg(f'''
<ellipse cx="350" cy="520" rx="170" ry="22" fill="#000" opacity=".35"/>
<rect x="210" y="470" width="280" height="50" rx="6" fill="#3b2a20"/>
<g filter="url(#sh)">
<path d="M262 470 Q240 360 270 260 L430 260 Q460 360 438 470 Z" fill="url(#gold)"/>
<path d="M250 300 Q180 250 150 160" stroke="url(#gold)" stroke-width="16" fill="none" stroke-linecap="round"/>
<path d="M450 300 Q520 250 550 180" stroke="url(#gold)" stroke-width="16" fill="none" stroke-linecap="round"/>
<path d="M200 330 Q150 300 120 240 Q160 270 220 280" fill="url(#gold)"/><path d="M500 330 Q550 300 580 240 Q540 270 480 280" fill="url(#gold)"/>
<rect x="300" y="300" width="100" height="70" rx="10" fill="#2a5d8f" stroke="#f3cf6b" stroke-width="5"/>
<path d="M312 335 q20 -20 38 0 t38 0" stroke="#f3cf6b" stroke-width="4" fill="none"/>
<circle cx="350" cy="205" r="62" fill="url(#gold)"/>
<path d="M290 168 Q350 100 410 168 L400 150 L350 120 L300 150 Z" fill="url(#gold)" stroke="#a8741c" stroke-width="3"/>
<circle cx="350" cy="140" r="9" fill="#1f9e8a"/><circle cx="318" cy="152" r="7" fill="#2a5d8f"/><circle cx="382" cy="152" r="7" fill="#2a5d8f"/>
<path d="M322 200 q10 -10 20 0 M358 200 q10 -10 20 0" stroke="#5a3a10" stroke-width="5" fill="none"/>
<circle cx="332" cy="206" r="6" fill="#3a2a10"/><circle cx="368" cy="206" r="6" fill="#3a2a10"/>
<path d="M330 238 L370 238" stroke="#5a3a10" stroke-width="5"/>
<rect x="138" y="122" width="22" height="58" rx="4" fill="#8a5a1c"/><rect x="124" y="176" width="50" height="10" rx="4" fill="url(#gold)"/>
<circle cx="552" cy="168" r="22" fill="#e9f3ff" stroke="url(#gold)" stroke-width="6"/>
</g>''')


def him_title():
    return '''<div class="title-plate" style="color:#f7e7c6">
<div class="t-kicker" style="color:#f2c14e">特別展覽・1F S101</div>
<div class="t-main">穿越喜瑪拉雅</div>
<div class="t-sub">從恆河到雪域的藝術行旅</div>
<div class="t-date">2026.10.08 – 2027.04.06</div></div>'''


def him_egg():
    return svg('''
<circle cx="350" cy="270" r="200" fill="#2e6f9e" filter="url(#sh)"/>
<path d="M210 190 q40 -60 110 -30 q20 40 -20 70 q-40 10 -50 50 q-30 20 -50 -20 q-20 -40 10 -70z" fill="#7fb069"/>
<path d="M400 160 q60 -20 90 30 q10 60 -40 80 q-40 -10 -50 -60 z" fill="#7fb069"/>
<path d="M430 330 q30 -10 40 20 q-10 30 -40 20 z" fill="#7fb069"/>
<path d="M240 240 C300 120 430 120 470 320" stroke="#f2c14e" stroke-width="7" fill="none" stroke-dasharray="14 10"/>
<path d="M458 316 L472 344 L484 314 Z" fill="#f2c14e"/>
<circle cx="240" cy="240" r="12" fill="#c0392b"/><circle cx="472" cy="330" r="12" fill="#c0392b"/>''')


# ================================================================ 2. FISHING
def fish_net():
    inner = '<rect width="300" height="400" fill="url(#silk)"/>' + ink_mountains(300, 400, 170, 3, 3)
    inner += '<circle cx="230" cy="70" r="26" fill="#f0b27a" opacity=".7"/>'
    inner += '<path d="M0 230 L300 230 L300 400 L0 400 Z" fill="#c9d6cf" opacity=".5"/>'
    inner += boat(90, 270, 0.9, net=True) + boat(210, 330, 0.75, net=True) + boat(120, 370, 0.6)
    inner += ''.join(f'<path d="M{x} {y} q15 -6 30 0" stroke="#7d8a86" stroke-width="1.5" fill="none"/>' for x, y in [(30,300),(200,280),(150,350),(240,380)])
    return svg(scroll(200, 90, 300, 400, inner))


def fish_family():
    inner = '<rect width="420" height="300" fill="url(#silk)"/>' + ink_mountains(420, 300, 110, 2, 7)
    inner += '<path d="M0 170 L420 170 L420 300 L0 300 Z" fill="#c9d6cf" opacity=".5"/>'
    inner += boat(120, 230, 1.0, fisher=False) + boat(220, 238, 1.0, fisher=False) + boat(315, 228, 0.95, fisher=False)
    inner += figure(100, 222, 0.42, robe='#4b5d55', sitting=True) + figure(140, 222, 0.42, robe='#6e5a3c', sitting=True)
    inner += figure(205, 230, 0.42, robe='#5a4c34', sitting=True) + figure(240, 230, 0.42, robe='#3d4b52', sitting=True)
    inner += figure(305, 220, 0.42, robe='#6a4a3a', sitting=True)
    inner += '<g fill="#9b6b3a"><ellipse cx="172" cy="216" rx="8" ry="10"/><ellipse cx="272" cy="222" rx="8" ry="10"/></g>'
    inner += '<path d="M20 160 q20 -40 0 -80 M40 160 q-10 -50 10 -90 M380 160 q10 -40 -10 -80" stroke="#8a9a7a" stroke-width="3" fill="none"/>'
    return svg(f'''<g filter="url(#sh)"><rect x="110" y="90" width="480" height="360" fill="#d8c7a0"/>
<svg x="140" y="120" width="420" height="300" viewBox="0 0 420 300">{inner}</svg>
<rect x="140" y="120" width="420" height="300" fill="none" stroke="#8b6d43" stroke-width="2"/></g>''')


def fish_snow():
    inner = '<rect width="300" height="400" fill="#eef0ee"/>' + ink_mountains(300, 400, 180, 3, 11, col='#6c7a80')
    inner += ''.join(f'<path d="M{x-14} {y} L{x} {y-30} L{x+14} {y} Z" fill="#fff"/>' for x, y in [(60,120),(150,95),(240,130)])
    inner += '<path d="M0 240 L300 240 L300 400 L0 400 Z" fill="#d9e1e4"/>'
    inner += boat(150, 320, 0.8, rod=True, col='#2f2f2f')
    inner += '<path d="M124 290 L160 270 L196 290 Z" fill="#8a7a50"/><path d="M128 300 Q160 330 192 300" fill="#a08c5a"/>'
    import random
    rnd = random.Random(5)
    inner += ''.join(f'<circle cx="{rnd.uniform(0,300):.0f}" cy="{rnd.uniform(0,400):.0f}" r="{rnd.uniform(1.5,3.2):.1f}" fill="#fff"/>' for _ in range(90))
    inner += '<g font-family="Noto Serif CJK TC" font-size="20" fill="#3a3a3a" writing-mode="tb"><text x="270" y="30">孤舟蓑笠翁</text><text x="245" y="30">獨釣寒江雪</text></g>'
    return svg(scroll(200, 90, 300, 400, inner))


def fish_hermit():
    inner = '<rect width="300" height="400" fill="url(#silk)"/>' + ink_mountains(300, 400, 150, 3, 21)
    inner += '<path d="M0 250 L300 250 L300 400 L0 400 Z" fill="#c9d6cf" opacity=".5"/>'
    inner += ''.join(f'<path d="M{x} 400 Q{x+6} 320 {x+14} {y}" stroke="#8a8a5a" stroke-width="2.5" fill="none"/><path d="M{x+14} {y} q-4 14 -10 18" stroke="#8a8a5a" stroke-width="5" fill="none"/>' for x, y in [(10,260),(30,240),(50,270),(230,250),(255,230),(275,262)])
    inner += boat(140, 320, 0.85, rod=True)
    inner += '<g transform="translate(120 290)"><rect x="-12" y="-10" width="40" height="8" fill="#6b5a3a"/></g>'
    inner += '<path d="M200 120 h60 v40 h-60z" fill="#a8a28a" opacity=".5"/><path d="M196 120 L230 100 L264 120 Z" fill="#6b6b5a" opacity=".6"/>'
    return svg(scroll(200, 90, 300, 400, inner))


def fish_zhuangzi():
    fish = ''.join(f'<g transform="translate({x} {y}) scale({s})"><path d="M-30 0 Q0 -18 30 0 Q0 18 -30 0 Z" fill="{c}"/><path d="M30 0 L48 -12 L48 12 Z" fill="{c}"/><circle cx="-16" cy="-3" r="3" fill="#222"/></g>' for x, y, s, c in [(220,420,1,'#e67e22'),(330,450,1.2,'#d35400'),(450,410,0.9,'#f39c12'),(560,455,1,'#e67e22')])
    return svg(f'''
<rect x="40" y="60" width="620" height="440" rx="14" fill="#e9f0ea" stroke="#8b6d43" stroke-width="6" filter="url(#sh)"/>
<path d="M50 330 L650 330 L650 490 L50 490 Z" fill="#9cc3c9"/>
<path d="M50 360 q60 -10 120 0 t120 0 t120 0 t120 0 t120 0" stroke="#d7eef0" stroke-width="3" fill="none"/>
<path d="M120 330 Q350 170 580 330" stroke="#7a5a3a" stroke-width="22" fill="none"/>
<path d="M120 330 Q350 190 580 330" stroke="#a0784e" stroke-width="6" fill="none"/>
{''.join(f'<line x1="{x}" y1="{330-((x-120)*(580-x))/350:.0f}" x2="{x}" y2="{300-((x-120)*(580-x))/350:.0f}" stroke="#7a5a3a" stroke-width="5"/>' for x in range(150, 580, 40))}
{figure(300, 222, 0.9, robe='#3d5a6e', hat='#2a2a2a')}{figure(400, 222, 0.9, robe='#7a4a3a', hat='#2a2a2a')}
{fish}
<g font-family="Noto Sans CJK TC" font-size="22" font-weight="700"><rect x="150" y="90" width="150" height="52" rx="26" fill="#fff" stroke="#3d5a6e" stroke-width="3"/><text x="225" y="125" text-anchor="middle" fill="#3d5a6e">魚好快樂！</text>
<rect x="400" y="90" width="210" height="52" rx="26" fill="#fff" stroke="#7a4a3a" stroke-width="3"/><text x="505" y="125" text-anchor="middle" fill="#7a4a3a">你又不是魚？</text></g>''')


def fish_tools():
    return svg(f'''
<g filter="url(#sh)">
<path d="M80 120 Q120 300 140 470" stroke="#6b4a2f" stroke-width="10" fill="none" stroke-linecap="round"/>
<path d="M80 120 Q60 200 70 300" stroke="#444" stroke-width="1.5" fill="none"/>
<g transform="translate(250 160)"><path d="M0 0 L-70 200 L70 200 Z" fill="none" stroke="#7a6a4a" stroke-width="4"/>
{''.join(f'<line x1="{-70+i*14}" y1="200" x2="0" y2="0" stroke="#7a6a4a" stroke-width="1.5"/>' for i in range(11))}
{''.join(f'<path d="M{-70*k/6} {200*k/6} L{70*k/6} {200*k/6}" stroke="#7a6a4a" stroke-width="1.5"/>' for k in range(1,7))}</g>
<g transform="translate(410 330)"><path d="M-55 0 Q-60 110 0 125 Q60 110 55 0 Z" fill="url(#bamboo)"/>
{''.join(f'<path d="M-56 {y} Q0 {y+10} 56 {y}" stroke="#8f6435" stroke-width="3" fill="none"/>' for y in range(14, 120, 18))}
<ellipse rx="55" ry="14" fill="#a87d47"/><ellipse rx="40" ry="9" fill="#5a3b22"/></g>
<g transform="translate(560 160)"><path d="M-80 60 L0 0 L80 60 Z" fill="#b39b62"/><path d="M-80 60 L80 60" stroke="#7d6a3a" stroke-width="4"/>
<path d="M-60 90 Q-70 260 -40 320 L40 320 Q70 260 60 90 Z" fill="#9d8a55"/>
{''.join(f'<path d="M{x} 92 L{x+4} 320" stroke="#7d6a3a" stroke-width="2"/>' for x in range(-56, 60, 10))}</g>
</g>
<g font-family="Noto Sans CJK TC" font-size="24" font-weight="700" fill="#4a3220" text-anchor="middle">
<text x="110" y="520">釣竿</text><text x="250" y="400">漁網</text><text x="410" y="500">魚簍</text><text x="560" y="520">斗笠・蓑衣</text></g>''')


def fish_title():
    return '''<div class="title-plate" style="color:#2d3a3a">
<div class="t-kicker" style="color:#8a3324">特別展覽・2F S203</div>
<div class="t-main" style="font-family:'Noto Serif CJK TC';font-weight:900">漁樂圖</div>
<div class="t-sub">知漁之樂特展</div>
<div class="t-date">2026.11.11 – 2027.02.14</div></div>'''


def fish_egg():
    return svg('''
<g filter="url(#sh)"><rect x="200" y="60" width="300" height="420" fill="#c0392b" rx="6"/>
<rect x="216" y="76" width="268" height="388" fill="none" stroke="#f2c14e" stroke-width="4"/></g>
<g transform="translate(350 210)"><path d="M-80 0 Q0 -50 80 0 Q0 50 -80 0 Z" fill="#f2c14e"/><path d="M80 0 L124 -34 L124 34 Z" fill="#f2c14e"/><circle cx="-46" cy="-8" r="8" fill="#7a1d12"/>
<path d="M-20 -20 q10 20 0 40 M10 -24 q10 24 0 48" stroke="#c0392b" stroke-width="4" fill="none"/></g>
<text x="350" y="380" text-anchor="middle" font-family="Noto Serif CJK TC" font-weight="900" font-size="64" fill="#f2c14e">年年有魚</text>''')


# ================================================================ 3. CALLIGRAPHY
def screen(x, y, w, h, inner):
    return f'''<g filter="url(#sh)"><rect x="{x-14}" y="{y-14}" width="{w+28}" height="{h+28}" rx="14" fill="#1b1f24"/>
<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="url(#screen)"/>{inner}</svg></g>'''


def cal_copy():
    inner = '<rect x="30" y="30" width="200" height="260" fill="#f4ead2"/><text x="130" y="200" font-family="Noto Serif CJK TC" font-size="170" font-weight="900" text-anchor="middle" fill="#1a1a1a">永</text>'
    inner += '<rect x="290" y="30" width="200" height="260" fill="#f4ead2"/><text x="390" y="200" font-family="Noto Serif CJK TC" font-size="170" font-weight="900" text-anchor="middle" fill="#1a1a1a" opacity=".18">永</text>'
    inner += '<path d="M350 90 L392 82 M380 120 L410 115 L398 150" stroke="#111" stroke-width="16" stroke-linecap="round" fill="none"/>'
    inner += '<g font-family="Noto Sans CJK TC" font-size="20" fill="#9fd3ff"><text x="130" y="320" text-anchor="middle">名家字帖</text><text x="390" y="320" text-anchor="middle">換你寫寫看</text></g>'
    return svg(screen(90, 60, 520, 340, inner) + '''
<g transform="translate(470 470) rotate(-35)"><rect x="-10" y="-140" width="20" height="150" rx="8" fill="#e8e8e8"/><rect x="-10" y="-140" width="20" height="30" rx="8" fill="#2d7dd2"/><path d="M-10 10 L0 40 L10 10 Z" fill="#222"/></g>
<rect x="160" y="440" width="380" height="60" rx="10" fill="#2b3036"/>
<text x="300" y="480" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="700" font-size="24" fill="#fff">王羲之・懷素・蘇軾・黃庭堅</text>''')


def cal_linmo():
    left = '''<rect x="40" y="90" width="120" height="160" fill="#f4ead2" stroke="#999"/><text x="100" y="205" font-family="Noto Serif CJK TC" font-size="110" font-weight="900" text-anchor="middle">書</text>
<rect x="180" y="90" width="120" height="160" fill="#fffdf6" stroke="#999"/><text x="240" y="205" font-family="Noto Serif CJK TC" font-size="110" font-weight="700" text-anchor="middle" fill="#333">書</text>
<path d="M150 170 L180 170" stroke="#c0392b" stroke-width="4" marker-end="url(#ar)"/>'''
    right = '''<rect x="40" y="90" width="150" height="190" fill="#f4ead2" stroke="#999"/><text x="115" y="225" font-family="Noto Serif CJK TC" font-size="130" font-weight="900" text-anchor="middle">書</text>
<rect x="60" y="70" width="150" height="190" fill="#ffffff" opacity=".6" stroke="#5aa0d8" stroke-width="2"/>
<text x="135" y="205" font-family="Noto Serif CJK TC" font-size="130" font-weight="900" text-anchor="middle" fill="none" stroke="#c0392b" stroke-width="3" stroke-dasharray="6 5">書</text>'''
    return svg(f'''
<g filter="url(#sh)"><rect x="20" y="40" width="320" height="420" rx="14" fill="#fff8e8"/><rect x="360" y="40" width="320" height="420" rx="14" fill="#eef6ff"/></g>
<svg x="20" y="40" width="320" height="420" viewBox="0 0 320 420">{left}<text x="160" y="330" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="900" font-size="72" fill="#c0392b">臨</text><text x="160" y="385" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="24" fill="#555">看著字帖寫</text></svg>
<svg x="360" y="40" width="320" height="420" viewBox="0 0 320 420">{right}<text x="160" y="345" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="900" font-size="72" fill="#1f618d">摹</text><text x="160" y="395" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="24" fill="#555">蓋上薄紙描</text></svg>''')


def cal_tiger():
    chars = '天地玄黃宇宙洪荒日月盈昃'
    stele = ''.join(f'<text x="{90+ (i//4)*50}" y="{170+(i%4)*52}" font-family="Noto Serif CJK TC" font-size="40" font-weight="700" fill="#5d564c" text-anchor="middle">{c}</text>' for i, c in enumerate(chars))
    rub = ''.join(f'<text x="{430+ (i//4)*50}" y="{170+(i%4)*52}" font-family="Noto Serif CJK TC" font-size="40" font-weight="700" fill="#f0ece2" text-anchor="middle">{c}</text>' for i, c in enumerate(chars))
    return svg(f'''
<g filter="url(#sh)"><path d="M50 110 Q50 70 90 70 L230 70 Q270 70 270 110 L270 400 L50 400 Z" fill="url(#stone)"/><rect x="30" y="400" width="260" height="70" rx="6" fill="#6e675c"/></g>
<path d="M70 110 L250 110" stroke="#6e675c" stroke-width="3"/>{stele}
<g filter="url(#sh)"><rect x="380" y="90" width="210" height="320" fill="#141414"/></g>{rub}
<g transform="translate(560 450)"><circle r="56" fill="#f39c12"/><path d="M-40 -40 l14 26 l-28 0z M40 -40 l-14 26 l28 0z" fill="#f39c12"/>
<path d="M-30 -8 l12 4 M30 -8 l-12 4 M-20 -30 l6 12 M0 -36 l0 14 M20 -30 l-6 12" stroke="#2a1a0a" stroke-width="5" stroke-linecap="round"/><circle cx="-18" cy="0" r="6" fill="#222"/><circle cx="18" cy="0" r="6" fill="#222"/><path d="M-10 22 q10 10 20 0" stroke="#222" stroke-width="4" fill="none"/></g>
<text x="210" y="525" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="26" font-weight="700" fill="#e8e2d4">石碑 ➜ 拓片「黑老虎」</text>''')


def cal_qianwen():
    import random
    rnd = random.Random(8)
    stars = ''.join(f'<circle cx="{rnd.uniform(0,640):.0f}" cy="{rnd.uniform(0,460):.0f}" r="{rnd.uniform(.8,2.4):.1f}" fill="#fff" opacity="{rnd.uniform(.4,1):.2f}"/>' for _ in range(160))
    chars = '天地玄黃宇宙洪荒日月盈昃辰宿列張寒來暑往秋收冬藏'
    cs = ''
    for i, c in enumerate(chars):
        x = 60 + (i % 8) * 75 + rnd.uniform(-10, 10); y = 110 + (i // 8) * 120 + rnd.uniform(-14, 14)
        cs += f'<text x="{x:.0f}" y="{y:.0f}" font-family="Noto Serif CJK TC" font-size="{rnd.choice([40,48,56])}" font-weight="{rnd.choice([300,700,900])}" fill="#e8f4ff" text-anchor="middle" filter="url(#glow)">{c}</text>'
    return svg(f'''<g filter="url(#sh)"><rect x="20" y="30" width="660" height="490" rx="20" fill="#05070f"/></g>
<svg x="30" y="40" width="640" height="460" viewBox="0 0 640 460"><rect width="640" height="460" fill="#0a1030"/>
<circle cx="520" cy="90" r="160" fill="#3a2a7a" opacity=".35"/><circle cx="120" cy="380" r="180" fill="#1a5a7a" opacity=".3"/>{stars}{cs}</svg>''')


def cal_scripts():
    cards = [('篆', '圓轉古老', '#8e44ad'), ('隸', '蠶頭燕尾', '#c0392b'), ('楷', '端正工整', '#1f618d'), ('草', '快速連綿', '#117a65')]
    out = ''
    for i, (c, d, col) in enumerate(cards):
        x = 40 + i * 160
        out += f'<g filter="url(#sh)"><rect x="{x}" y="90" width="140" height="330" rx="12" fill="#fbf6ea"/></g>'
        out += f'<rect x="{x}" y="90" width="140" height="16" rx="6" fill="{col}"/>'
        out += f'<text x="{x+70}" y="260" text-anchor="middle" font-family="Noto Serif CJK TC" font-weight="900" font-size="110" fill="#1a1a1a">{c}</text>'
        out += f'<text x="{x+70}" y="320" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="700" font-size="30" fill="{col}">{c}書</text>'
        out += f'<text x="{x+70}" y="380" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="24" fill="#555">{d}</text>'
    out += '<path d="M60 470 L640 470" stroke="#b8a982" stroke-width="5"/><path d="M630 456 L660 470 L630 484 Z" fill="#b8a982"/>'
    out += '<text x="350" y="520" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="24" font-weight="700" fill="#e8e2d4">書體大不同</text>'
    return svg(out)


def cal_jiucheng():
    chars = '九成宮醴泉銘'
    st = ''.join(f'<text x="{340}" y="{120+i*58}" font-family="Noto Serif CJK TC" font-size="50" font-weight="700" fill="#1a1a1a" text-anchor="middle">{c}</text>' for i, c in enumerate(chars))
    inner = f'<rect width="460" height="420" fill="#efe6d0"/><rect x="250" y="40" width="180" height="370" fill="#f8f3e6" stroke="#b39b62"/>{st}'
    inner += '<g transform="translate(120 230)"><circle r="70" fill="none" stroke="#2d7dd2" stroke-width="4" stroke-dasharray="8 6"/><text y="35" text-anchor="middle" font-family="Noto Serif CJK TC" font-size="110" font-weight="900" fill="#c0392b">泉</text></g>'
    inner += '<g transform="translate(180 330)"><path d="M0 0 q10 -40 30 -50 q12 -4 12 10 l-6 34 l24 4 q12 4 10 18 l-8 40 l-50 0 z" fill="#f2d2b0" stroke="#b07a50" stroke-width="2"/></g>'
    return svg(screen(110, 60, 460, 420, inner) + '<text x="340" y="530" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="700" font-size="26" fill="#e8e2d4">觸控螢幕・歐陽詢楷書</text>')


def cal_title():
    return '''<div class="title-plate" style="color:#f1f6ff">
<div class="t-kicker" style="color:#6cc4ff">常設展・2F S204</div>
<div class="t-main" style="font-family:'Noto Serif CJK TC';font-weight:900">揮翰學書</div>
<div class="t-sub">書法跨域新媒體展</div>
<div class="t-date">e 筆臨摹・拓碑・千文宇宙</div></div>'''


def cal_egg():
    pieces = [('M0 0 L60 0', 0, 0), ('M0 0 L0 120', 60, 40), ('M0 0 Q-30 60 -70 90', 160, 60), ('M0 0 Q30 60 80 90', 240, 80), ('M0 0 L20 20', 340, 30)]
    out = ''
    for i, (d, x, y) in enumerate(pieces):
        bx = 150 + (i % 3) * 150; by = 140 + (i // 3) * 180
        out += f'<g filter="url(#sh)"><rect x="{bx-60}" y="{by-60}" width="130" height="150" rx="16" fill="{["#f9e79f","#aed6f1","#f5b7b1","#a9dfbf","#d7bde2"][i]}"/></g>'
        out += f'<path transform="translate({bx-10} {by-20})" d="{d}" stroke="#1a1a1a" stroke-width="16" stroke-linecap="round" fill="none"/>'
    out += '<text x="560" y="420" text-anchor="middle" font-family="Noto Serif CJK TC" font-size="120" font-weight="900" fill="#1a1a1a" opacity=".85">木</text>'
    return svg(out)


# ================================================================ 4. TEA
def tea_tang():
    return svg(f'''
<g filter="url(#sh)">
<g transform="translate(150 300)"><path d="M-70 -40 L70 -40 L60 60 L-60 60 Z" fill="#5a3b22"/><path d="M-90 -50 Q0 -90 90 -50 L70 -40 L-70 -40 Z" fill="#3a2a20"/>
<path d="M-30 60 L-36 110 M30 60 L36 110 M0 60 L0 110" stroke="#3a2a20" stroke-width="10"/>
<path d="M-40 10 q10 -20 20 0 t20 0 t20 0" stroke="#f39c12" stroke-width="6" fill="none"/>
<path d="M-20 -90 q10 -20 0 -40 M10 -95 q10 -20 0 -40" stroke="#ccc" stroke-width="4" fill="none" opacity=".7"/></g>
<g transform="translate(360 330)"><circle r="70" fill="#5a4630"/><circle r="56" fill="#6b5236"/><circle r="10" fill="#3a2a20"/>
<path d="M-50 -20 L50 20" stroke="#3a2a20" stroke-width="4"/><text y="110" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="22" font-weight="700" fill="#4a3220">茶餅</text></g>
<g transform="translate(540 300)"><path d="M-55 -60 Q-75 40 -40 100 L40 100 Q75 40 55 -60 Z" fill="url(#celadon)"/>
<ellipse cy="-60" rx="55" ry="14" fill="#9fb985"/><path d="M-58 -10 Q-110 -30 -100 -90" stroke="url(#celadon)" stroke-width="14" fill="none"/>
<path d="M55 -20 Q90 -10 100 20 Q90 50 55 50" stroke="url(#celadon)" stroke-width="14" fill="none"/>
<path d="M-30 20 q15 -20 30 0 t30 0" stroke="#55703f" stroke-width="4" fill="none"/></g>
</g>
<g font-family="Noto Sans CJK TC" font-size="22" font-weight="700" fill="#4a3220" text-anchor="middle"><text x="150" y="450">風爐與茶鍑</text><text x="540" y="450">長沙窯青釉單柄壺</text></g>
<text x="350" y="120" text-anchor="middle" font-family="Noto Serif CJK TC" font-weight="900" font-size="54" fill="#5a3b22">《茶經》</text>''')


def tea_song():
    return svg(f'''
<g filter="url(#sh)">
<g transform="translate(300 300)"><path d="M-150 -40 Q-140 100 -40 130 L40 130 Q140 100 150 -40 Z" fill="url(#black)"/>
<ellipse cy="-40" rx="150" ry="40" fill="#2a1a12"/><ellipse cy="-40" rx="128" ry="30" fill="url(#foam)"/>
<path d="M-120 -10 Q-100 60 -60 100" stroke="#8a6a50" stroke-width="2" opacity=".6" fill="none"/><path d="M-90 0 Q-80 50 -40 100" stroke="#a07a55" stroke-width="2" opacity=".5" fill="none"/>
<path d="M-30 130 L-40 160 L40 160 L30 130 Z" fill="#3a2a20"/></g>
<g transform="translate(560 260) rotate(15)"><rect x="-14" y="-150" width="28" height="110" rx="8" fill="url(#bamboo)"/>
{''.join(f'<path d="M0 -40 Q{dx} 30 {dx*1.3} 80" stroke="#d9b98a" stroke-width="3" fill="none"/>' for dx in range(-40, 44, 8))}</g>
</g>
<g font-family="Noto Sans CJK TC" font-size="24" font-weight="700" fill="#4a3220" text-anchor="middle"><text x="300" y="510">黑釉建盞＋白色茶沫</text><text x="580" y="440">茶筅</text></g>''')


def tea_ming():
    return svg(f'''
<rect x="60" y="50" width="580" height="300" fill="#d9c49a" opacity=".5"/>
<path d="M60 50 L350 10 L640 50" fill="none" stroke="#6b4a2f" stroke-width="8"/>
<rect x="100" y="80" width="140" height="200" fill="#efe3c4" stroke="#6b4a2f" stroke-width="4"/>
{ink_mountains(140, 200, 120, 2, 4).replace('<path', '<path transform="translate(100 80)"')}
<g transform="translate(470 150)"><rect x="-30" y="-60" width="60" height="80" rx="20" fill="#f7d77a" opacity=".85"/><path d="M-30 -60 L30 -60 M-30 20 L30 20" stroke="#8a2a1a" stroke-width="6"/><line x1="0" y1="-60" x2="0" y2="-90" stroke="#3a2a20" stroke-width="3"/></g>
<rect x="80" y="380" width="540" height="24" fill="#6b4a2f" filter="url(#sh)"/><rect x="110" y="404" width="20" height="100" fill="#5a3b22"/><rect x="570" y="404" width="20" height="100" fill="#5a3b22"/>
<g filter="url(#sh)"><g transform="translate(260 330)"><ellipse cy="40" rx="80" ry="12" fill="#3a1d12"/><path d="M-70 0 Q-80 50 0 52 Q80 50 70 0 Q60 -30 0 -32 Q-60 -30 -70 0 Z" fill="url(#clay)"/>
<path d="M70 0 Q110 -10 120 -40" stroke="url(#clay)" stroke-width="14" fill="none"/><path d="M-70 -6 Q-110 0 -96 30 Q-86 44 -66 28" stroke="url(#clay)" stroke-width="12" fill="none"/>
<ellipse cy="-32" rx="34" ry="8" fill="#6a3322"/><circle cy="-44" r="9" fill="url(#clay)"/></g>
{''.join(f'<g transform="translate({x} 360)"><path d="M-26 -18 Q-24 18 0 20 Q24 18 26 -18 Z" fill="url(#porc)"/><ellipse cy="-18" rx="26" ry="6" fill="#f6f1df"/><ellipse cy="-18" rx="20" ry="4" fill="#e6d9a6"/></g>' for x in (420, 490, 560))}</g>
<g font-family="Noto Sans CJK TC" font-size="22" font-weight="700" fill="#4a3220" text-anchor="middle"><text x="260" y="540">紫砂壺泡散茶</text><text x="490" y="540">白瓷杯看茶色</text></g>''')


def tea_japan():
    return svg(f'''
<rect x="40" y="40" width="620" height="460" fill="#efe4c8" filter="url(#sh)"/>
<rect x="40" y="340" width="620" height="160" fill="#c9c08a"/>
{''.join(f'<rect x="{40+i*155}" y="340" width="155" height="160" fill="none" stroke="#7d7442" stroke-width="3"/>' for i in range(4))}
<rect x="60" y="60" width="240" height="280" fill="#d8ccb0" stroke="#5a3b22" stroke-width="6"/>
<rect x="140" y="80" width="80" height="210" fill="#f3ead5" stroke="#8b6d43" stroke-width="2"/>
<text x="180" y="190" text-anchor="middle" font-family="Noto Serif CJK TC" font-size="40" font-weight="900" fill="#333" writing-mode="tb">一期一會</text>
<g transform="translate(180 320)"><path d="M-20 0 Q-30 -40 0 -60 Q30 -40 20 0 Z" fill="#8a9a5a"/><path d="M0 -60 q20 -30 10 -60 M0 -60 q-24 -20 -30 -50" stroke="#5a6a3a" stroke-width="3" fill="none"/></g>
<rect x="320" y="60" width="320" height="280" fill="#f6efdc" stroke="#5a3b22" stroke-width="6"/>
{''.join(f'<line x1="{320+i*40}" y1="60" x2="{320+i*40}" y2="340" stroke="#5a3b22" stroke-width="2"/>' for i in range(1,8))}
{''.join(f'<line x1="320" y1="{60+i*40}" x2="640" y2="{60+i*40}" stroke="#5a3b22" stroke-width="2"/>' for i in range(1,7))}
<g filter="url(#sh)"><g transform="translate(400 420)"><path d="M-70 -30 Q-66 40 0 44 Q66 40 70 -30 Z" fill="#c8b9a0"/><path d="M-66 -10 Q0 10 66 -10" stroke="#8a7a62" stroke-width="3" fill="none"/>
<ellipse cy="-30" rx="70" ry="16" fill="#e8dcc6"/><ellipse cy="-30" rx="56" ry="11" fill="#6aa04a"/></g>
<g transform="translate(540 430)"><rect x="-10" y="-60" width="20" height="40" fill="url(#bamboo)"/>{''.join(f'<path d="M0 -20 Q{dx} 10 {dx} 40" stroke="#e1c28d" stroke-width="3" fill="none"/>' for dx in range(-24, 28, 6))}</g></g>''')


def tea_mongol():
    return svg(f'''
<g filter="url(#sh)">
<g transform="translate(220 300)"><rect x="-60" y="-170" width="120" height="300" rx="20" fill="url(#gold)"/>
<path d="M-60 -170 Q0 -230 60 -170" fill="url(#gold)"/><path d="M40 -190 Q90 -220 110 -180 L60 -160" fill="url(#gold)"/>
{''.join(f'<rect x="-62" y="{y}" width="124" height="14" fill="#2a6f8f"/>' for y in (-130, -40, 50))}
{''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="{c}"/>' for x, y, c in [(-30,-123,"#c0392b"),(0,-123,"#1f9e8a"),(30,-123,"#c0392b"),(-30,-33,"#1f9e8a"),(0,-33,"#c0392b"),(30,-33,"#1f9e8a")])}
<path d="M60 -60 Q110 -40 110 20 Q110 60 60 70" stroke="url(#gold)" stroke-width="14" fill="none"/>
<path d="M-60 -110 Q-110 -120 -130 -170" stroke="url(#gold)" stroke-width="12" fill="none"/></g>
<g transform="translate(490 330)"><path d="M-60 -60 Q-80 60 0 80 Q80 60 60 -60 Z" fill="url(#porc)"/>
<path d="M-60 -60 Q-30 -110 0 -90 Q30 -130 70 -100 L60 -60 Z" fill="#e8ecef" stroke="#9aa5ab" stroke-width="2"/>
<path d="M-62 -70 Q-110 -110 -120 -150" stroke="#cfd6db" stroke-width="10" fill="none"/>
<path d="M-40 0 q20 -24 40 0 t40 0" stroke="#2a5d8f" stroke-width="5" fill="none"/></g>
</g>
<g font-family="Noto Sans CJK TC" font-size="22" font-weight="700" fill="#4a3220" text-anchor="middle"><text x="220" y="470">奶茶壺</text><text x="490" y="470">僧帽壺</text></g>
<g transform="translate(360 510)"><ellipse rx="44" ry="12" fill="#f6efe2" stroke="#c9b48a" stroke-width="3"/></g>''')


def tea_taiwan():
    return svg(f'''
<rect x="60" y="390" width="580" height="30" fill="#6b4a2f" filter="url(#sh)"/>
<g filter="url(#sh)">
<g transform="translate(140 340)"><path d="M-40 50 L-50 -40 L50 -40 L40 50 Z" fill="#b3542e"/><rect x="-20" y="0" width="40" height="30" fill="#2a1a12"/><path d="M-12 20 q6 -14 12 0 t12 0" stroke="#f39c12" stroke-width="4" fill="none"/>
<g transform="translate(0 -70)"><ellipse rx="44" ry="34" fill="#c56a3a"/><path d="M40 -6 Q64 -10 70 -30" stroke="#c56a3a" stroke-width="10" fill="none"/><path d="M-20 -30 Q0 -60 20 -30" stroke="#5a3b22" stroke-width="5" fill="none"/></g></g>
<g transform="translate(330 360)"><path d="M-46 0 Q-52 30 0 32 Q52 30 46 0 Q40 -22 0 -24 Q-40 -22 -46 0 Z" fill="url(#clay)"/><path d="M46 0 Q72 -6 78 -26" stroke="url(#clay)" stroke-width="10" fill="none"/>
<path d="M-46 -2 Q-74 2 -64 22 Q-56 30 -44 20" stroke="url(#clay)" stroke-width="9" fill="none"/><ellipse cy="-24" rx="22" ry="5" fill="#6a3322"/><circle cy="-32" r="6" fill="url(#clay)"/></g>
{''.join(f'<g transform="translate({x} 376)"><path d="M-16 -12 Q-14 12 0 13 Q14 12 16 -12 Z" fill="url(#porc)"/><ellipse cy="-12" rx="16" ry="4" fill="#f6f1df"/><ellipse cy="-12" rx="12" ry="3" fill="#c98a3a"/></g>' for x in (450, 500, 550, 600))}
</g>
<g font-family="Noto Sans CJK TC" font-size="22" font-weight="700" fill="#4a3220" text-anchor="middle">
<text x="140" y="460">潮汕烘爐＋玉書煨</text><text x="330" y="460">孟臣壺</text><text x="525" y="460">若深杯</text></g>
<text x="350" y="130" text-anchor="middle" font-family="Noto Serif CJK TC" font-weight="900" font-size="56" fill="#5a3b22">潮汕四寶</text>''')


def tea_title():
    return '''<div class="title-plate" style="color:#3b2a1c">
<div class="t-kicker" style="color:#8a3324">常設展・2F S202</div>
<div class="t-main" style="font-family:'Noto Serif CJK TC';font-weight:900">東亞茶文化</div>
<div class="t-sub">煎茶・點茶・泡茶・茶道</div>
<div class="t-date">中國・日本・蒙藏・臺灣</div></div>'''


def tea_egg():
    return svg('''
<g filter="url(#sh)"><path d="M290 140 L410 140 Q410 260 350 280 Q290 260 290 140 Z" fill="url(#gold)"/>
<path d="M290 160 Q240 160 240 200 Q240 240 300 240" stroke="url(#gold)" stroke-width="14" fill="none"/><path d="M410 160 Q460 160 460 200 Q460 240 400 240" stroke="url(#gold)" stroke-width="14" fill="none"/>
<rect x="330" y="280" width="40" height="60" fill="url(#gold)"/><rect x="290" y="340" width="120" height="30" rx="6" fill="#5a3b22"/></g>
<g transform="translate(180 420)"><path d="M-70 -20 Q-60 40 0 44 Q60 40 70 -20 Z" fill="url(#black)"/><ellipse cy="-20" rx="70" ry="16" fill="#2a1a12"/><ellipse cy="-20" rx="60" ry="12" fill="url(#foam)"/></g>
<g transform="translate(520 420)"><path d="M-70 -20 Q-60 40 0 44 Q60 40 70 -20 Z" fill="url(#black)"/><ellipse cy="-20" rx="70" ry="16" fill="#2a1a12"/><ellipse cy="-20" rx="60" ry="12" fill="#c9b37a"/><ellipse cx="20" cy="-20" rx="24" ry="5" fill="#a08850"/></g>
<text x="350" y="110" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="900" font-size="44" fill="#8a3324">鬥茶 VS</text>''')


# ================================================================ 5. TIANTUAN
def tt_eight():
    figs = ''.join(figure(150 + i * 58, 300 - (i % 2) * 18, 0.55, robe=['#c0392b', '#1f618d', '#117a65', '#7d3c98', '#b9770e', '#922b21', '#2e4053', '#a04000'][i], face='#f8ecd4') for i in range(8))
    return svg(f'''
<g filter="url(#sh)"><path d="M90 140 Q350 90 610 140 L610 420 Q350 380 90 420 Z" fill="url(#ivory)"/>
<path d="M110 160 Q350 115 590 160 L590 400 Q350 362 110 400 Z" fill="#efe0bd"/></g>
<path d="M110 330 q30 -20 60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 L590 400 Q350 362 110 400 Z" fill="#d6c095"/>
<path d="M110 350 q30 -20 60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0" stroke="#b39b62" stroke-width="3" fill="none"/>
{figs.replace('fill="#f8ecd4"', 'fill="#fff6e3"')}
<g opacity=".55">{figs}</g>
<path d="M140 190 q40 -30 80 0 M480 180 q40 -30 80 0" stroke="#b39b62" stroke-width="4" fill="none"/>
<text x="350" y="490" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="26" font-weight="700" fill="#4a3220">象牙臂擱・八仙渡海</text>''')


def tt_three():
    return svg(f'''
<g filter="url(#sh)"><path d="M140 240 L560 240 L600 300 L100 300 Z" fill="url(#lacq)"/>
<rect x="120" y="300" width="460" height="170" fill="url(#lacq)"/>
<path d="M150 250 L550 250 L580 292 L120 292 Z" fill="#c1332a"/></g>
{''.join(f'<path d="M{130+i*18} 300 l0 170" stroke="#8a1810" stroke-width="2" opacity=".4"/>' for i in range(26))}
<g transform="translate(350 270) scale(.9 .35)"><circle r="44" fill="#fff4e6" stroke="#7d1410" stroke-width="5"/><path d="M0 -44 a22 22 0 0 1 0 44 a22 22 0 0 0 0 44 a44 44 0 0 1 0 -88" fill="#7d1410"/></g>
{figure(250, 288, 0.55, robe='#7d1410', face='#f3d6b9', hat='#5a0f0a')}{figure(450, 288, 0.55, robe='#7d1410', face='#f3d6b9', hat='#5a0f0a')}
<g transform="translate(540 288) scale(.55)"><path d="M-22 0 L-16 -60 L16 -60 L22 0 Z" fill="#7d1410"/><ellipse cx="0" cy="-82" rx="16" ry="24" fill="#f3d6b9"/><path d="M-5 -78 a1.6 1.6 0 1 0 .1 0 M5 -78 a1.6 1.6 0 1 0 .1 0" fill="#3a2a20"/><path d="M-6 -66 Q0 -50 6 -66" fill="#fff"/></g>
<g font-family="Noto Sans CJK TC" font-weight="900" font-size="30" fill="#7d1410" text-anchor="middle"><text x="250" y="400">福</text><text x="350" y="400">祿</text><text x="450" y="400">壽</text></g>
<text x="350" y="530" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="26" font-weight="700" fill="#4a3220">剔紅方盒・三星看太極圖</text>''')


def tt_hehe():
    return svg(f'''
<ellipse cx="350" cy="480" rx="200" ry="24" fill="#000" opacity=".3"/>
<g filter="url(#sh)"><path d="M160 470 Q140 390 200 350 Q260 320 330 360 Q420 300 500 350 Q570 400 540 470 Z" fill="url(#bamboo)"/>
{''.join(f'<path d="M{x} 470 q-10 -30 0 -60" stroke="#8f6435" stroke-width="3" fill="none"/>' for x in range(190, 540, 40))}
<g transform="translate(270 360)"><path d="M-50 0 Q-60 -80 -30 -110 L30 -110 Q60 -80 50 0 Z" fill="url(#bamboo)"/><circle cy="-140" r="38" fill="url(#bamboo)"/>
<path d="M-16 -146 q8 -8 16 0 M4 -146 q8 -8 16 0" stroke="#5a3b22" stroke-width="4" fill="none"/><path d="M-16 -124 Q0 -108 16 -124" stroke="#5a3b22" stroke-width="5" fill="none"/></g>
<g transform="translate(430 330)"><path d="M-40 20 L-34 -130 L34 -130 L40 20 Z" fill="url(#bamboo)"/><circle cy="-160" r="36" fill="url(#bamboo)"/>
<path d="M-16 -166 q8 -8 16 0 M4 -166 q8 -8 16 0" stroke="#5a3b22" stroke-width="4" fill="none"/><path d="M-16 -144 Q0 -128 16 -144" stroke="#5a3b22" stroke-width="5" fill="none"/>
<path d="M30 -100 L80 -170" stroke="#8f6435" stroke-width="10" stroke-linecap="round"/><path d="M70 -180 q20 -10 30 10 q-20 10 -30 -10" fill="#c3955a"/></g></g>
<text x="350" y="530" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="26" font-weight="700" fill="#4a3220">竹根雕・寒山與拾得相視而笑</text>''')


def tt_arhat():
    heads = ''.join(f'<circle cx="{300+ (i%4)*34}" cy="{300+(i//4)*40}" r="13" fill="#f3d6b9" stroke="#8a5a2a" stroke-width="2"/>' for i in range(12))
    return svg(f'''
<ellipse cx="350" cy="510" rx="130" ry="20" fill="#000" opacity=".3"/>
<g filter="url(#sh)"><path d="M330 70 L370 70 L372 200 Q500 230 500 350 Q500 490 350 500 Q200 490 200 350 Q200 230 328 200 Z" fill="url(#porc)"/>
<ellipse cx="350" cy="70" rx="26" ry="8" fill="#e8ecef"/>
<path d="M340 90 L340 190 M360 90 L360 190" stroke="#d4a017" stroke-width="3"/>
<ellipse cx="350" cy="350" rx="110" ry="110" fill="#fff8e8" stroke="#d4a017" stroke-width="6"/>
{''.join(f'<path d="M{x} 240 q10 -14 20 0" stroke="#c0392b" stroke-width="5" fill="none"/>' for x in range(230, 470, 30))}
{''.join(f'<path d="M{x} 470 q10 14 20 0" stroke="#2a5d8f" stroke-width="5" fill="none"/>' for x in range(240, 460, 30))}</g>
<g transform="translate(-5 0)">{heads}</g>
{''.join(f'<path d="M{290+(i%4)*34} {318+(i//4)*40} l20 0 l4 16 l-28 0z" fill="{["#c0392b","#2a5d8f","#117a65","#b9770e"][i%4]}"/>' for i in range(12))}
<text x="350" y="430" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="20" font-weight="700" fill="#8a5a2a">十八羅漢</text>''')


def tt_seven():
    import math
    petals = ''
    for k in range(7):
        a = math.pi + k * math.pi / 6
        x = 350 + math.cos(a) * 170; y = 330 + math.sin(a) * 60
        petals += f'<ellipse cx="{x:.0f}" cy="{y+60:.0f}" rx="44" ry="72" transform="rotate({(k-3)*14} {x:.0f} {y+60:.0f})" fill="url(#jade)" stroke="#6f9a72" stroke-width="3"/>'
        petals += f'<g transform="translate({x:.0f} {y+50:.0f})"><circle r="12" fill="#86b48a"/><path d="M-12 26 Q0 0 12 26 Z" fill="#86b48a"/></g>'
    return svg(f'''
<ellipse cx="350" cy="500" rx="200" ry="22" fill="#000" opacity=".3"/>
<g filter="url(#sh)"><path d="M190 390 Q350 520 510 390 Z" fill="url(#jade)"/>{petals}
<ellipse cx="350" cy="250" rx="170" ry="40" fill="url(#jade)" stroke="#6f9a72" stroke-width="3"/>
<path d="M200 250 Q350 130 500 250" fill="url(#jade)" stroke="#6f9a72" stroke-width="3"/>
<circle cx="350" cy="160" r="22" fill="url(#jade)" stroke="#6f9a72" stroke-width="3"/>
{''.join(f'<circle cx="{260+k*30}" cy="{235 - abs(k-3)*6}" r="9" fill="none" stroke="#6f9a72" stroke-width="3"/>' for k in range(7))}</g>
<text x="350" y="545" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="26" font-weight="700" fill="#4a3220">蓮花玉供碗・過去七佛</text>''')


def tt_wubin():
    inner = '<rect width="440" height="320" fill="url(#silk)"/>'
    inner += '<path d="M0 320 L0 200 Q40 120 20 60 Q70 20 90 80 Q120 30 140 110 Q160 60 170 140 L170 320 Z" fill="#8a8f7a" opacity=".85"/>'
    inner += '<path d="M440 320 L440 180 Q400 110 420 40 Q380 10 360 70 Q330 30 310 120 L300 320 Z" fill="#8a8f7a" opacity=".85"/>'
    inner += '<path d="M30 70 q20 -20 40 0 M380 60 q20 -18 40 0 M60 160 q20 -20 40 0 M340 180 q20 -16 40 0" stroke="#5c604e" stroke-width="4" fill="none"/>'
    inner += '<circle cx="220" cy="150" r="70" fill="url(#halo)"/>'
    inner += '<g transform="translate(220 230)"><path d="M-60 40 Q-60 -40 0 -50 Q60 -40 60 40 Z" fill="#c0392b"/><circle cy="-80" r="28" fill="#f3d6b9"/><path d="M-28 -90 Q0 -130 28 -90" fill="#2a3a5a"/><path d="M-80 40 L80 40 L70 60 L-70 60 Z" fill="#f2c14e"/></g>'
    return svg(f'''<g filter="url(#sh)"><rect x="110" y="90" width="480" height="370" fill="#d8c7a0"/>
<svg x="130" y="115" width="440" height="320" viewBox="0 0 440 320">{inner}</svg>
<rect x="130" y="115" width="440" height="320" fill="none" stroke="#8b6d43" stroke-width="2"/><line x1="350" y1="90" x2="350" y2="460" stroke="#8b6d43" stroke-width="2" opacity=".5"/></g>
<text x="350" y="520" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="26" font-weight="700" fill="#4a3220">吳彬・奇石與佛像冊頁</text>''')


def tt_title():
    return '''<div class="title-plate" style="color:#fff">
<div class="t-kicker" style="color:#ffd76a">人氣國寶展・3F S302</div>
<div class="t-main" style="font-weight:900;text-shadow:0 0 30px rgba(255,120,200,.6)">天團降臨</div>
<div class="t-sub">藝術中的仙佛組合</div>
<div class="t-date">八仙・福祿壽・和合二仙・十八羅漢・過去七佛</div></div>'''


def tt_egg():
    return svg('''
<ellipse cx="350" cy="500" rx="150" ry="20" fill="#000" opacity=".3"/>
<g filter="url(#sh)"><path d="M300 490 Q260 380 280 230 Q300 120 350 80 Q400 120 420 230 Q440 380 400 490 Z" fill="url(#jadeg)"/>
<path d="M300 490 Q230 400 250 280 Q270 330 320 470 Z" fill="#f2f6e6" opacity=".9"/><path d="M400 490 Q470 400 450 280 Q430 330 380 470 Z" fill="#eaf3dc"/>
<path d="M350 100 L350 470" stroke="#bfe0b0" stroke-width="5"/>
<path d="M350 200 L300 160 M350 260 L400 220 M350 320 L300 290" stroke="#bfe0b0" stroke-width="3"/>
<g transform="translate(380 150)"><ellipse rx="16" ry="8" fill="#2f6b3a"/><path d="M-16 0 l-12 -8 M-16 0 l-12 8" stroke="#2f6b3a" stroke-width="3"/></g></g>''')


# ================================================================ 6. BUDDHA
def bd_yakshi():
    return svg(f'''
<g filter="url(#sh)">
<rect x="60" y="80" width="40" height="400" fill="url(#stone)"/><rect x="600" y="80" width="40" height="400" fill="url(#stone)"/>
{''.join(f'<rect x="60" y="{y}" width="580" height="46" rx="20" fill="url(#stone)"/>' for y in (130, 260, 390))}
{''.join(f'<g transform="translate({x} {y})"><circle r="40" fill="#a59d8f" stroke="#7a7266" stroke-width="3"/>' + ''.join(f'<ellipse rx="10" ry="30" transform="rotate({k*45})" fill="#c4bcae"/>' for k in range(8)) + '<circle r="10" fill="#7a7266"/></g>' for x, y in [(180,153),(520,153),(180,413),(520,413)])}
<g transform="translate(350 360)"><path d="M-60 -200 Q-90 -260 -40 -280 Q0 -300 30 -260" stroke="#7a7266" stroke-width="14" fill="none"/>
<path d="M-40 -280 q-30 -10 -50 10 M30 -260 q30 -20 50 0 M0 -290 q0 -30 20 -40" stroke="#8f877a" stroke-width="10" fill="none"/>
<circle cx="-10" cy="-150" r="30" fill="#b9b2a5"/><path d="M-30 -120 Q-50 -40 -40 40 L40 40 Q50 -40 20 -120 Z" fill="#b0a898"/>
<path d="M-36 -110 Q-70 -160 -60 -200" stroke="#b0a898" stroke-width="14" fill="none" stroke-linecap="round"/>
<path d="M-22 -150 q6 6 12 0 M2 -150 q6 6 12 0" stroke="#5a5348" stroke-width="3" fill="none"/><path d="M-20 -136 Q-8 -126 4 -136" stroke="#5a5348" stroke-width="3" fill="none"/>
<path d="M-40 -60 Q0 -40 40 -60 M-40 0 Q0 20 40 0" stroke="#8f877a" stroke-width="5" fill="none"/></g>
</g>
<text x="350" y="530" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="26" font-weight="700" fill="#f1e6d0">佛塔欄楯・蓮花與藥叉女</text>''')


def bd_birth():
    return svg(f'''
<ellipse cx="350" cy="490" rx="160" ry="22" fill="#000" opacity=".35"/>
<g filter="url(#sh)">
<g transform="translate(350 470)">{''.join(f'<ellipse cx="{dx}" cy="-10" rx="40" ry="16" transform="rotate({dx/6} {dx} -10)" fill="url(#bronze)"/>' for dx in (-100,-50,0,50,100))}
{''.join(f'<path d="M{dx} -10 Q{dx-26} -60 {dx} -70 Q{dx+26} -60 {dx} -10" fill="url(#gold)"/>' for dx in (-80,-40,0,40,80))}</g>
<g transform="translate(350 400)"><path d="M-55 0 Q-70 -110 -40 -150 L40 -150 Q70 -110 55 0 Z" fill="url(#gold)"/>
<path d="M-40 -110 Q0 -80 40 -110 L36 -70 Q0 -50 -36 -70 Z" fill="#c0392b" opacity=".85"/>
<circle cy="-190" r="46" fill="url(#gold)"/><circle cy="-238" r="16" fill="url(#gold)"/>
<path d="M-18 -196 q8 -6 16 0 M6 -196 q8 -6 16 0" stroke="#7a5212" stroke-width="4" fill="none"/><path d="M-12 -172 Q0 -164 12 -172" stroke="#7a5212" stroke-width="4" fill="none"/>
<path d="M40 -140 L70 -250" stroke="url(#gold)" stroke-width="22" stroke-linecap="round"/><circle cx="72" cy="-262" r="13" fill="url(#gold)"/>
<path d="M-40 -130 L-80 -30" stroke="url(#gold)" stroke-width="22" stroke-linecap="round"/><circle cx="-84" cy="-20" r="13" fill="url(#gold)"/></g>
</g>
<path d="M440 120 L470 80 M450 150 L500 130" stroke="#ffe08a" stroke-width="5" stroke-linecap="round" filter="url(#glow)"/>''')


def bd_mudra():
    def hand_up(x, y):
        return f'<g transform="translate({x} {y})"><path d="M-36 60 L-36 -10 Q-36 -30 -24 -30 L-24 -70 Q-24 -84 -12 -84 Q0 -84 0 -70 L0 -84 Q0 -98 12 -98 Q24 -98 24 -84 L24 -70 Q24 -84 36 -84 Q48 -84 48 -70 L48 10 Q48 60 20 70 L-10 70 Z" fill="url(#gold)" stroke="#8a5a1c" stroke-width="3"/><path d="M-36 -10 Q-60 -20 -64 -46 Q-50 -52 -36 -32" fill="url(#gold)" stroke="#8a5a1c" stroke-width="3"/></g>'
    panels = [('禪定印', '讓心安定', 'M-70 20 Q0 70 70 20 Q40 0 0 4 Q-40 0 -70 20 Z M-10 6 Q0 -16 10 6'),
              ('施無畏印', '不要害怕', None),
              ('說法印', '講重要的道理', 'M-60 30 Q-70 -20 -30 -30 L-6 -6 M60 30 Q70 -20 30 -30 L6 -6')]
    out = ''
    for i, (n, d, path) in enumerate(panels):
        x = 40 + i * 215
        out += f'<g filter="url(#sh)"><rect x="{x}" y="70" width="195" height="400" rx="16" fill="#3b2f27"/></g>'
        out += f'<circle cx="{x+97}" cy="230" r="80" fill="url(#halo)" opacity=".5"/>'
        if path:
            out += f'<path transform="translate({x+97} 240)" d="{path}" fill="url(#gold)" stroke="#8a5a1c" stroke-width="5" stroke-linejoin="round"/>'
        else:
            out += hand_up(x + 90, 240)
        out += f'<text x="{x+97}" y="390" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="900" font-size="32" fill="#ffd76a">{n}</text>'
        out += f'<text x="{x+97}" y="435" text-anchor="middle" font-family="Noto Sans CJK TC" font-size="22" fill="#f1e6d0">{d}</text>'
    return svg(out)


def bd_route():
    return svg(f'''
<rect x="40" y="50" width="620" height="440" rx="16" fill="#e9dcc0" stroke="#8a6a3d" stroke-width="6" filter="url(#sh)"/>
<path d="M60 70 L640 70 L640 470 L60 470 Z" fill="#a9c6d4"/>
<path d="M60 120 Q160 100 260 140 Q330 130 380 160 Q460 120 540 150 Q600 140 640 160 L640 470 L420 470 Q400 400 360 380 Q330 420 300 470 L180 470 Q160 400 120 380 Q90 330 60 340 Z" fill="#d8cba6"/>
<path d="M560 250 q30 -10 40 20 q-14 30 -40 20 z M600 200 q20 0 20 30 q-20 10 -24 -10 z" fill="#d8cba6"/>
<path d="M190 380 q10 -6 14 4 q-6 12 -14 6 z" fill="#d8cba6"/>
<path d="M200 330 C220 260 260 220 320 210 S440 190 500 210 S560 230 590 230" stroke="#c0392b" stroke-width="7" fill="none" stroke-dasharray="16 10" stroke-linecap="round"/>
<path d="M200 330 L196 380" stroke="#c0392b" stroke-width="6" stroke-dasharray="10 8"/>
<path d="M200 330 C170 260 150 200 180 160" stroke="#c0392b" stroke-width="6" fill="none" stroke-dasharray="10 8"/>
<path d="M580 218 L606 230 L580 244 Z" fill="#c0392b"/>
<g font-family="Noto Sans CJK TC" font-weight="700" font-size="22" fill="#3a2a20">
<text x="150" y="345">印度</text><text x="150" y="410">斯里蘭卡</text><text x="140" y="150">中亞</text><text x="330" y="200">絲路</text><text x="450" y="250">中國</text><text x="555" y="190">韓國</text><text x="580" y="290">日本</text></g>
<circle cx="200" cy="330" r="12" fill="#c0392b"/>''')


def bd_guanyin():
    import math
    arms = ''
    for k in range(26):
        a = math.radians(-170 + k * (340 / 25))
        x = 350 + math.cos(a) * 190; y = 260 + math.sin(a) * 190
        arms += f'<path d="M350 260 L{x:.0f} {y:.0f}" stroke="url(#gold)" stroke-width="12" stroke-linecap="round"/>'
        arms += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="11" fill="url(#gold)"/>'
    return svg(f'''
<circle cx="350" cy="260" r="230" fill="url(#halo)" opacity=".7"/>
<g filter="url(#sh)">{arms}
<path d="M290 480 Q270 360 300 290 L400 290 Q430 360 410 480 Z" fill="url(#gold)"/>
<path d="M300 330 Q350 300 400 330" stroke="#a8741c" stroke-width="4" fill="none"/>
<path d="M340 300 L310 210 M360 300 L390 210" stroke="url(#gold)" stroke-width="18" stroke-linecap="round"/>
<path d="M300 200 L350 180 L400 200 L350 230 Z" fill="url(#gold)"/>
<circle cx="350" cy="140" r="50" fill="url(#gold)"/><path d="M310 108 L350 64 L390 108 Z" fill="url(#gold)" stroke="#a8741c" stroke-width="3"/>
<path d="M328 140 q8 -6 16 0 M356 140 q8 -6 16 0" stroke="#7a5212" stroke-width="4" fill="none"/><path d="M338 162 Q350 170 362 162" stroke="#7a5212" stroke-width="4" fill="none"/>
<rect x="250" y="480" width="200" height="40" rx="8" fill="#3b2a20"/></g>''')


def bd_craft():
    return svg(f'''
<g filter="url(#sh)">
<g transform="translate(150 320)"><path d="M-70 120 L-70 -60 Q-70 -130 0 -140 Q70 -130 70 -60 L70 120 Z" fill="#9c6b4a"/>
<path d="M-50 100 L-50 -50 Q-50 -110 0 -116 Q50 -110 50 -50 L50 100 Z" fill="#5a3b22"/>
<path d="M-20 -150 L-20 -200 L20 -200 L20 -150" fill="#7a4a2a"/><text y="170" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="700" font-size="22" fill="#f1e6d0">① 做模型</text></g>
<g transform="translate(350 300)"><path d="M-50 -120 L50 -120 L40 -20 L-40 -20 Z" fill="#555"/><path d="M40 -100 L110 -130" stroke="#555" stroke-width="16" stroke-linecap="round"/>
<path d="M-36 -20 Q-30 40 -10 120" stroke="#ff8a1e" stroke-width="16" fill="none" filter="url(#glow)"/><text y="190" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="700" font-size="22" fill="#f1e6d0">② 倒入銅液</text></g>
<g transform="translate(550 330)"><path d="M-55 110 Q-70 20 -40 -10 L40 -10 Q70 20 55 110 Z" fill="url(#gold)"/><circle cy="-50" r="40" fill="url(#gold)"/><circle cy="-94" r="12" fill="url(#gold)"/>
<path d="M-40 60 Q0 80 40 60" stroke="#a8741c" stroke-width="4" fill="none"/><text y="160" text-anchor="middle" font-family="Noto Sans CJK TC" font-weight="700" font-size="22" fill="#f1e6d0">③ 打磨鎏金</text></g>
</g>
<path d="M230 300 L270 300 M440 300 L480 300" stroke="#ffd76a" stroke-width="6" marker-end="url(#ar)"/>
<path d="M262 288 L282 300 L262 312 Z M472 288 L492 300 L472 312 Z" fill="#ffd76a"/>''')


def bd_title():
    return '''<div class="title-plate" style="color:#f6ead2">
<div class="t-kicker" style="color:#ffd76a">常設展・3F S303</div>
<div class="t-main" style="font-family:'Noto Serif CJK TC';font-weight:900">佛陀形影</div>
<div class="t-sub">院藏亞洲佛教藝術之美</div>
<div class="t-date">印度・中亞・中國・韓國・日本</div></div>'''


def bd_egg():
    return svg(f'''
<ellipse cx="350" cy="510" rx="140" ry="18" fill="#000" opacity=".35"/>
<g filter="url(#sh)">
<path d="M220 500 Q220 380 280 350 L420 350 Q480 380 480 500 Z" fill="url(#stone)"/>
<path d="M260 390 Q350 440 440 390" stroke="#e2b247" stroke-width="8" fill="none"/><circle cx="350" cy="430" r="14" fill="#c0392b"/><circle cx="300" cy="415" r="8" fill="#1f9e8a"/><circle cx="400" cy="415" r="8" fill="#1f9e8a"/>
<rect x="320" y="300" width="60" height="60" fill="#a59d8f"/>
<ellipse cx="350" cy="230" rx="78" ry="92" fill="#b9b2a5"/>
{''.join(f'<circle cx="{350+dx}" cy="{150+dy}" r="18" fill="#8f877a"/>' for dx, dy in [(-60,10),(-36,-14),(-8,-24),(22,-22),(50,-10),(68,14),(-72,40),(76,44)])}
<path d="M340 220 L334 262 L350 268" stroke="#6e675c" stroke-width="5" fill="none"/>
<path d="M310 214 q12 -8 24 0 M366 214 q12 -8 24 0" stroke="#5a5348" stroke-width="4" fill="none"/>
<path d="M326 290 Q350 302 374 290" stroke="#5a5348" stroke-width="4" fill="none"/></g>
<g transform="translate(520 380)"><path d="M-20 60 Q-34 0 -14 -20 L-10 -60 L10 -60 L14 -20 Q34 0 20 60 Z" fill="url(#bronze)"/></g>''')


ROOMS = {
  'himalaya': {'exhibits': [him_mountain, him_ganges, him_route, him_thangka, him_newar, him_king], 'title': him_title, 'egg': him_egg},
  'fishing': {'exhibits': [fish_net, fish_family, fish_snow, fish_hermit, fish_zhuangzi, fish_tools], 'title': fish_title, 'egg': fish_egg},
  'calligraphy': {'exhibits': [cal_copy, cal_linmo, cal_tiger, cal_qianwen, cal_scripts, cal_jiucheng], 'title': cal_title, 'egg': cal_egg},
  'tea': {'exhibits': [tea_tang, tea_song, tea_ming, tea_japan, tea_mongol, tea_taiwan], 'title': tea_title, 'egg': tea_egg},
  'tiantuan': {'exhibits': [tt_eight, tt_three, tt_hehe, tt_arhat, tt_seven, tt_wubin], 'title': tt_title, 'egg': tt_egg},
  'buddha': {'exhibits': [bd_yakshi, bd_birth, bd_mudra, bd_route, bd_guanyin, bd_craft], 'title': bd_title, 'egg': bd_egg},
}
