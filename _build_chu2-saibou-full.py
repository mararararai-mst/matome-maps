# -*- coding: utf-8 -*-
"""中2 生物1章「生物と細胞」全体まとめマップ（完成見本）を生成する。
既存の全体ツリー chu1-p43-44-shokubutsu-zentai-bunrui.html の様式を踏襲。"""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

VB_W, VB_H = 1280, 760

# ---------- ノード定義 (id, label, cx, cy, w, h, nodeclass, labelclass) ----------
N = {}
def node(i, label, cx, cy, w, h, ncls, lcls, fs=15):
    N[i] = dict(label=label, cx=cx, cy=cy, w=w, h=h, ncls=ncls, lcls=lcls, fs=fs)

# 中心
node('karada', '生物のからだ', 640, 40, 220, 46, 'node-main', 'label-main', 17)
node('saibou', '細胞',        640, 110, 150, 44, 'node-main', 'label-main', 17)
# 3本の柱
node('h_tsuku', '細胞のつくり',     220, 204, 200, 42, 'node-yellow', 'label-leaf label-yellow')
node('h_nari',  'からだの成り立ち', 640, 204, 220, 42, 'node-orange', 'label-leaf label-orange')
node('h_hata',  '細胞のはたらき',   1060, 204, 210, 42, 'node-blue',  'label-leaf label-blue')

# --- 柱1 細胞のつくり ---
node('shoku', '植物の細胞', 110, 304, 160, 44, 'node-green', 'label-leaf label-green')
node('dou',   '動物の細胞', 330, 304, 160, 44, 'node-pink',  'label-leaf label-pink')
node('kyotsu','共通のつくり', 220, 382, 180, 44, 'node-yellow', 'label-leaf label-yellow')
node('kaku',  '核',       110, 460, 100, 44, 'node-yellow', 'label-leaf label-yellow')
node('maku',  '細胞膜',   220, 460, 100, 44, 'node-yellow', 'label-leaf label-yellow')
node('shitsu','細胞質',   330, 460, 100, 44, 'node-yellow', 'label-leaf label-yellow')
node('kouhen','孔辺細胞', 110, 538, 130, 44, 'node-green', 'label-leaf label-green')
node('sdake', '植物だけにある', 110, 616, 165, 44, 'node-green', 'label-leaf label-green', 14)
node('heki',  '細胞壁',   60, 694, 100, 44, 'node-yellow', 'label-leaf label-yellow')
node('you',   '葉緑体',  170, 694, 100, 44, 'node-yellow', 'label-leaf label-yellow')
node('eki',   '液胞',    280, 694, 100, 44, 'node-yellow', 'label-leaf label-yellow')

# --- 柱2 からだの成り立ち ---
node('tan', '単細胞生物', 540, 304, 170, 44, 'node-orange', 'label-leaf label-orange')
node('ta',  '多細胞生物', 740, 304, 170, 44, 'node-orange', 'label-leaf label-orange')
node('c1',  '細胞', 740, 374, 150, 44, 'node-orange', 'label-leaf label-orange')
node('c2',  '組織', 740, 454, 150, 44, 'node-orange', 'label-leaf label-orange')
node('c3',  '器官', 740, 534, 150, 44, 'node-orange', 'label-leaf label-orange')
node('c4',  '個体', 740, 614, 150, 44, 'node-orange', 'label-leaf label-orange')

# --- 柱3 細胞のはたらき ---
node('kokyu', '細胞の呼吸',   1060, 274, 190, 44, 'node-blue', 'label-leaf label-blue')
node('san',   '酸素',          990, 378, 120, 44, 'node-blue', 'label-leaf label-blue')
node('yobun', '養分（有機物）',1150, 378, 190, 44, 'node-blue', 'label-leaf label-blue')
node('bunkai','分解',         1070, 474, 140, 44, 'node-blue', 'label-leaf label-blue')
node('ene',   'エネルギー',   1070, 554, 180, 44, 'node-blue', 'label-leaf label-blue')

