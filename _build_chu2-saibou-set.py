# -*- coding: utf-8 -*-
"""中2 生物1章「生物と細胞」全体まとめマップを3段階で生成する。
  goku … 語句だけ（A4縦・白紙に自分で組む）
  waku … 枠あり（A3横・空の枠に語句を書きこむ）
  full … 完成見本（A4横・答え）
既存の全体ツリー chu1-p43-44-shokubutsu-zentai-bunrui.html の様式を踏襲。"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

VB_W, VB_H = 1280, 760
OUTDIR = r'C:\Users\marar\Documents\MSTbase\education\matome-maps'

# ---------- ノード定義 ----------
N = {}
def node(i, label, cx, cy, w, h, ncls, lcls, fs=15):
    N[i] = dict(label=label, cx=cx, cy=cy, w=w, h=h, ncls=ncls, lcls=lcls, fs=fs)

node('karada', '生物のからだ', 640, 40, 220, 46, 'node-main', 'label-main', 17)
node('saibou', '細胞',        640, 110, 150, 44, 'node-main', 'label-main', 17)
node('h_tsuku', '細胞のつくり',     220, 204, 200, 42, 'node-yellow', 'label-leaf label-yellow')
node('h_nari',  'からだの成り立ち', 640, 204, 220, 42, 'node-orange', 'label-leaf label-orange')
node('h_hata',  '細胞のはたらき',   1060, 204, 210, 42, 'node-blue',  'label-leaf label-blue')
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
node('tan', '単細胞生物', 540, 304, 170, 44, 'node-orange', 'label-leaf label-orange')
node('ta',  '多細胞生物', 740, 304, 170, 44, 'node-orange', 'label-leaf label-orange')
node('c1',  '細胞', 740, 374, 150, 44, 'node-orange', 'label-leaf label-orange')
node('c2',  '組織', 740, 454, 150, 44, 'node-orange', 'label-leaf label-orange')
node('c3',  '器官', 740, 534, 150, 44, 'node-orange', 'label-leaf label-orange')
node('c4',  '個体', 740, 614, 150, 44, 'node-orange', 'label-leaf label-orange')
node('kokyu', '細胞の呼吸',   1060, 274, 190, 44, 'node-blue', 'label-leaf label-blue')
node('san',   '酸素',          990, 378, 120, 44, 'node-blue', 'label-leaf label-blue')
node('yobun', '養分（有機物）',1150, 378, 190, 44, 'node-blue', 'label-leaf label-blue')
node('bunkai','分解',         1070, 474, 140, 44, 'node-blue', 'label-leaf label-blue')
node('ene',   'エネルギー',   1070, 554, 180, 44, 'node-blue', 'label-leaf label-blue')

LINK = [
    [(640,63),(640,88)], [(640,132),(640,158)], [(220,158),(1060,158)],
    [(220,158),(220,183)], [(640,158),(640,183)], [(1060,158),(1060,183)],
    [(220,225),(220,258)], [(110,258),(330,258)],
    [(110,258),(110,282)], [(330,258),(330,282)],
    [(110,326),(110,352)], [(330,326),(330,352)], [(110,352),(330,352)], [(220,352),(220,360)],
    [(220,404),(220,420)], [(110,420),(330,420)],
    [(110,420),(110,438)], [(220,420),(220,438)], [(330,420),(330,438)],
    [(30,304),(18,304),(18,594)],
    [(18,516),(45,516)], [(18,594),(30,594)],
    [(110,638),(110,656)], [(60,656),(280,656)],
    [(60,656),(60,672)], [(170,656),(170,672)], [(280,656),(280,672)],
    [(640,225),(640,258)], [(540,258),(740,258)],
    [(540,258),(540,282)], [(740,258),(740,282)],
    [(1060,225),(1060,252)],
    [(1060,296),(1060,330)], [(990,330),(1150,330)],
    [(990,330),(990,356)], [(1150,330),(1150,356)],
    [(990,400),(990,426)], [(1150,400),(1150,426)], [(990,426),(1150,426)],
    [(1070,426),(1070,452)],
]
FLOW = [
    [(740,326),(740,350)], [(740,396),(740,430)], [(740,476),(740,510)],
    [(740,556),(740,590)], [(1070,496),(1070,530)],
]
TEXT = [
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
LEGEND = dict(x=950, y=640, w=300, h=100,
    items=[('node-main','中心となる語句',0,0), ('node-pink','動物の細胞',1,0),
           ('node-yellow','細胞のつくり',0,1),  ('node-orange','からだの成り立ち',1,1),
           ('node-green','植物の細胞',0,2),     ('node-blue','はたらき',1,2)])

WORDS = ['細胞','植物の細胞','動物の細胞','核','細胞膜','細胞質','細胞壁','葉緑体','液胞','孔辺細胞',
         '単細胞生物','多細胞生物','組織','器官','個体','細胞の呼吸','酸素','養分（有機物）','分解','エネルギー']
SHOU_Q = '多様な生物の間に見られる共通点は何だろうか。'   # 教科書P104 Before & After
# 骨組みのラベル（必須20語ではない）。枠あり版でも印字して手がかりにする
SCAFFOLD = {'karada','h_tsuku','h_nari','h_hata','kyotsu','sdake'}

# ================= 検証 =================
def txt_w(s, fs):
    return sum(fs * (0.55 if ord(c) < 0x2000 else 1.0) for c in s)

errs = []
ids = list(N)
for a in range(len(ids)):
    for b in range(a+1, len(ids)):
        p, q = N[ids[a]], N[ids[b]]
        ax1, ax2, ay1, ay2 = p['cx']-p['w']/2, p['cx']+p['w']/2, p['cy']-p['h']/2, p['cy']+p['h']/2
        bx1, bx2, by1, by2 = q['cx']-q['w']/2, q['cx']+q['w']/2, q['cy']-q['h']/2, q['cy']+q['h']/2
        if ax1 < bx2 and bx1 < ax2 and ay1 < by2 and by1 < ay2:
            errs.append(f'ノード重なり: {ids[a]} x {ids[b]}')
for i, n in N.items():
    if txt_w(n['label'], n['fs']) > n['w'] - 14:
        errs.append(f'ラベル溢れ: {i}')
    if n['cx']-n['w']/2 < 0 or n['cx']+n['w']/2 > VB_W or n['cy']+n['h']/2 > VB_H:
        errs.append(f'はみ出し: {i}')
for (x, y, cls, anc, s, fs) in TEXT:
    w = txt_w(s, fs)
    x1 = x - w/2 if anc == 'middle' else (x - w if anc == 'end' else x)
    x2, y1, y2 = x1 + w, y - fs*0.6, y + fs*0.6
    for i, n in N.items():
        nx1, nx2 = n['cx']-n['w']/2, n['cx']+n['w']/2
        ny1, ny2 = n['cy']-n['h']/2, n['cy']+n['h']/2
        if x1 < nx2 and nx1 < x2 and y1 < ny2 and ny1 < y2:
            errs.append(f'文字がノードに重なる: 「{s}」 x {i}')
missing = [w for w in WORDS if w not in {n['label'] for n in N.values()}]
if missing:
    errs.append(f'必須語がマップに無い: {missing}')
print('--- 幾何検査 ---')
print('\n'.join(errs) if errs else 'エラーなし（重なり・溢れ・はみ出し・必須20語の配置）')
if errs:
    sys.exit(1)

# ================= SVG =================
def make_svg(mode):
    """mode: 'full'=語句あり / 'waku'=枠だけ（塗りなし・語句なし）"""
    s = [f'<div class="svg-scroll"><svg viewBox="0 0 {VB_W} {VB_H}" xmlns="http://www.w3.org/2000/svg">',
         '  <defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#444"/></marker></defs>']
    for pts in LINK:
        s.append('  <polyline class="link" points="' + ' '.join(f'{x},{y}' for x, y in pts) + '"/>')
    for pts in FLOW:
        s.append('  <polyline class="flow" marker-end="url(#ar)" points="' + ' '.join(f'{x},{y}' for x, y in pts) + '"/>')
    for i, n in N.items():
        # 枠あり版は白黒印刷で書きこめるよう塗りを白にする
        style = ' style="fill:#ffffff"' if mode == 'waku' else ''
        s.append(f'  <rect class="{n["ncls"]}" x="{n["cx"]-n["w"]/2:g}" y="{n["cy"]-n["h"]/2:g}" '
                 f'width="{n["w"]:g}" height="{n["h"]:g}" rx="9"{style}/>')
        if mode == 'full' or i in SCAFFOLD:
            s.append(f'  <text class="label {n["lcls"]}" x="{n["cx"]:g}" y="{n["cy"]:g}" '
                     f'style="font-size:{n["fs"]}px">{n["label"]}</text>')
    for (x, y, cls, anc, s2, fs) in TEXT:
        s.append(f'  <text class="{cls}" x="{x}" y="{y}" style="text-anchor:{anc};font-size:{fs}px">{s2}</text>')
    if mode == 'full':
        L = LEGEND
        s.append(f'  <rect x="{L["x"]}" y="{L["y"]}" width="{L["w"]}" height="{L["h"]}" rx="8" style="fill:#fafafa;stroke:#ccc;stroke-width:1;"/>')
        s.append(f'  <text x="{L["x"]+L["w"]/2:g}" y="{L["y"]+16}" style="font-size:11px;fill:#666;text-anchor:middle;font-weight:bold;">凡例</text>')
        for (ncls, lab, col, row) in L['items']:
            sx, sy = L['x'] + 20 + col*140, L['y'] + 30 + row*22
            s.append(f'  <rect class="{ncls}" x="{sx}" y="{sy}" width="18" height="13" rx="3"/>')
            s.append(f'  <text x="{sx+24}" y="{sy+7}" style="font-size:11px;fill:#555;dominant-baseline:central;">{lab}</text>')
    s.append('</svg></div>')
    return '\n'.join(s)

def summary_html(mode):
    def bl(w):
        return f'<span class="blank">{w}</span>' if mode == 'full' else '<span class="blank">　</span>'
    return f"""  生物のからだは、すべて {bl('細胞')} からできている。<br>
  細胞を顕微鏡で観察すると、{bl('植物の細胞')} にも {bl('動物の細胞')} にも {bl('核')}・{bl('細胞膜')}・{bl('細胞質')} が見られる。
  いっぽう {bl('細胞壁')}・{bl('葉緑体')}・{bl('液胞')} は {bl('植物の細胞')} だけに見られ、葉の表皮には三日月形をした {bl('孔辺細胞')} がある。<br>
  からだが１つの細胞からできている生物を {bl('単細胞生物')}、多くの細胞からできている生物を {bl('多細胞生物')} という。<br>
  {bl('多細胞生物')} では、形やはたらきが同じ {bl('細胞')} が集まって {bl('組織')} をつくり、いくつかの {bl('組織')} が集まって特定のはたらきをする {bl('器官')} となり、いくつかの {bl('器官')} が集まって {bl('個体')} となる。<br>
  細胞の内部では、{bl('酸素')} が使われて {bl('養分（有機物）')} が {bl('分解')} され、{bl('エネルギー')} がとり出される。このはたらきを {bl('細胞の呼吸')} という。"""

def cards(cls='word-card'):
    return '\n'.join(f'    <div class="{cls}">{w}</div>' for w in WORDS)

# ================= CSS =================
BASE_CSS = """* { box-sizing: border-box; margin: 0; padding: 0; }
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
.label-yellow { fill: #6b4a00; } .label-green { fill: #1b5e20; } .label-pink { fill: #b03856; }
.label-orange { fill: #8c3d00; } .label-blue { fill: #0d4c8f; }
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
.svg-scroll { overflow-x: auto; -webkit-overflow-scrolling: touch; max-width: 100%; margin: 0 auto; }
@media print { .print-btn, .back-btn, .words-btn { display: none; } body { padding: 0; } }
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

# 枠あり用の追加（白黒印刷で書きこめるよう塗りを消す・語句バンク）
WAKU_CSS = """.bank { margin-top: 14px; padding: 14px 18px 18px; border: 2px dashed #888; border-radius: 12px; }
.bank h2 { font-size: 14px; margin-bottom: 4px; }
.bank .hint { font-size: 11.5px; color: #666; margin-bottom: 12px; }
.bank .words-grid { grid-template-columns: repeat(auto-fill, minmax(115px, 1fr)); gap: 9px; max-width: none; }
.bank .word-card { background: #fff; border: 1.6px solid #555; color: #222; box-shadow: none; padding: 9px 6px; font-size: 14px; }
.summary .blank { min-width: 96px; }
@media print { .svg-scroll svg { width: auto; max-height: 198mm; } }"""

GOKU_CSS = """.lead { max-width: 640px; margin: 0 auto 22px; font-size: 13.5px; line-height: 2.0; color: #444; }
.q-box { max-width: 640px; margin: 0 auto 24px; padding: 14px 18px; border: 2px solid #222; border-radius: 12px; text-align: center; }
.q-box .q-lab { font-size: 12px; color: #888; letter-spacing: .1em; display: block; margin-bottom: 6px; }
.q-box .q-txt { font-size: 15.5px; font-weight: bold; line-height: 1.8; }
.words-grid { grid-template-columns: repeat(auto-fill, minmax(155px, 1fr)); gap: 18px; max-width: 680px; }
.word-card { padding: 25px 10px; font-size: 19px; }
.foot { max-width: 660px; margin: 26px auto 0; font-size: 12px; color: #666; line-height: 1.9; }"""

def page(title, ogdesc, page_css, h1, meta, body, extra_css='', script='', extra_btn=''):
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta property="og:title" content="{title}">
<meta property="og:description" content="{ogdesc}">
<meta property="og:type" content="article">
<style>
{page_css}
{BASE_CSS}
{extra_css}
</style>
</head>
<body>
<div class="wrap">

<h1>{h1} <a href="index.html" class="back-btn">📋 一覧へ</a>{extra_btn}<button class="print-btn" onclick="window.print()">🖨 印刷</button></h1>
<div class="meta">{meta}</div>

{body}

</div>
{script}
</body>
</html>
"""

TOGGLE_JS = """<script>
function toggleWords(btn) {
  const svg = document.querySelector('.svg-scroll');
  const summary = document.querySelector('.summary');
  const words = document.querySelector('.words-only');
  if (words.hidden) {
    svg.style.display = 'none'; summary.style.display = 'none';
    words.hidden = false; btn.textContent = '\\u{1F5FA}\\u{FE0F} マップへ戻る';
  } else {
    svg.style.display = ''; summary.style.display = '';
    words.hidden = true; btn.textContent = '\\u{1F4DD} 語句のみ';
  }
}
</script>"""

# ---------- 1) 語句だけ ----------
goku_body = f"""<div class="q-box">
  <span class="q-lab">この章の問い</span>
  <span class="q-txt">{SHOU_Q}</span>
</div>

<p class="lead">
  下の <b>20の語句</b> を、関係のあるものどうし線でつないで、<br>
  自分のノートに <b>1枚のまとめマップ</b> を組み立てよう。<br>
  つなぐ線には「なぜそうつながるのか」も書きこめるといい。
</p>

<div class="words-grid">
{cards()}
</div>

<p class="foot">
  ・語句は何回使ってもかまいません。ここに無い語句を書き加えるのもOKです。<br>
  ・組み立てたら、マップを矢印の順になぞって「まとめ文」を書いてみよう。
</p>"""

# ---------- 2) 枠あり ----------
waku_body = f"""{make_svg('waku')}

<div class="bank">
  <h2>📝 使う語句（20）</h2>
  <p class="hint">※ 何回つかってもかまいません。ここに無い語句を書き加えるのもOK。</p>
  <div class="words-grid">
{cards()}
  </div>
</div>

<div class="summary">
  <strong>📝 まとめ文（マップを矢印の順になぞって書こう）</strong>
{summary_html('waku')}
</div>"""

# ---------- 3) 完成見本 ----------
full_body = f"""{make_svg('full')}

<div class="summary">
  <strong>📝 まとめ文（マップを矢印の順になぞって書こう）</strong>
{summary_html('full')}
</div>

<div class="words-only" hidden>
  <h2>📝 語句チェック</h2>
  <p class="hint">この語句が、マップのどこにあって、どうつながっていたか思い出せるかな？</p>
  <div class="words-grid">
{cards()}
  </div>
</div>"""

FILES = [
 ('chu2-p92-103-saibou-zentai-goku.html',
  page('生物と細胞まとめ（語句だけ）｜まとめマップ',
       '中2理科 生物1章「生物と細胞」P.92-103 の必須20語。白紙のノートに自分でまとめマップを組み立てるための語句だけの版。',
       '@page { size: A4 portrait; margin: 14mm; }',
       '生物と細胞まとめ（語句だけ）｜まとめマップ',
       '中2理科 生物1章「生物と細胞」P.92-103 ／ Lv1 自分で組み立てる',
       goku_body, GOKU_CSS)),
 ('chu2-p92-103-saibou-zentai-waku.html',
  page('生物と細胞まとめ（枠あり・書きこみ用）｜まとめマップ',
       '中2理科 生物1章「生物と細胞」P.92-103 の枠あり版。空の枠に語句を書きこんで、まとめマップを完成させる。',
       '@page { size: A3 landscape; margin: 10mm; }',
       '生物と細胞まとめ（枠あり）｜まとめマップ',
       '中2理科 生物1章「生物と細胞」P.92-103 ／ Lv2 枠に語句を書きこむ',
       waku_body, WAKU_CSS)),
 ('chu2-p92-103-saibou-zentai-full.html',
  page('生物と細胞まとめ（完成見本）｜まとめマップ',
       '中2理科 生物1章「生物と細胞」P.92-103 の全体まとめマップ完成見本。パフォーマンステストの答え合わせ用。',
       '@page { size: A4 landscape; margin: 10mm; }',
       '生物と細胞まとめ（完成見本）｜まとめマップ',
       '中2理科 生物1章「生物と細胞」P.92-103 ／ Lv3 見本（答え）',
       full_body, '', TOGGLE_JS,
       '<button class="words-btn" onclick="toggleWords(this)">📝 語句のみ</button>')),
]

import os
print('--- 出力 ---')
for name, html in FILES:
    with open(os.path.join(OUTDIR, name), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  {name}  ({len(html)} bytes)')

# 内容照合
print('--- 内容照合 ---')
for name, html in FILES:
    n_word = sum(html.count(f'>{w}</div>') for w in WORDS)
    n_rect = html.count('<rect class="node')
    n_lab  = html.count('<text class="label')
    print(f'  {name}: 語句カード{n_word} / 枠{n_rect} / 枠内ラベル{n_lab}')
