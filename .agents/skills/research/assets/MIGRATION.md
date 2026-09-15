# Recommended placement

Copy:

- `home/.codex/AGENTS.md` -> `~/.codex/AGENTS.md`
- `home/.agents/skills/research/` -> `~/.agents/skills/research/`

For each substantial research project, prefer:

```text
<project>/
├── .git/
├── HANDOFF.md          # when multi-session state is useful
├── AGENTS.md           # optional: only project-specific rules
├── manuscript/
├── src/
├── experiments/
└── ...
```

Use `assets/HANDOFF.template.md` as a starting point when a project needs `HANDOFF.md`.

The old `~/.codex/skills/research/research_skill.md` should be retired after confirming the new Skill is detected.
