# Codex Agent Operating System

[English](README.md)

Codexの運用資産を、versioned・testable・installable・auditableな小さなAgent OSとして管理するrepositoryです。

以下を分離します。

- **Cognitive Control:** global/project AGENTS、progressive disclosure型Skills、研究epistemics、HANDOFF、Experience Promotion
- **Execution Control:** privateなmachine設定を保持したまま使えるapproval・sandbox・network・reasoning profile
- **Durable State:** Git、HANDOFF、再構築可能なproject artifacts
- **Deterministic Control:** validation、installation、doctor、rollback、plugin packaging
- **Distribution:** MCP・hooks・credentials・個人設定を含まないSkill-only portable plugin

設計原理は次のとおりです。

> minimal persistent context + progressive disclosure + least privilege + durable external state + explicit validation

## 構成

```text
.
├── AGENTS.md                    # repository-local開発ルール
├── global/AGENTS.md             # global runtime policyのcanonical source
├── .agents/skills/              # canonicalかつrepoで発見可能なSkills
├── config/
│   ├── default/config.toml      # portable baseline例
│   └── profiles/                # install可能なnamed profiles
├── templates/project-AGENTS.md
├── plugin/                      # Skill-only package manifests
├── scripts/                     # validate/install/doctor/uninstall/package
├── docs/
└── VERSION
```

canonical Skillsはrepository-native discoveryに合わせて `.agents/skills` に維持します。Plugin生成時だけ標準`skills/`へ正確にコピーするため、二つ目の編集対象はありません。

## 利用方法

内容を確認してから実行してください。

```sh
scripts/validate
scripts/install --dry-run
scripts/install
scripts/doctor --include-codex-runtime
```

installerが管理するのはglobal AGENTS、4つのrepository Skills、Agent OS profile filesだけです。変更前runtimeをbackupし、hash manifestを残します。privateな `~/.codex/config.toml`、credentials、MCP、plugin、project trust、memories、sessions、cachesは上書きしません。

Skill-only Plugin packageは次で生成します。

```sh
scripts/package-plugin
```

既定の生成先はGit管理外の`dist/`です。

## 収録Skills

- **Research:** literature、mathematical、computational、empirical、verification、critical review、publication、reproducibility、recoveryを選択的にrouting
- **Experience Promotion:** evidenceに基づく分類、重複排除、圧縮、最小scopeへの配置、統合、降格、archive、削除
- **Multidisciplinary Review:** 重要な分野横断意思決定の選択的レビュー
- **Local-First App Development:** 暗黙に公開せず、localで開発・検証

## 文書

- [Architecture](docs/architecture.md)
- [Environment inventory](docs/inventory.md)
- [Risk report](docs/risk-report.md)
- [Configuration](docs/configuration.md)
- [Installation and rollback](docs/installation.md)
- [Security](docs/security.md)
- [Development](docs/development.md)
- [Migration mapping](docs/migration.md)
- [Evaluation](docs/evaluation.md)

## 証拠の境界

静的validationとisolated deployment testは構造的完全性と再現可能性を示しますが、agent behaviorの改善を証明しません。複数runのgolden-task evalを実施するまで、行動上の優越性は`NOT VERIFIED`です。

これはOpenAI公式projectではなく、sanitizedした個人設定projectです。config schema変更やPlugin公開前には最新のCodex公式documentationを再確認してください。

## ライセンス

[MIT](LICENSE)
