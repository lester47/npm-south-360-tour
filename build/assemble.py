# -*- coding: utf-8 -*-
import re, sys, json, base64, os
sys.path.insert(0, os.path.dirname(__file__))
from content import DATA

SRC, OUT, ASSETS = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(SRC, encoding='utf-8').read()


def uri(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(open(path, 'rb').read()).decode()


ids = [e['id'] for e in DATA['eras']]
badges = {i: uri(f'{ASSETS}/badge_{i}.png', 'image/png') for i in ids}
panos = {i: uri(f'{ASSETS}/pano_{i}.jpg', 'image/jpeg') for i in ids}
mascot = uri(f'{ASSETS}/mascot.png', 'image/png')
certbg = uri(f'{ASSETS}/cert_bg.png', 'image/png')

data = json.loads(json.dumps(DATA))
for e in data['eras']:
    e['badge'] = badges[e['id']]


def replace_block(s, marker, new_js):
    i = s.index(marker)
    j = s.index('</script>', i)
    return s[:i] + new_js + '\n' + s[j:]


s = replace_block(s, 'window.ERAS_DATA = {', 'window.ERAS_DATA = ' + json.dumps(data, ensure_ascii=False, indent=1) + ';')
s = replace_block(s, 'window.PANO_DATA = {', 'window.PANO_DATA = ' + json.dumps(panos) + ';')
cert = {'bg': certbg, 'mascot': mascot}; cert.update(badges)
s = replace_block(s, 'window.CERT_ASSETS = {', 'window.CERT_ASSETS = ' + json.dumps(cert) + ';')

# inline mascot <img> tags
s = re.sub(r'(<img src=")data:image/[a-z]+;base64,[A-Za-z0-9+/=]+(" alt="茶芽小隊長")', lambda m: m.group(1) + mascot + m.group(2), s)

REPL = [
  ('      if (window.isTeacherMode) return true;', '      return true; // all rooms open: explore in any order'),
  ('🔓 目前關卡・點擊啟動探索', '🔓 可自由探索・點擊進入'),
  ('.marker-icon-box {\n  width: 56px;\n  height: 56px;', '.marker-icon-box {\n  width: 44px;\n  height: 44px;'),
  ('  font-size: 28px;\n  border: 3.5px solid #ffffff;', '  font-size: 22px;\n  border: 3px solid #ffffff;'),
  ('  width: 60px;\n  height: 60px;\n  border-radius: 50%;\n  pointer-events: none;', '  width: 48px;\n  height: 48px;\n  border-radius: 50%;\n  pointer-events: none;'),
  ('  padding: 6px 14px;\n  border-radius: 16px;\n  font-size: 15px;', '  padding: 4px 10px;\n  border-radius: 14px;\n  font-size: 13px;'),
  ('<span class="brand-icon">🌱</span>', '<span class="brand-icon">🏛️</span>'),
  ('🌱 開始闖關任務', '🎯 開始闖關任務'),
  ('`🌱 ${currentEra.name}', '`🎯 ${currentEra.name}'),
  ('搭上食農小火車走訪南投五大產地，轉動 360° 全景畫面找出產地線索，完成闖關任務，成為南投食農小大使！', '跟著小鼎導覽員走訪故宮南院六大展廳，轉動 360° 全景畫面找出文物線索，完成闖關任務，成為故宮南院文物小導覽員！'),
  ('<h3>🎉 恭喜走完南投五大產地！</h3>', '<h3>🎉 恭喜走完故宮南院六大展廳！</h3>'),
  ('<p>準備好領取「南投食農小大使」證書了嗎？</p>', '<p>準備好領取「故宮南院文物小導覽員」證書了嗎？</p>'),
  ('<h2>📊 南投五大產地農產比較總表</h2>', '<h2>📊 故宮南院六大展廳比較總表</h2>'),
  ("'搭乘食農小火車，走訪南投五大產地，'", "'走進故宮南院六大展廳，'"),
  ("'細心觀察產地線索，並全數完成闖關任務，'", "'細心觀察文物線索，並全數完成闖關任務，'"),
  ('<title>南投食農小旅行：360° 從產地到餐桌｜國小食農教育數位教材</title>', '<title>故宮南院文物小旅行</title>'),
  ('國小食農教育：透過 360° 全景走訪南投鹿谷、魚池、埔里、信義、竹山五大產地生活，挑戰生存問答領取探險家證書！', '故宮南院校外教學：透過 360° 全景走訪六大展廳，找出文物線索、完成闖關任務，領取文物小導覽員證書！'),
  ('<h1 class="brand-title">南投食農小旅行</h1>', '<h1 class="brand-title">故宮南院文物小旅行</h1>'),
  ('title="查看五大產地比較表"', 'title="查看六大展廳比較表"'),
  ('📊 產地農產比較表', '📊 展廳比較總表'),
  ('alt="茶芽小隊長"', 'alt="小鼎導覽員"'),
  ('南投食農小旅行<br>360° 從產地到餐桌', '故宮南院文物小旅行<br>360° 穿越六大展廳'),
  ('請輸入小大使姓名：', '請輸入小導覽員姓名：'),
  ('🚂 搭上食農小火車', '🎫 刷票進入故宮南院'),
  ('🗺️ 南投產地地圖', '🗺️ 故宮南院展廳地圖'),
  ('歡迎小大使 <strong', '歡迎小導覽員 <strong'),
  ('！請依序走訪南投五大產地：', '！六大展廳可以任選順序探索（建議路線 1F → 2F → 3F）：'),
  ('🏆 前往領取食農小大使證書', '🏆 前往領取文物小導覽員證書'),
  ('title="返回產地地圖"', 'title="返回展廳地圖"'),
  ('<span class="hud-btn-text">回產地地圖</span>', '<span class="hud-btn-text">回展廳地圖</span>'),
  ('產地名稱', '展廳名稱'), ('產地資訊', '展廳資訊'),
  ('<span class="captain-speaker-name">茶芽小隊長：</span>', '<span class="captain-speaker-name">小鼎導覽員：</span>'),
  ('產地・闖關任務', '展廳・闖關任務'),
  ('🎉 恭喜榮獲食農小大使證書！', '🎉 恭喜榮獲文物小導覽員證書！'),
  ('你已經走完南投五大產地，表現優異，快下載或列印你的榮譽證書吧！', '你已經走完故宮南院六大展廳，表現優異，快下載或列印你的榮譽證書吧！'),
  ('🏠 回產地地圖', '🏠 回展廳地圖'),
  ('前往下一個產地 ➔', '前往下一個展廳 ➔'),
  ('這個產地的線索你都找齊了', '這個展廳的線索你都找齊了'),
  ("name: '食農小大使終極任務'", "name: '文物小導覽員終極任務'"),
  ("|| '南投食農小大使'", "|| '故宮南院文物小導覽員'"),
  ('領取食農小大使證書', '領取文物小導覽員證書'),
  ("|| '小小食農大使'", "|| '小小導覽員'"),
  ("|| '食農小達人'", "|| '文物小達人'"),
  ("|| '食農小大使'", "|| '文物小導覽員'"),
  ('個產地任務', '個展廳任務'),
  ("|| '小大使'", "|| '小導覽員'"),
  ('<span class="node-label">🍽️ 餐桌</span>', '<span class="node-label">🏆 證書</span>'),
  ('📍 產地：', '📍 展廳：'),
  ('這一站還沒開放喔！', '這個展廳還沒開放喔！'),
  ('認識了這裡的農產與農夫的智慧！', '認識了這個展廳的文物與背後的故事！'),
  ('NT-FOOD-', 'NPM-S-'),
  ("const STORAGE_KEY = 'nantou_food_360_progress';", "const STORAGE_KEY = 'npm_south_360_progress';"),
  ("unlockedEras: ['paleolithic']", f"unlockedEras: ['{ids[0]}']"),
  ("lastActiveEra: 'paleolithic'", f"lastActiveEra: '{ids[0]}'"),
  # palette: tea-garden green -> museum celadon teal
  ('--color-bg: #f4f7ec;', '--color-bg: #f6f1e7;'), ('--color-card-bg: #fffffa;', '--color-card-bg: #fffdf8;'),
  ('--color-earth-dark: #2f3a1f;', '--color-earth-dark: #2b2622;'), ('--color-earth-medium: #5a5034;', '--color-earth-medium: #5b4a3a;'),
  ('--color-earth-light: #edf2e1;', '--color-earth-light: #efe8dc;'), ('--color-border: #cfdcb8;', '--color-border: #dccfb8;'),
  ('#2e7d32', '#1d5c6e'), ('#388e3c', '#24707f'), ('#1b5e20', '#123f4c'), ('#e8f5e9', '#e6f1f1'),
  ('#c8e6c9', '#c9e0e0'), ('#a5d6a7', '#a6cccd'), ('#81c784', '#7fb4b6'),
  ('rgba(46, 125, 50', 'rgba(29, 92, 110'), ('rgba(76, 175, 80', 'rgba(60, 150, 160'),
]
for a, b in REPL:
    if a not in s:
        print('MISSING:', a[:60])
    s = s.replace(a, b)

open(OUT, 'w', encoding='utf-8').write(s)
print('wrote', OUT, round(len(s) / 1e6, 2), 'MB')
left = re.findall(r'[^\n]{0,20}(?:南投|食農|產地|茶芽)[^\n]{0,20}', re.sub(r'base64,[A-Za-z0-9+/=]+', '', s))
print('leftover theme words:', len(left)); [print('  ', l) for l in left[:30]]
