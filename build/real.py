# -*- coding: utf-8 -*-
# Real NPM Open Data (CC0) photos: crop boxes and how each is staged.
import os, sys
from PIL import Image

SRC = '/mnt/user-data/uploads/故宮南院文物小旅行/assets'
CROP = {  # fractions (l, t, r, b) removing colour charts / catalogue tags
  'f-snow': (0.27, 0.25, 0.78, 0.75), 'c-cursive': (0.265, 0.05, 0.535, 0.95),
  'c-copy': (0.0, 0.02, 0.93, 0.88), 'c-qianwen': (0.0, 0.02, 0.93, 0.88),
  'c-tiger': (0.1, 0.02, 0.92, 0.98), 'c-jiucheng': (0.07, 0.05, 0.9, 0.95),
  'g-wubin': (0.52, 0.05, 0.93, 0.95), 'g-three': (0.15, 0.22, 0.88, 0.79),
  't-song': (0.1, 0.18, 0.9, 0.82), 'g-hehe': (0.12, 0.0, 0.88, 0.84),
  't-tang': (0.08, 0.04, 0.95, 0.84), 'g-arhat': (0.05, 0.0, 0.95, 0.86),
  'g-eight': (0.15, 0.0, 0.85, 0.88), 'g-seven': (0.0, 0.0, 1.0, 0.82),
  't-mongol': (0.0, 0.0, 1.0, 0.86), 'c-seal': (0.03, 0.02, 0.97, 0.98),
  'c-clerical': (0.03, 0.01, 0.97, 0.99),
  'h-king': (0.1, 0.0, 1.0, 1.0), 'b-maitreya-egg': (0.0, 0.0, 1.0, 0.88),
  't-ming-cup': (0.12, 0.25, 0.88, 0.7), 'f-year-egg': (0.15, 0.3, 0.85, 0.74),
  'c-linmo-copy': (0.08, 0.02, 0.88, 0.94), 'c-linmo-study': (0.09, 0.03, 0.9, 0.94),
  'b-mudra-meditation': (0.0, 0.0, 1.0, 0.8), 'b-mudra-teaching': (0.0, 0.0, 1.0, 0.84),
  'f-zhuangzi': (0.0, 0.27, 1.0, 0.67), 'b-craft-process': (0.0, 0.15, 1.0, 0.85),
  't-japan': (0.1, 0.1, 0.9, 0.85), 't-taiwan-cup': (0.1, 0.25, 0.9, 0.8),
}