# ---------- 線 ----------
LINK = [  # 通常の枝
    [(640,63),(640,88)],
    [(640,132),(640,158)],
    [(220,158),(1060,158)],
    [(220,158),(220,183)], [(640,158),(640,183)], [(1060,158),(1060,183)],
    # 柱1
    [(220,225),(220,258)], [(110,258),(330,258)],
    [(110,258),(110,282)], [(330,258),(330,282)],
    [(110,326),(110,352)], [(330,326),(330,352)], [(110,352),(330,352)], [(220,352),(220,360)],
    [(220,404),(220,420)], [(110,420),(330,420)],
    [(110,420),(110,438)], [(220,420),(220,438)], [(330,420),(330,438)],
    [(30,304),(18,304),(18,594)],           # 植物の細胞からの左レール
    [(18,516),(45,516)], [(18,594),(30,594)],
    [(110,638),(110,656)], [(60,656),(280,656)],
    [(60,656),(60,672)], [(170,656),(170,672)], [(280,656),(280,672)],
    # 柱2
    [(640,225),(640,258)], [(540,258),(740,258)],
    [(540,258),(540,282)], [(740,258),(740,282)],
    # 柱3
    [(1060,225),(1060,252)],
    [(1060,296),(1060,330)], [(990,330),(1150,330)],
    [(990,330),(990,356)], [(1150,330),(1150,356)],
    [(990,400),(990,426)], [(1150,400),(1150,426)], [(990,426),(1150,426)],
    [(1070,426),(1070,452)],
]
FLOW = [  # 矢印つき（順序・因果）
    [(740,326),(740,350)],
    [(740,396),(740,430)],
    [(740,476),(740,510)],
    [(740,556),(740,590)],
    [(1070,496),(1070,530)],
]

# ---------- 文字（問い・注記） ----------
TEXT = [  # (x, y, class, anchor, 文字列, フォントsize)
    (640, 76,  'criterion', 'middle', 'からだは何からできている？', 12),
    (220, 243, 'criterion', 'middle', '植物と動物でくらべると？', 12),
    (110, 502, 'criterion', 'middle', '葉の表皮に見られる細胞', 12),
    (640, 243, 'criterion', 'middle', '細胞はいくつ？', 12),
    (540, 272, 'answer',    'middle', '１つ', 11),
    (740, 272, 'answer',    'middle', '多く', 11),
    (540, 348, 'note-small','middle', '１つの細胞に、生命活動に', 11),
    (540, 366, 'note-small','middle', '必要なしくみが全てある', 11),
    (655, 414, 'chg-label', 'end',    '形やはたらきが同じものが集まる', 11),
    (655, 494, 'chg-label', 'end',    'いくつかが集まる', 11),
    (655, 574, 'chg-label', 'end',    'いくつかが集まる', 11),
    (1060, 316,'criterion', 'middle', '細胞の内部で起こる', 12),
    (1085, 514,'chg-label', 'start',  'エネルギーがとり出される', 11),
]

# ---------- 凡例 ----------
LEGEND = dict(x=950, y=640, w=300, h=100,
    items=[('node-main','label-main','中心となる語句',0,0), ('node-pink','','動物の細胞',1,0),
           ('node-yellow','','細胞のつくり',0,1),          ('node-orange','','からだの成り立ち',1,1),
           ('node-green','','植物の細胞',0,2),             ('node-blue','','はたらき',1,2)])

# ================= 検証 =================
def txt_w(s, fs):
    """日本語=全角1.0em、半角=0.55emでざっくり見積もる"""
    w = 0
    for ch in s:
        w += fs * (0.55 if ord(ch) < 0x2000 else 1.0)
    return w

errs = []
ids = list(N)
for a in range(len(ids)):
    for b in range(a+1, len(ids)):
        p, q = N[ids[a]], N[ids[b]]
        ax1, ax2 = p['cx']-p['w']/2, p['cx']+p['w']/2
        ay1, ay2 = p['cy']-p['h']/2, p['cy']+p['h']/2
        bx1, bx2 = q['cx']-q['w']/2, q['cx']+q['w']/2
        by1, by2 = q['cy']-q['h']/2, q['cy']+q['h']/2
        if ax1 < bx2 and bx1 < ax2 and ay1 < by2 and by1 < ay2:
            errs.append(f'ノード重なり: {ids[a]} x {ids[b]}')
        elif ax1 < bx2 and bx1 < ax2 and abs(ay1-by2) < 6 and abs(ay1-by2) > 0:
            errs.append(f'ノード隣接すぎ(縦{abs(ay1-by2):.0f}px): {ids[a]} x {ids[b]}')

