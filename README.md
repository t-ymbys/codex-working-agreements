# Codex Working Agreements

[日本語](README.ja.md)

A practical, opinionated configuration for making Codex work carefully,
reproducibly, and with bounded effort.

This repository separates persistent rules, progressive task guidance, and
durable state:

- `AGENTS.md`: durable working agreements that should apply to almost every task.
- `.agents/skills/<name>/SKILL.md`: task-specific procedures loaded only when relevant.
- `HANDOFF.md`, Git, checks, and reports: current state, history, deterministic
  enforcement, and evidence, kept outside persistent prompt context.

The central design rule is:

> minimal persistent context + progressive disclosure + durable external state + explicit validation

The goal is not to make every task maximally elaborate. The configuration asks
Codex to use the smallest reliable process, preserve user work, state
uncertainty, validate proportionally to risk, and stop when the requested
outcome is satisfied.

## Repository layout

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

## Included skills

### Research

A thin router for literature review, novelty assessment, mathematical,
computational, and empirical research, verification, critical review,
publication, reproducibility, and recovery. It loads only the references that
can affect the current decision.

It distinguishes verified evidence, inference, hypotheses, assumptions, and
unresolved uncertainty. It also defines search bounds, human-review flags, and
completion gates.

### Experience Promotion

A governed workflow for turning selected operational experience into the
smallest useful durable intervention.

Ordinary success and one-off noise take the fast path. Meaningful experience is
classified, validated, deduplicated, compressed, and routed to the narrowest
sufficient scope. Guidance may also be merged, demoted, archived, or deleted
when it becomes redundant, disproven, stale, or model-obsolete.

### Multidisciplinary Review

A selective cross-domain review workflow for consequential decisions, frontier
questions, and explicit requests for top-tier professional perspectives.

It translates named exemplars into scientific-discovery, philosophical,
strategy-and-systems, founder-and-executive, and AI/ML/cloud evaluation lenses.
It loads only the lenses that can change the decision, preserves disagreement,
and ends with a test, recommendation, or next action rather than prestige-based
role-play.

### Local-First App Development

A release-safety workflow for app and game work. Local development, testing,
and previews remain local by default; deployment or distribution requires an
explicit request naming the destination and release scope. It also distinguishes
access restriction from verified deletion when cleaning up unintended online
resources.

## Use

Clone the repository and review the files before adopting them:

```sh
git clone https://github.com/t-ymbys/codex-working-agreements.git
cd codex-working-agreements
```

When Codex runs inside this repository, the root `AGENTS.md` and repository
skills under `.agents/skills` are available in repository scope.

For personal, cross-repository use, selectively merge the parts you want into:

```text
~/.codex/AGENTS.md
~/.agents/skills/<skill-name>/
```

Do not blindly overwrite an existing configuration. Compare, adapt, and test
the instructions against representative tasks in your own environment.

Run the deterministic repository checks with:

```sh
python3 scripts/validate_repository.py
```

See [Context Architecture](docs/CONTEXT_ARCHITECTURE.md),
[Migration Report](docs/MIGRATION_REPORT.md), and
[Evaluation Proposal](docs/EVAL_PROPOSAL.md) for design and evidence boundaries.

## Status and limitations

- This is a personal working configuration, not an official OpenAI project.
- The skill files have passed static structure and frontmatter validation in the
  author's environment, including local link and sensitive-pattern checks.
- The documented repository and user skill paths were checked against current
  official Codex documentation. Behavioral effectiveness has not been
  established by a controlled benchmark.
- Some rules are intentionally conservative and may be too heavy for disposable
  prototypes.
- Paths and supported behavior can change as Codex evolves; consult current
  official documentation before relying on environment-specific details.

## Snapshot provenance

This repository is a sanitized snapshot of the author's active working
agreements, reviewed on 2026-09-27. Mutable memory, task history, credentials,
local configuration, and private research artifacts are not included.

## License

[MIT](LICENSE)
