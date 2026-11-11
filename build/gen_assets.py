# -*- coding: utf-8 -*-
# Badges (256px), mascot (1024px) and certificate background (1754x1240), drawn as SVG and screenshotted.
import os, sys, asyncio

BADGES = {
  'himalaya': ('雪', '#7a2e22', '#f2c14e'), 'fishing': ('漁', '#2f5d62', '#cfe3df'),
  'calligraphy': ('書', '#1b4f8a', '#9fd3ff'), 'tea': ('茶', '#5a3b22', '#e9c78f'),
  'tiantuan': ('團', '#5b2a86', '#ffd76a'), 'buddha': ('佛', '#8a6a20', '#fff1b8'),
}


def badge_svg(ch, c1, c2):
    rays = ''.join(f'<path d="M128 128 L{128+120*__import__("math").cos(a*0.2618):.1f} {128+120*__import__("math").sin(a*0.2618):.1f} L{128+120*__import__("math").cos(a*0.2618+0.13):.1f} {128+120*__import__("math").sin(a*0.2618+0.13):.1f} Z" fill="{c2}" opacity=".55"/>' for a in range(24))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 256 256">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff1b8"/><stop offset=".45" stop-color="#e2b247"/><stop offset="1" stop-color="#a8741c"/></linearGradient></defs>