for i, n in N.items():
    need = txt_w(n['label'], n['fs'])
    if need > n['w'] - 14:
        errs.append(f'ラベルが箱に入らない: {i} 「{n["label"]}」 必要{need:.0f}px > 箱{n["w"]-14}px')
    if n['cx']-n['w']/2 < 0 or n['cx']+n['w']/2 > VB_W or n['cy']-n['h']/2 < 0 or n['cy']+n['h']/2 > VB_H:
        errs.append(f'viewBoxはみ出し: {i}')

# 文字と箱の衝突
for (x, y, cls, anc, s, fs) in TEXT:
    w = txt_w(s, fs)
    x1 = x - w/2 if anc == 'middle' else (x - w if anc == 'end' else x)
    x2 = x1 + w
    y1, y2 = y - fs*0.6, y + fs*0.6
    if x1 < 0 or x2 > VB_W:
        errs.append(f'文字がviewBox外: 「{s}」')
    for i, n in N.items():
        nx1, nx2 = n['cx']-n['w']/2, n['cx']+n['w']/2
        ny1, ny2 = n['cy']-n['h']/2, n['cy']+n['h']/2
        if x1 < nx2 and nx1 < x2 and y1 < ny2 and ny1 < y2:
            errs.append(f'文字がノードに重なる: 「{s}」 x {i}')

print('--- 自動検査 ---')
print('\n'.join(errs) if errs else 'エラーなし（ノード重なり・ラベル溢れ・はみ出し・文字衝突すべて0件）')
print(f'ノード数 {len(N)} / 線 {len(LINK)+len(FLOW)} / 文字 {len(TEXT)}')
if errs:
    sys.exit(1)

# ================= SVG 生成 =================
def rect(n):
    return (f'  <rect class="{n["ncls"]}" x="{n["cx"]-n["w"]/2:g}" y="{n["cy"]-n["h"]/2:g}" '
            f'width="{n["w"]:g}" height="{n["h"]:g}" rx="9"/>\n'
            f'  <text class="label {n["lcls"]}" x="{n["cx"]:g}" y="{n["cy"]:g}" '
            f'style="font-size:{n["fs"]}px">{n["label"]}</text>')

svg = [f'<div class="svg-scroll"><svg viewBox="0 0 {VB_W} {VB_H}" xmlns="http://www.w3.org/2000/svg">',
       '  <defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#444"/></marker></defs>']
for pts in LINK:
    svg.append('  <polyline class="link" points="' + ' '.join(f'{x},{y}' for x, y in pts) + '"/>')
for pts in FLOW:
    svg.append('  <polyline class="flow" marker-end="url(#ar)" points="' + ' '.join(f'{x},{y}' for x, y in pts) + '"/>')
for i in N:
    svg.append(rect(N[i]))
for (x, y, cls, anc, s, fs) in TEXT:
    svg.append(f'  <text class="{cls}" x="{x}" y="{y}" style="text-anchor:{anc};font-size:{fs}px">{s}</text>')
L = LEGEND
svg.append(f'  <rect x="{L["x"]}" y="{L["y"]}" width="{L["w"]}" height="{L["h"]}" rx="8" style="fill:#fafafa;stroke:#ccc;stroke-width:1;"/>')
svg.append(f'  <text x="{L["x"]+L["w"]/2:g}" y="{L["y"]+16}" style="font-size:11px;fill:#666;text-anchor:middle;font-weight:bold;">凡例</text>')
for (ncls, _lc, lab, col, row) in L['items']:
    sx = L['x'] + 20 + col*140
    sy = L['y'] + 30 + row*22
    svg.append(f'  <rect class="{ncls}" x="{sx}" y="{sy}" width="18" height="13" rx="3"/>')
    svg.append(f'  <text x="{sx+24}" y="{sy+7}" style="font-size:11px;fill:#555;dominant-baseline:central;">{lab}</text>')
svg.append('</svg></div>')
SVG = '\n'.join(svg)

# ================= まとめ文・語句 =================
def bl(w):
    return f'<span class="blank">{w}</span>'

