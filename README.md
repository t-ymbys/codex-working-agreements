# Codex Working Agreements

[日本語](README.ja.md)

A practical, opinionated configuration for making Codex work carefully,
reproducibly, and with bounded effort.

This repository separates three kinds of guidance:

- `AGENTS.md`: durable working agreements that should apply to almost every task.
- `.agents/skills/<name>/SKILL.md`: task-specific procedures loaded only when relevant.
- mutable project or learning state: deliberately kept outside this repository.

The central design rule is:

> correctness x recoverability x reproducibility x cost efficiency

The goal is not to make every task maximally elaborate. The configuration asks
Codex to use the smallest reliable process, preserve user work, state
uncertainty, validate proportionally to risk, and stop when the requested
outcome is satisfied.

## Repository layout

```text
.
├── AGENTS.md
└── .agents/
    └── skills/
        ├── research/
        │   ├── SKILL.md
        │   ├── references/
        │   └── assets/
        └── experience-promotion/
            ├── SKILL.md
            ├── references/
            └── assets/
```

## Included skills

### Research

A rigorous workflow for literature review, novelty assessment, theoretical and
computational work, empirical studies, reproducibility, manuscript preparation,
and interrupted-research recovery.

It distinguishes verified evidence, inference, hypotheses, assumptions, and
unresolved uncertainty. It also defines search bounds, human-review flags, and
completion gates.

### Experience Promotion

A governed workflow for turning selected operational experience into the
smallest useful durable intervention.

Its Stage 0 fast path deliberately does nothing for ordinary successful tasks.
Deeper analysis is reserved for important failures, recurring problems,
high-reuse techniques, or explicit self-improvement requests. Promotion ranges
from transient context to deterministic guardrails, with stronger evidence and
review required as impact increases.

## Use

Clone the repository and review the files before adopting them:

```sh
git clone git@github.com:t-ymbys/codex-working-agreements.git
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

## Status and limitations

- This is a personal working configuration, not an official OpenAI project.
- The skill files have passed static structure and frontmatter validation in the
  author's environment.
- Automatic discovery and behavioral effectiveness have not been established
  by a controlled benchmark.
- Some rules are intentionally conservative and may be too heavy for disposable
  prototypes.
- Paths and supported behavior can change as Codex evolves; consult current
  official documentation before relying on environment-specific details.

## Snapshot provenance

The initial public version is a sanitized snapshot of the author's active
configuration as of 2026-09-16. Mutable memory, task history, credentials, local
configuration, and private research artifacts are not included.

## License

[MIT](LICENSE)
