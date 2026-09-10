# セッション引き継ぎメモ
更新：2026-06-12（酸化マップ完成＋「揺れ」の正体＝ジャンクションを特定）

## 🔴🔴 最優先：この環境は「揺れる」。git を唯一の信頼源にする
`C:\Users\marar\MSTbase` は **JUNCTION** で、実体は `C:\Users\marar\OneDrive\Documents\MSTbase`（Documents 自体も OneDrive リダイレクト）。
→ **MSTbase / Documents\MSTbase / OneDrive\Documents\MSTbase の3パスが同一実体**。このせいで：
- 素の Read / grep / 画像Read / working tree が **矛盾した結果・空・旧版への巻き戻り** を起こす
- 毎回 `Shell cwd was reset to C:\Users\marar\MSTbase`／画像Read は corrupted

**対処（必ず守る）:**
- 読む → `git show HEAD:<file>`（素の Read/grep を信用しない）
- 書く → Write/heredoc → **即 `git add -f` & commit（公開まで要るなら即 push）を同一 Bash コマンドで**。ターンを跨ぐと消える。heredoc は JS 内をダブルクオートにする
- 検証 → `wc -l` / `grep -c` の**客観数値**で、working tree と `git show HEAD:` の一致を見る
- 画像 → headless Chrome で PNG 生成 → **ユーザーに `file://` で開いてもらう**（撮影は1880px、座標はコードtrace）
- 一時ファイルは **`C:/tmp/`**（Git Bash の `/tmp` は Windows python から見えない）
- 確認コマンド：`cmd //c "dir C:\Users\marar" | grep -i mstbase` → `<JUNCTION>` 表示
- 詳細はメモリ env_mstbase_junction_onedrive.md（MEMORY.md からロードされる）

## ✅ 今日(2026-06-12)完了したこと
- **酸化を防ぐくふう まとめマップ** `chu2-p55-sanka-wo-fusegu.html`（中2化学・発展）を新規作成・公開
  - スタート画面(2ボタン)＋語句カード18＋3ボタン＋穴埋め。内容は**定番版**（教科書P55に該当が無く、さび止め＋食品の酸化防止でドラフト＝**要・教科書照合**）
  - matome-maps push済(main=080ada3)、index 登録（中2化学・全2マップ・全17）
  - edu-box push済(master=4d27e78)、まとめマップ一覧に酸化カード追加
  - 公開URL: https://mararararai-mst.github.io/matome-maps/chu2-p55-sanka-wo-fusegu.html
- 前回🔴の **未pushの24マップ → push済(matome-maps f9c3137)で解消**
- **まとめマップ SKILL.md に「揺れる環境＝git基盤」堅牢化セクションを追記**
- メモリに環境の罠を記録

## ⏳ 残務（手作業・未確認）
- 配布物の **SharePoint アップ**（パフォーマンステスト docx/pdf 等）＝ユーザー手作業
- 酸化マップ内容を**教科書P55実物と照合**（写真をもらえれば差し替え）

## スキルの状態
- まとめマップスキルは **健全**（add_start_screen 等は正常）。今日の混乱は全て環境（ジャンクション）が原因だった
- 場所：`C:\Users\marar\.claude\skills\まとめマップ\`（.claude 配下＝OneDrive外＝揺れない）

## 触らないファイル
- このメモ自身、worksheet 類・語句カード.xlsx（配布物・未追跡）