SUMMARY = f"""  生物のからだは、すべて {bl('細胞')} からできている。<br>
  細胞を顕微鏡で観察すると、{bl('植物の細胞')} にも {bl('動物の細胞')} にも {bl('核')}・{bl('細胞膜')}・{bl('細胞質')} が見られる。
  いっぽう {bl('細胞壁')}・{bl('葉緑体')}・{bl('液胞')} は {bl('植物の細胞')} だけに見られ、葉の表皮には三日月形をした {bl('孔辺細胞')} がある。<br>
  からだが１つの細胞からできている生物を {bl('単細胞生物')}、多くの細胞からできている生物を {bl('多細胞生物')} という。<br>
  {bl('多細胞生物')} では、形やはたらきが同じ {bl('細胞')} が集まって {bl('組織')} をつくり、いくつかの {bl('組織')} が集まって特定のはたらきをする {bl('器官')} となり、いくつかの {bl('器官')} が集まって {bl('個体')} となる。<br>
  細胞の内部では、{bl('酸素')} が使われて {bl('養分（有機物）')} が {bl('分解')} され、{bl('エネルギー')} がとり出される。このはたらきを {bl('細胞の呼吸')} という。"""

WORDS = ['細胞','植物の細胞','動物の細胞','核','細胞膜','細胞質','細胞壁','葉緑体','液胞','孔辺細胞',
         '単細胞生物','多細胞生物','組織','器官','個体','細胞の呼吸','酸素','養分（有機物）','分解','エネルギー']
CARDS = '\n'.join(f'    <div class="word-card">{w}</div>' for w in WORDS)

# 必須語句がマップ上に全部あるか照合
labels = {n['label'] for n in N.values()}
missing = [w for w in WORDS if w not in labels]
print('必須20語のうちマップ上に無いもの:', missing if missing else 'なし')
if missing:
    sys.exit(1)

