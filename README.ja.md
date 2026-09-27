# Codex Working Agreements

[English](README.md)

Codexを慎重かつ再現可能に、そして処理を際限なく重くせず運用するための、
実践的で意見を持った設定例です。

このリポジトリでは、恒久ルール、段階的に読む手続き、外部状態を分離しています。

- `AGENTS.md`：ほぼすべてのタスクに適用する恒久的な作業上の合意
- `.agents/skills/<name>/SKILL.md`：必要な場合だけ読み込むタスク固有の手続き
- `HANDOFF.md`、Git、検証スクリプト、レポート：現在状態、履歴、機械的制約、
  証拠をpersistent promptの外に保持

中心となる判断基準は次のとおりです。

> minimal persistent context + progressive disclosure + durable external state + explicit validation

すべてのタスクを最大限に重くすることが目的ではありません。必要十分な手順を
選び、ユーザーの作業を守り、不確実性を明示し、リスクに応じて検証し、依頼の
達成条件を満たしたら停止することを目指しています。

## 構成

```text
.
├── AGENTS.md
├── docs/
│   ├── CONTEXT_ARCHITECTURE.md
│   ├── MIGRATION_REPORT.md
│   └── EVAL_PROPOSAL.md
├── scripts/
│   └── validate_repository.py
└── .agents/
    └── skills/
        ├── research/
        │   ├── SKILL.md
        │   ├── references/
        │   └── assets/
        ├── experience-promotion/
        │   ├── SKILL.md
        │   ├── references/
        │   └── assets/
        ├── multidisciplinary-review/
        │   ├── SKILL.md
        │   └── references/
        └── local-first-app-development/
            └── SKILL.md
```

## 収録Skill

### Research

文献調査、新規性評価、数学・計算・実証研究、Verification、Critical Review、
出版・再現性、復旧を振り分ける薄いルーターです。現在の判断に影響するreferenceだけを
読み込みます。

検証済みの証拠、推論、仮説、仮定、未解決の不確実性を区別し、調査の上限、
人間による確認事項、完了条件を定めています。

### Experience Promotion

重要な経験だけを、必要最小限の恒久的な介入へ昇格させるためのワークフローです。

通常の成功や一度限りのノイズは対象外です。重要な経験は分類、検証、重複排除、圧縮を
行い、必要十分な最小範囲へ配置します。重複・反証・陳腐化・modelの進歩に応じて、
既存指示の統合、降格、archive、削除も扱います。

### Multidisciplinary Review

重要な意思決定、研究フロンティアの問い、またはトッププロによる複眼的なレビューを
明示的に求められた場合のための、選択的な分野横断ワークフローです。

著名人の人物模倣ではなく、科学的発見、哲学、戦略・システム、創業者・経営者、
AI・機械学習・クラウドの評価レンズへ変換します。結論に影響するレンズだけを読み、
対立を残したまま統合し、権威に依存せず検証、推奨、または次の行動へつなげます。

### Local-First App Development

アプリやゲームの公開範囲を守るためのワークフローです。開発、テスト、プレビューは
既定でローカルに限定し、デプロイや配布には公開先とリリース範囲を明示した依頼を
必要とします。意図せずオンライン公開した場合には、アクセス制限と検証済みの削除を
区別して後処理します。

## 利用方法

まずcloneし、導入前に内容を確認してください。

```sh
git clone https://github.com/t-ymbys/codex-working-agreements.git
cd codex-working-agreements
```

このリポジトリ内でCodexを実行すると、ルートの `AGENTS.md` と
`.agents/skills` 以下のSkillをリポジトリスコープで利用できます。

個人用の横断設定として使う場合は、必要な部分だけを次の場所へ統合します。

```text
~/.codex/AGENTS.md
~/.agents/skills/<skill-name>/
```

既存設定を無条件に上書きしないでください。差分を確認し、自分の環境に合わせ、
代表的なタスクで挙動を検証してください。

リポジトリの機械検証は次で実行できます。

```sh
python3 scripts/validate_repository.py
```

設計と証拠の境界は、[Context Architecture](docs/CONTEXT_ARCHITECTURE.md)、
[Migration Report](docs/MIGRATION_REPORT.md)、
[Evaluation Proposal](docs/EVAL_PROPOSAL.md)を参照してください。

## 状態と制約

- OpenAI公式プロジェクトではなく、個人の作業設定です。
- Skillは作者の環境で構造、frontmatter、リンク、sensitive patternの静的検証を
  通過しています。
- 記載したリポジトリ用・ユーザー用Skillのパスは、現在のCodex公式ドキュメントと
  照合しています。行動上の有効性は、対照実験ではまだ検証していません。
- 一部の規則は意図的に保守的で、使い捨ての試作には重すぎる場合があります。
- Codexの更新によりパスや挙動が変わる可能性があります。環境依存事項は最新の
  公式ドキュメントを確認してください。

## スナップショットの由来

このリポジトリは、2026-09-27にレビューした作者の現用設定をサニタイズした
スナップショットです。可変メモリ、タスク履歴、認証情報、ローカル設定、非公開の
研究成果物は含みません。

## ライセンス

[MIT](LICENSE)
