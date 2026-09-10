# -*- coding: utf-8 -*-
"""既存の 1章全体ツリー を土台に、折衷案の改訂版を作る。
土台のスタート画面・骨組みだけモード・かんたん版・point-box はそのまま残し、
(1) 細胞のつくりの下に 植物の細胞／動物の細胞 をノード追加（共通/植物だけ の左右を入れ替え）
(2) 細胞の呼吸の右に 酸素＋養分（有機物）→分解→エネルギー をノード展開
(3) 語句カード13→19、まとめ文の空欄を追加
の3点だけ差し替える。既存ファイルは書き換えない。"""
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

D   = r'C:\Users\marar\Documents\MSTbase\education\matome-maps'
SRC = D + r'\chu2-1shou-seibutsu-to-saibou-zentai.html'
DST = D + r'\chu2-1shou-seibutsu-to-saibou-zentai-kai.html'
h = io.open(SRC, encoding='utf-8').read()
orig = h

def rep(old, new, tag):
    global h
    assert old in h, f'見つからない: {tag}'
    assert h.count(old) == 1, f'複数一致: {tag} ({h.count(old)}件)'
    h = h.replace(old, new)
    print(f'  置換OK: {tag}')

# ---------------- (0) 呼び名 ----------------
rep('<title>1章 生物と細胞 全体ツリー｜まとめマップ</title>',
    '<title>1章 生物と細胞 全体ツリー（改訂版）｜まとめマップ</title>', 'title')
rep('<h1>1章 生物と細胞　全体ツリー｜まとめマップ',
    '<h1>1章 生物と細胞　全体ツリー（改訂版）｜まとめマップ', 'h1')
rep('<h2>1章 生物と細胞 全体ツリー — どうやって学ぶ？</h2>',
    '<h2>1章 生物と細胞 全体ツリー（改訂版） — どうやって学ぶ？</h2>', 'スタート画面の見出し')

# ---------------- (1) 左：細胞のつくり ----------------
OLD_LEFT = '''  <line class="link" x1="380" y1="238" x2="380" y2="262"/>
  <line class="link" x1="180" y1="262" x2="580" y2="262"/>
  <line class="link" x1="180" y1="262" x2="180" y2="290"/>
  <line class="link" x1="580" y1="262" x2="580" y2="290"/>

  <text class="answer" x="180" y="278">植物・動物に共通</text>
  <text class="answer" x="580" y="278">植物の細胞だけ</text>

  <line class="link" x1="70" y1="300" x2="290" y2="300"/>
  <line class="link" x1="180" y1="290" x2="180" y2="300"/>
  <line class="link" x1="70" y1="300" x2="70" y2="318"/>
  <line class="link" x1="180" y1="300" x2="180" y2="318"/>
  <line class="link" x1="290" y1="300" x2="290" y2="318"/>

  <rect class="node-yellow kw" x="20" y="318" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="70" y="338">核</text>
  <rect class="node-yellow kw" x="130" y="318" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="180" y="338">細胞膜</text>
  <rect class="node-yellow kw" x="240" y="318" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="290" y="338">細胞質</text>

  <line class="link" x1="470" y1="300" x2="690" y2="300"/>
  <line class="link" x1="580" y1="290" x2="580" y2="300"/>
  <line class="link" x1="470" y1="300" x2="470" y2="318"/>
  <line class="link" x1="580" y1="300" x2="580" y2="318"/>
  <line class="link" x1="690" y1="300" x2="690" y2="318"/>

  <rect class="node-green kw" x="420" y="318" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-green kw" x="470" y="338">細胞壁</text>
  <rect class="node-green kw" x="530" y="318" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-green kw" x="580" y="338">葉緑体</text>
  <rect class="node-green kw" x="640" y="318" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-green kw" x="690" y="338">液胞</text>

  <rect class="node-info" x="20" y="378" width="320" height="36" rx="6"/>
  <text class="label label-ex" x="180" y="396">細胞膜と、その内側で核以外＝細胞質</text>

  <rect class="node-info" x="420" y="378" width="320" height="36" rx="6"/>
  <text class="label label-ex" x="580" y="396">細胞壁は細胞膜のさらに外側を囲む</text>'''

