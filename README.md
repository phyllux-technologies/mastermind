# MASTERMIND — Coordination System for Improving All Your Work

A modular, sophisticated coordination engine that helps you and AI improve every project and every process. Add ideas, run propagation, apply improvements across your entire workflow.

**Created by David Edward Sproule and Cursor AI (Composer)** — February 2026

**Ecosystem:** Integrates with [Phyllux](https://phyllux.io) (biomimetic tech, ENGENICA), Content Studio, and the broader coordination ecosystem. Partnership inquiries welcome — affiliates, resellers, integrators. Mutual benefit.

![MASTERMIND Hero](assets/mastermind-hero.png)

![Improve all your work](assets/mastermind-quote-card.png)

---

## What It Does

- **Main Memory** — A single canonical store for ideas, epiphanies, lessons learned, and insights
- **Improvement Propagation** — Evaluates every idea against all your projects and applies improvements automatically
- **Cross-project coordination** — Keeps multiple projects aligned to your mission and helps learnings spread
- **Self-improving system** — The system improves itself and the process of improvement

![Key features](assets/mastermind-feature-grid.png)

![You choose. The system serves you.](assets/mastermind-counter-agency.png)

---

## Values

- **Voluntary** — Optional. You decide. No compliance required.
- **Transparent** — Open source, open docs. Trust through transparency.
- **Human-centered** — Tools serve people. Improves you; doesn't control you.
- **Free to leave** — No lock-in. No cages. See [Lessons from Systems Critique](docs/ecosystem/05_LESSONS_FROM_SYSTEMS_CRITIQUE.md).

---

## Quick Start

1. **Install** — Clone or copy this repo into your workspace (see [Installation](docs/01_INSTALLATION.md))
2. **Setup** — Copy `mastermind.md` to your workspace root; configure your projects (see [Setup](docs/02_SETUP.md))
3. **Use** — Add ideas: `mm add "idea"` or add to `core/memory/main_memory.md`; run `mm propagate` or the propagation process
4. **Benefit** — Improvements propagate across projects; everything gets better

**CLI:** `mm add "idea"` | `mm propagate` | `mm check` | `mm sync-links` | `mm scan` | `mm status` — see [docs/11_CLI.md](docs/11_CLI.md)

**Ready to publish?** → [REPO_SETUP.md](REPO_SETUP.md) · [Rollout & Web Strategy](docs/ecosystem/07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md)

---

## Documentation

| Document | Purpose |
|----------|---------|
| [01_INSTALLATION](docs/01_INSTALLATION.md) | How to install MASTERMIND |
| [02_SETUP](docs/02_SETUP.md) | How to set up and configure |
| [03_DEPLOYMENT](docs/03_DEPLOYMENT.md) | How to deploy (local, team, repo) |
| [04_BENEFITS](docs/04_BENEFITS.md) | How to benefit; what you gain |
| [05_USER_GUIDE](docs/05_USER_GUIDE.md) | Complete guide to every component |
| [06_BEST_PRACTICES](docs/06_BEST_PRACTICES.md) | Optimal usage |
| [07_WORKFLOWS](docs/07_WORKFLOWS.md) | Step-by-step workflows |
| [08_REFERENCE](docs/08_REFERENCE.md) | Quick lookup |
| [09_FAQ](docs/09_FAQ.md) | FAQ and troubleshooting |
| [10_HOW_WE_BUILT_IT](docs/10_HOW_WE_BUILT_IT.md) | Architecture, design |
| [11_CLI](docs/11_CLI.md) | mm commands — add, propagate, check, sync-links, scan, status |
| [ecosystem/](docs/ecosystem/) | Strategy, Governor, modules, scrutiny, counter-narratives |

---

## Structure

```
mastermind/
├── README.md           ← You are here
├── LICENSE             ← MIT
├── CREDITS.md          ← Attribution
├── .gitignore
├── mastermind.md       ← The pilot — copy to workspace root
├── scripts/            ← CLI (mm add, propagate, check, sync-links, scan, status)
├── core/               ← The engine
│   ├── memory/         ← Main Memory, epiphanies, session log
│   ├── processes/      ← Improvement Propagation
│   ├── projects/       ← Project registry, per-project coordination
│   ├── meta/           ← Improvement-of-improvement
│   └── sync/           ← Templates
├── config/             ← Your mission (copy .example files)
├── templates/          ← MASTERMIND_LINK, cursor-rule (copy to workspace)
└── docs/               ← Comprehensive documentation
```

---

## Credits

**Creators:** David Edward Sproule & Cursor AI (Composer)

See [CREDITS.md](CREDITS.md) for full attribution.

---

## License

MIT License. See [LICENSE](LICENSE).

---

*MASTERMIND — A system that improves all systems. Last updated: February 2026.*