<path d="M80 170 L60 250 L95 232 L112 256 L128 180 Z" fill="{c1}"/><path d="M176 170 L196 250 L161 232 L144 256 L128 180 Z" fill="{c1}"/>
{rays}
<circle cx="128" cy="120" r="100" fill="url(#g)"/>
<circle cx="128" cy="120" r="84" fill="{c1}"/>
<circle cx="128" cy="120" r="76" fill="none" stroke="{c2}" stroke-width="3" stroke-dasharray="4 6"/>
<text x="128" y="152" text-anchor="middle" font-family="Noto Serif CJK TC" font-weight="900" font-size="96" fill="{c2}">{ch}</text>
</svg>'''


MASCOT = '''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
<linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e3b56d"/><stop offset=".5" stop-color="#b9823f"/><stop offset="1" stop-color="#7d5124"/></linearGradient>
<linearGradient id="t" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5fb3a3"/><stop offset="1" stop-color="#2f7d70"/></linearGradient>
<filter id="s"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-opacity=".3"/></filter>
</defs>
<g filter="url(#s)">
<path d="M330 760 L290 930 Q290 950 312 950 L350 950 Q368 950 372 930 L410 770 Z" fill="url(#b)"/>
<path d="M694 760 L734 930 Q734 950 712 950 L674 950 Q656 950 652 930 L614 770 Z" fill="url(#b)"/>
<path d="M512 840 L500 960 Q500 975 520 975 L540 975 Q556 975 552 960 L540 840 Z" fill="url(#b)"/>
<path d="M300 300 L300 200 Q300 170 330 170 L360 170 Q390 170 390 200 L390 330 Z" fill="url(#b)" stroke="#6b4420" stroke-width="10"/>
<path d="M724 300 L724 200 Q724 170 694 170 L664 170 Q634 170 634 200 L634 330 Z" fill="url(#b)" stroke="#6b4420" stroke-width="10"/>
<path d="M210 330 Q512 250 814 330 Q850 560 760 720 Q650 860 512 860 Q374 860 264 720 Q174 560 210 330 Z" fill="url(#b)" stroke="#6b4420" stroke-width="12"/>
<path d="M220 360 Q512 300 804 360 L798 420 Q512 370 226 420 Z" fill="url(#t)"/>
<path d="M250 640 Q512 700 774 640" stroke="#6b4420" stroke-width="8" fill="none" opacity=".5"/>
<path d="M300 660 q30 -40 60 0 t60 0 t60 0 t60 0 t60 0 t60 0 t60 0" stroke="url(#t)" stroke-width="16" fill="none"/>
<ellipse cx="400" cy="520" rx="44" ry="54" fill="#2a1a10"/><ellipse cx="624" cy="520" rx="44" ry="54" fill="#2a1a10"/>
<circle cx="414" cy="502" r="16" fill="#fff"/><circle cx="638" cy="502" r="16" fill="#fff"/>
<ellipse cx="330" cy="600" rx="40" ry="22" fill="#f08a7a" opacity=".55"/><ellipse cx="694" cy="600" rx="40" ry="22" fill="#f08a7a" opacity=".55"/>
<path d="M470 600 Q512 650 554 600" stroke="#2a1a10" stroke-width="14" fill="none" stroke-linecap="round"/>
<path d="M200 470 Q120 450 110 380" stroke="url(#b)" stroke-width="40" fill="none" stroke-linecap="round"/>
<circle cx="108" cy="360" r="36" fill="url(#b)"/>
<path d="M824 500 Q900 520 930 470" stroke="url(#b)" stroke-width="40" fill="none" stroke-linecap="round"/>
<rect x="900" y="330" width="80" height="120" rx="10" fill="#f6efdc" stroke="#6b4420" stroke-width="8" transform="rotate(12 940 390)"/>
<path d="M918 360 l50 10 M914 385 l50 10 M910 410 l40 8" stroke="#c0392b" stroke-width="8" transform="rotate(12 940 390)"/>
</g></svg>'''


def cert_bg():
    import math
    clouds = ''
    for (x, y, s) in [(60, 60, 1), (1694, 60, -1), (60, 1180, 1), (1694, 1180, -1)]:
        clouds += f'<g transform="translate({x} {y}) scale({s} {1 if y < 600 else -1})"><circle r="70" fill="#f6efdc" stroke="#b8862f" stroke-width="6"/><path d="M-36 10 q0 -36 36 -36 q36 0 36 30 q0 24 -24 24 q-20 0 -20 -18 q0 -14 14 -14" stroke="#1d5c6e" stroke-width="8" fill="none" stroke-linecap="round"/></g>'
    meander = ''.join(f'<path d="M{x} 40 h30 v30 h-20 v-14 h10" stroke="#b8862f" stroke-width="4" fill="none"/>' for x in range(150, 1600, 44))
    meander2 = ''.join(f'<path d="M{x} 1200 h30 v-30 h-20 v14 h10" stroke="#b8862f" stroke-width="4" fill="none"/>' for x in range(150, 1600, 44))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1754" height="1240" viewBox="0 0 1754 1240">
<defs><radialGradient id="p" cx=".5" cy=".45" r=".7"><stop offset="0" stop-color="#fffdf6"/><stop offset="1" stop-color="#f1e6cc"/></radialGradient></defs>
<rect width="1754" height="1240" fill="#f3e8d0"/>
<rect x="20" y="20" width="1714" height="1200" rx="28" fill="none" stroke="#1d5c6e" stroke-width="22"/>
<rect x="44" y="44" width="1666" height="1152" rx="18" fill="url(#p)" stroke="#b8862f" stroke-width="4"/>
{meander}{meander2}
<path d="M150 1110 Q400 1000 650 1080 T1150 1060 T1620 1090 L1620 1150 L150 1150 Z" fill="#1d5c6e" opacity=".07"/>
<path d="M400 1150 L560 980 L680 1100 L820 960 L980 1120 L1100 1010 L1300 1150 Z" fill="#1d5c6e" opacity=".06"/>
{clouds}
</svg>'''


async def main(outdir):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        async def shot(name, svg, w, h, transparent=True):
            pg = await b.new_page(viewport={'width': w, 'height': h})
            html = f'<html><body style="margin:0;background:transparent">{svg}</body></html>'
            await pg.set_content(html)
            await pg.wait_for_timeout(150)
            await pg.screenshot(path=os.path.join(outdir, name), omit_background=transparent, clip={'x': 0, 'y': 0, 'width': w, 'height': h})
            await pg.close()
        for k, (ch, c1, c2) in BADGES.items():
            await shot(f'badge_{k}.png', badge_svg(ch, c1, c2), 256, 256)
        await shot('mascot.png', MASCOT, 1024, 1024)
        await shot('cert_bg.png', cert_bg(), 1754, 1240, transparent=False)
        await b.close()

if __name__ == '__main__':
    out = os.path.abspath(sys.argv[1]); os.makedirs(out, exist_ok=True)
    asyncio.run(main(out)); print('assets ok')