NEW_LEFT = '''  <line class="link" x1="380" y1="238" x2="380" y2="258"/>
  <line class="link" x1="180" y1="258" x2="580" y2="258"/>
  <line class="link" x1="180" y1="258" x2="180" y2="282"/>
  <line class="link" x1="580" y1="258" x2="580" y2="282"/>

  <rect class="node-green kw" x="90" y="282" width="180" height="40" rx="8"/>
  <text class="label label-leaf label-green kw" x="180" y="302">植物の細胞</text>
  <rect class="node-pink kw" x="490" y="282" width="180" height="40" rx="8"/>
  <text class="label label-leaf label-pink kw" x="580" y="302">動物の細胞</text>

  <!-- 植物の細胞 → 植物の細胞だけにあるつくり（まっすぐ下） -->
  <line class="link" x1="180" y1="322" x2="180" y2="368"/>
  <text class="answer" x="180" y="344">植物の細胞だけ</text>

  <!-- 植物の細胞 → 共通のつくり（横にまわって動物の細胞の線に合流） -->
  <line class="link" x1="270" y1="302" x2="400" y2="302"/>
  <line class="link" x1="400" y1="302" x2="400" y2="342"/>
  <line class="link" x1="400" y1="342" x2="580" y2="342"/>

  <line class="link" x1="580" y1="322" x2="580" y2="368"/>
  <text class="answer" x="580" y="358">植物・動物に共通</text>

  <line class="link" x1="70" y1="368" x2="290" y2="368"/>
  <line class="link" x1="70" y1="368" x2="70" y2="386"/>
  <line class="link" x1="180" y1="368" x2="180" y2="386"/>
  <line class="link" x1="290" y1="368" x2="290" y2="386"/>

  <rect class="node-green kw" x="20" y="386" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-green kw" x="70" y="406">細胞壁</text>
  <rect class="node-green kw" x="130" y="386" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-green kw" x="180" y="406">葉緑体</text>
  <rect class="node-green kw" x="240" y="386" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-green kw" x="290" y="406">液胞</text>

  <line class="link" x1="470" y1="368" x2="690" y2="368"/>
  <line class="link" x1="470" y1="368" x2="470" y2="386"/>
  <line class="link" x1="580" y1="368" x2="580" y2="386"/>
  <line class="link" x1="690" y1="368" x2="690" y2="386"/>

  <rect class="node-yellow kw" x="420" y="386" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="470" y="406">核</text>
  <rect class="node-yellow kw" x="530" y="386" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="580" y="406">細胞膜</text>
  <rect class="node-yellow kw" x="640" y="386" width="100" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="690" y="406">細胞質</text>

  <rect class="node-info" x="20" y="446" width="320" height="36" rx="6"/>
  <text class="label label-ex" x="180" y="464">細胞壁は細胞膜のさらに外側を囲む</text>

  <rect class="node-info" x="420" y="446" width="320" height="36" rx="6"/>
  <text class="label label-ex" x="580" y="464">細胞膜と、その内側で核以外＝細胞質</text>'''
rep(OLD_LEFT, NEW_LEFT, '左：細胞のつくり（植物/動物の細胞を追加・左右入れ替え）')

# 左からの集約線の起点を下げる
rep('<line class="link" x1="180" y1="414" x2="180" y2="520"/>',
    '<line class="link" x1="180" y1="482" x2="180" y2="520"/>', '左から細胞の呼吸への集約線')

# ---------------- (2) 下：細胞の呼吸の中身をノード化 ----------------
OLD_BOTTOM = '''  <rect x="320" y="614" width="760" height="54" rx="8" style="fill:#fff8e8;stroke:#c8961e;stroke-width:1.2;stroke-dasharray:4,3;"/>
  <text class="extra" x="700" y="634" style="font-size:13px;fill:#946800;text-anchor:middle;font-weight:bold;">細胞の内部で、酸素を使って養分（有機物）を分解し、エネルギーをとり出す</text>
  <text class="extra" x="700" y="655" style="font-size:12px;fill:#946800;text-anchor:middle;">単細胞生物も多細胞生物も、ひとつひとつの細胞で行っている</text>'''

NEW_BOTTOM = '''  <!-- 細胞の呼吸の中身：酸素＋養分（有機物）→ 分解 → エネルギー -->
  <line class="link" x1="820" y1="579" x2="840" y2="579"/>
  <line class="link" x1="840" y1="560" x2="840" y2="616"/>
  <line class="link" x1="840" y1="560" x2="860" y2="560"/>
  <line class="link" x1="840" y1="616" x2="860" y2="616"/>

  <rect class="node-yellow kw" x="860" y="540" width="160" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="940" y="560">酸素</text>
  <rect class="node-yellow kw" x="860" y="596" width="160" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="940" y="616" style="font-size:14px;">養分（有機物）</text>

  <line class="link" x1="1020" y1="560" x2="1050" y2="560"/>
  <line class="link" x1="1020" y1="616" x2="1050" y2="616"/>
  <line class="link" x1="1050" y1="560" x2="1050" y2="616"/>
  <line class="link" x1="1050" y1="588" x2="1080" y2="588"/>

  <rect class="node-yellow kw" x="1080" y="568" width="140" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="1150" y="588">分解</text>

  <text class="label" x="1245" y="588" style="font-size:15px;fill:#888;">→</text>

  <rect class="node-yellow kw" x="1270" y="568" width="180" height="40" rx="8"/>
  <text class="label label-leaf label-yellow kw" x="1360" y="588">エネルギー</text>

  <text class="extra" x="620" y="648" style="font-size:12px;fill:#946800;text-anchor:middle;">単細胞生物も多細胞生物も、ひとつひとつの細胞で行っている</text>'''