# hotspot id -> (photo id, staging kind, object label)
# kind: object (free-standing in a lit vitrine) | painting (mounted scroll/leaf) | screen (on a touch screen)
REAL = {
  'h-king': ('h-king', 'object', '青銅鎏金南天王立像'),
  'f-net': ('f-net', 'painting', '清 丁觀鵬 摹宋人漁樂圖 軸'),
  'f-family': ('f-family', 'painting', '宋人 漁樂圖 軸'),
  'f-snow': ('f-snow', 'painting', '民國 王震 寒江獨釣 軸'),
  'f-hermit': ('f-hermit', 'painting', '明 唐寅 花溪漁隱圖 軸'),
  'c-copy': ('c-copy', 'screen', '明 文徵明 四體千文（楷書）'),
  'c-tiger': ('c-tiger', 'painting', '九成宮醴泉銘 拓本 冊'),
  'c-qianwen': ('c-qianwen', 'screen', '明 文徵明 四體千文 卷'),
  'c-jiucheng': ('c-jiucheng', 'screen', '唐 歐陽詢 九成宮醴泉銘 宋拓本'),
  't-tang': ('t-tang', 'object', '長沙窯 綠釉單柄壺'),
  't-song': ('t-song', 'object', '建窯 黑釉兔毫盞'),
  't-mongol': ('t-mongol', 'object', '仿拉古里木釉多穆壺'),
  'g-eight': ('g-eight', 'object', '清 雕象牙八仙渡海臂擱'),
  'g-three': ('g-three', 'object', '明 剔紅山水人物方盒'),
  'g-hehe': ('g-hehe', 'object', '清 竹雕和合二仙'),
  'g-arhat': ('g-arhat', 'object', '清乾隆 洋彩開光十八羅漢膽瓶'),
  'g-seven': ('g-seven', 'object', '清 玉供碗（陰刻七佛）'),
  'g-wubin': ('g-wubin', 'painting', '明 吳彬 畫楞嚴廿五圓通佛像 冊'),
  'g-cabbage-egg': ('g-cabbage-egg', 'object', '清 翠玉白菜'),
  'b-yakshi': ('b-yakshi', 'object', '貴霜王朝 秣菟羅佛塔欄楯'),
  'b-birth': ('b-birth', 'object', '日本白鳳時代 銅鎏金誕生佛立像'),
  'b-guanyin': ('b-guanyin', 'object', '千手觀音倚坐像'),
  'b-maitreya-egg': ('b-maitreya-egg', 'object', '犍陀羅 石雕彌勒菩薩立像'),
  'h-mountain': ('h-mountain', 'photo', '從太空看喜瑪拉雅山脈｜NASA（公有領域）'),
  'h-ganges': ('h-ganges', 'photo', '鹿野苑 達美克佛塔｜攝影 Rmanish1973，CC BY-SA 3.0'),
  'h-mandala': ('h-mandala', 'painting', 'Mandala of Jnanadakini（同類作品）｜大都會藝術博物館藏 1987.16，公有領域'),
  'h-newar': ('h-newar', 'painting', 'Chakrasamvara Mandala｜大都會藝術博物館藏 1995.233，公有領域'),
  'f-zhuangzi': ('f-zhuangzi', 'painting', '清 董邦達 花港觀魚 御題 軸'),
  'f-year-egg': ('f-year-egg', 'object', '青花蓮塘魚藻紋杯'),
  't-japan': ('t-japan', 'object', '日本 志野鐵繪龜甲紋茶碗 銘「春錦」'),
  't-contest-egg': ('t-contest-egg', 'painting', '宋 劉松年 攆茶圖 軸'),
  'b-craft': ('b-craft-process', 'photo', '印度工匠製作失蠟鑄造蠟模｜攝影 Shoot stufz，CC BY-SA 4.0'),
}
# several real pieces in one case: hotspot -> (kind, [(photo, caption)], label line)
MULTI = {
  'c-linmo': ('painting', [('c-linmo-copy', '字帖'), ('c-linmo-study', '臨本')], '晉王羲之蘭亭序墨拓本／清高宗御臨懷仁集王羲之書'),
  't-ming': ('object', [('t-ming-pot', '紫砂壺'), ('t-ming-cup', '甜白茶鍾')], '甜白暗花葵花式茶鍾、花卉款梨形紫砂壺（清代比較件）'),
  't-taiwan': ('object', [('t-taiwan-pot', '孟臣壺'), ('t-taiwan-cup', '工夫茶杯')], '「孟臣製」款紫砂壺、工夫茶器組青花杯'),
  'b-mudra': ('object', [('b-mudra-meditation', '禪定印'), ('b-mudra-fearless', '施無畏印'), ('b-mudra-teaching', '說法印')], '北魏銅鎏金佛坐像、誕生佛立像、雙首師說法印銅佛'),
}
# route maps on the NASA Blue Marble base (lon 60E-150E, lat 50N-5N)
def ll(lon, lat, box=(60, 150, 50, 5)):
    w, e, n, so = box
    return ((lon - w) / (e - w), (n - lat) / (n - so))
HIM = (68, 98, 38, 20)
MAPS = {
  'h-route': [[('恆河平原', ll(83, 25.3, HIM)), ('喀什米爾', ll(74.8, 34, HIM))], [('恆河平原', ll(83, 25.3, HIM)), ('尼泊爾', ll(85.3, 27.7, HIM)), ('西藏俄寺', ll(88.8, 29.2, HIM))]],
  'b-route': [[('印度', ll(85, 24.7)), ('斯里蘭卡', ll(80.7, 7.9))], [('印度', ll(85, 24.7)), ('中亞', ll(76, 39.5)), ('敦煌', ll(94.7, 40.1)), ('長安', ll(108.9, 34.3)), ('韓國', ll(129.2, 35.8)), ('日本', ll(135.8, 34.7))]],
}
# the four scripts panel uses four real works side by side
SCRIPTS = [('c-seal', '篆', '吳昌碩'), ('c-clerical', '隸', '俞樾'), ('c-copy', '楷', '文徵明'), ('c-cursive', '草', '王鐸')]


def prepare(out):
    os.makedirs(out, exist_ok=True)
    ids = set(v[0] for v in REAL.values()) | set(s[0] for s in SCRIPTS) | {p for m in MULTI.values() for p, _ in m[1]} | {'asia-satellite'}
    for pid in sorted(ids):
        im = Image.open(os.path.join(SRC, pid + '.jpg')).convert('RGB')
        if pid in CROP:
            l, t, r, b = CROP[pid]; W, H = im.size
            im = im.crop((int(l * W), int(t * H), int(r * W), int(b * H)))
        im.save(os.path.join(out, pid + '.jpg'), quality=92)
        if pid == 'asia-satellite':
            W, H = im.size; w, e, n, so = HIM
            im.crop((int((w - 60) / 90 * W), int((50 - n) / 45 * H), int((e - 60) / 90 * W), int((50 - so) / 45 * H))).resize((1200, 720)).save(os.path.join(out, 'asia-satellite-him.jpg'), quality=92)
    print('prepared', len(ids))


if __name__ == '__main__':
    prepare(sys.argv[1])