CSS = """@page { size: A4 landscape; margin: 10mm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: "UD デジタル 教科書体 NP-B", "Hiragino Maru Gothic ProN", "Meiryo", sans-serif;
  background: white; color: #222; padding: 12px 16px;
}
.wrap { max-width: 1280px; margin: 0 auto; }
h1 {
  font-size: 18px; text-align: center; color: #222; padding-bottom: 6px;
  border-bottom: 2px solid #222; margin-bottom: 10px; letter-spacing: 0.08em;
}
.meta { text-align: center; font-size: 12px; color: #888; margin-bottom: 12px; }
svg { display: block; margin: 0 auto; width: 100%; height: auto; max-width: 1280px; }

.node { fill: white; stroke: #222; stroke-width: 1.6; }
.node-main { fill: #fff9ec; stroke: #222; stroke-width: 2.5; }
.node-yellow { fill: #fff4c2; stroke: #C8961E; stroke-width: 2; }
.node-green { fill: #d8f3dc; stroke: #2E7D32; stroke-width: 2; }
.node-pink { fill: #ffe3ec; stroke: #D63384; stroke-width: 2; }
.node-orange { fill: #ffe8d0; stroke: #E65100; stroke-width: 2; }
.node-blue { fill: #dceefb; stroke: #1565C0; stroke-width: 2; }

.label { font-family: inherit; font-size: 15px; fill: #222; text-anchor: middle; dominant-baseline: central; }
.label-main { font-weight: bold; }
.label-leaf { font-weight: bold; }
.label-yellow { fill: #6b4a00; }
.label-green { fill: #1b5e20; }
.label-pink { fill: #b03856; }
.label-orange { fill: #8c3d00; }
.label-blue { fill: #0d4c8f; }

.criterion { fill: #555; text-anchor: middle; dominant-baseline: central; font-style: italic; font-weight: bold; }
.answer { fill: #888; text-anchor: middle; dominant-baseline: central; }
.note-small { fill: #666; text-anchor: middle; dominant-baseline: central; }
.chg-label { fill: #777; dominant-baseline: central; }
.link { stroke: #222; stroke-width: 1.4; fill: none; }
.flow { stroke: #444; stroke-width: 1.6; fill: none; }

.summary { margin-top: 16px; padding: 12px 16px; border: 1.5px solid #222; font-size: 13px; line-height: 2.0; }
.summary strong { display: block; margin-bottom: 4px; font-size: 14px; }
.summary .blank {
  display: inline-block; border-bottom: 1.5px solid #222; min-width: 70px;
  text-align: center; padding: 0 6px; color: #666; font-size: 12px;
}
.back-btn, .words-btn, .print-btn {
  display: inline-block; padding: 4px 14px; color: white; border: none; border-radius: 14px;
  text-decoration: none; font-family: inherit; font-size: 12px; font-weight: bold;
  margin-left: 8px; vertical-align: middle; cursor: pointer;
}
.back-btn { background: #74c69d; } .back-btn:hover { background: #57b387; }
.words-btn { background: #f0a000; } .words-btn:hover { background: #d68a00; }
.print-btn { background: #D63384; }
.words-only { margin-top: 24px; padding: 28px 24px 50px; text-align: center; background: #fff8e8; border: 2px dashed #e8c84a; border-radius: 16px; }
.words-only h2 { font-size: 20px; margin-bottom: 8px; color: #946800; }
.words-only .hint { color: #886a3a; font-size: 13px; margin-bottom: 26px; line-height: 1.7; }
.words-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 14px; max-width: 820px; margin: 0 auto; }
.word-card { background: #fff4c2; border: 2px solid #e8c84a; border-radius: 12px; padding: 18px 10px; font-size: 17px; font-weight: bold; color: #6b4a00; box-shadow: 0 2px 4px rgba(216,173,105,0.2); }
@media print { .print-btn, .back-btn, .words-btn, .words-only { display: none; } body { padding: 0; } }
.svg-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; max-width: 100%; margin: 0 auto; }
@media (max-width: 600px) {
  body { padding: 8px 6px; }
  h1 { font-size: 14px; line-height: 1.6; letter-spacing: 0.03em; }
  .meta { font-size: 11px; margin-bottom: 8px; }
  .back-btn, .words-btn, .print-btn { padding: 4px 10px; font-size: 11px; margin-left: 4px; margin-top: 6px; }
  svg { min-width: 940px; }
  .summary { font-size: 12px; padding: 10px 12px; line-height: 1.9; }
  .words-grid { gap: 8px; grid-template-columns: repeat(auto-fill, minmax(95px, 1fr)); }
  .word-card { font-size: 14px; padding: 12px 6px; }
}"""

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>生物と細胞まとめ（完成見本）｜まとめマップ</title>
<meta property="og:title" content="生物と細胞まとめ（完成見本）｜まとめマップ">
<meta property="og:description" content="中2理科 生物1章「生物と細胞」P.92-103 の全体まとめマップ完成見本。パフォーマンステストの答え合わせ用。">
<meta property="og:type" content="article">
<style>
{CSS}
</style>
</head>
<body>
<div class="wrap">

<h1>生物と細胞まとめ（完成見本）｜まとめマップ <a href="index.html" class="back-btn">📋 一覧へ</a><button class="words-btn" onclick="toggleWords(this)">📝 語句のみ</button><button class="print-btn" onclick="window.print()">🖨 印刷</button></h1>
<div class="meta">中2理科 生物1章「生物と細胞」P.92-103 ／ パフォーマンステストの見本（答え）</div>

{SVG}

<div class="summary">
  <strong>📝 まとめ文（マップを矢印の順になぞって書こう）</strong>
{SUMMARY}
</div>

<div class="words-only" hidden>
  <h2>📝 語句チェック</h2>
  <p class="hint">この語句が、マップのどこにあって、どうつながっていたか思い出せるかな？</p>
  <div class="words-grid">
{CARDS}
  </div>
</div>

<script>
function toggleWords(btn) {{
  const svg = document.querySelector('.svg-scroll');
  const summary = document.querySelector('.summary');
  const words = document.querySelector('.words-only');
  if (words.hidden) {{
    svg.style.display = 'none';
    summary.style.display = 'none';
    words.hidden = false;
    btn.textContent = '🗺️ マップへ戻る';
  }} else {{
    svg.style.display = '';
    summary.style.display = '';
    words.hidden = true;
    btn.textContent = '📝 語句のみ';
  }}
}}
</script>

</div>
</body>
</html>
"""

OUT = r'C:\Users\marar\Documents\MSTbase\education\matome-maps\chu2-p92-103-saibou-zentai-full.html'
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)
print('保存:', OUT, f'({len(HTML)} bytes)')