rep(OLD_BOTTOM, NEW_BOTTOM, '下：細胞の呼吸の中身をノード化')

# ---------------- (3) 語句カード 13 → 19 ----------------
WORDS = ['細胞','植物の細胞','動物の細胞','核','細胞膜','細胞質','細胞壁','葉緑体','液胞',
         '単細胞生物','多細胞生物','組織','器官','個体','細胞の呼吸','酸素','養分（有機物）','分解','エネルギー']
old_cards = re.search(r'(    <div class="word-card">細胞</div>.*?<div class="word-card">細胞の呼吸</div>\n)', h, re.S).group(1)
new_cards = '\n'.join(f'    <div class="word-card">{w}</div>' for w in WORDS) + '\n'
rep(old_cards, new_cards, '語句カード13→19')

# ---------------- (4) まとめ文（くわしい版）に空欄を追加 ----------------
rep('生物のからだは <span class="blank">細胞</span> からできている。植物の細胞にも動物の細胞にも共通して、<span class="blank">核</span> と <span class="blank">細胞膜</span> があり、細胞膜とその内側で核をふくまない部分をまとめて <span class="blank">細胞質</span> という。一方、<span class="blank">細胞壁</span> ・ <span class="blank">葉緑体</span> ・発達した <span class="blank">液胞</span> は、植物の細胞に見られるつくりである。',
    '生物のからだは <span class="blank">細胞</span> からできている。<span class="blank">植物の細胞</span> にも <span class="blank">動物の細胞</span> にも共通して、<span class="blank">核</span> と <span class="blank">細胞膜</span> があり、細胞膜とその内側で核をふくまない部分をまとめて <span class="blank">細胞質</span> という。一方、<span class="blank">細胞壁</span> ・ <span class="blank">葉緑体</span> ・発達した <span class="blank">液胞</span> は、<span class="blank">植物の細胞</span> だけに見られるつくりである。',
    'まとめ文 📘細胞のつくり')
rep('単細胞生物でも多細胞生物でも、細胞の内部では <span class="blank">酸素</span> を使って <span class="blank">養分</span> が分解され、<span class="blank">エネルギー</span> がとり出されている。このはたらきを <span class="blank">細胞の呼吸</span> という。',
    '単細胞生物でも多細胞生物でも、細胞の内部では <span class="blank">酸素</span> を使って <span class="blank">養分（有機物）</span> が <span class="blank">分解</span> され、<span class="blank">エネルギー</span> がとり出されている。このはたらきを <span class="blank">細胞の呼吸</span> という。',
    'まとめ文 📙1章のゴール')

io.open(DST, 'w', encoding='utf-8').write(h)
print(f'\n保存: {DST}')

# ================= 検証 =================
print('\n--- 検証 ---')
v = io.open(DST, encoding='utf-8').read()
svg = re.search(r'(<svg .*?</svg>)', v, re.S).group(1)
vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
VW, VH = int(vb.group(1)), int(vb.group(2))
print(f'viewBox: {VW}x{VH}（土台と同じか: {VW==1480 and VH==700}）')

rects = [(float(m.group(2)), float(m.group(3)), float(m.group(4)), float(m.group(5)), m.group(1))
         for m in re.finditer(r'<rect class="([^"]+)" x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)" height="([\d.]+)"', svg)]
errs = []
for i in range(len(rects)):
    for j in range(i+1, len(rects)):
        ax, ay, aw, ah, ac = rects[i]; bx, by, bw, bh, bc = rects[j]
        if ax < bx+bw and bx < ax+aw and ay < by+bh and by < ay+ah:
            errs.append(f'ノード重なり: {ac}@({ax},{ay}) x {bc}@({bx},{by})')
    x, y, w, hh, c = rects[i]
    if x < 0 or x+w > VW or y < 0 or y+hh > VH:
        errs.append(f'viewBoxはみ出し: {c}@({x},{y},{w},{hh})')
print('重なり/はみ出し:', errs if errs else 'なし')

kw = re.findall(r'<text class="label[^"]*kw"[^>]*>([^<]+)</text>', svg)
print(f'語句ノード({len(kw)}):', kw)
missing = [w for w in WORDS if w not in kw]
print('語句カード19語のうちマップに無いもの:', missing if missing else 'なし')
extra = [k for k in kw if k not in WORDS and k != '→']
print('マップにあって語句カードに無いもの:', extra if extra else 'なし')
print('骨組みだけモード: kwを持つrect =', len([r for r in rects if 'kw' in r[4]]), '個')
print('土台からの差分行数:', abs(len(v.splitlines()) - len(orig.splitlines())))
