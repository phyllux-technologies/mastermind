# MASTERMIND — Central Control

**Location:** Copy this file to your workspace root. From `mastermind/mastermind.md`.  
**Purpose:** Central control for your coordination system. The core engine lives in `mastermind/core/`; this file is the pilot. Read this first when coordinating or when you say "read mastermind."

---

## 1. Mission

> Use intelligence and creativity to build systems that improve all your work. Add ideas, run propagation, apply improvements across every project. Improve the system; improve the process of improvement.

**Customize:** Edit `mastermind/config/mission.md` to define your own mission.

---

## 2. System Architecture

![Data flow](mastermind/assets/mastermind-data-flow.png)

```
your-workspace/
├── mastermind.md          ← THIS FILE (copy to workspace root)
├── mastermind/            ← This repo
│   ├── core/              ← The engine
│   │   ├── memory/        ← Main Memory, epiphanies, session log
│   │   ├── processes/     ← Improvement Propagation
│   │   ├── projects/      ← Project registry
│   │   ├── meta/          ← Improvement-of-improvement
│   │   └── sync/          ← Templates
│   ├── config/            ← Your mission, paths
│   └── docs/              ← Documentation
│
└── your-projects/         ← Your actual projects
```

---

## 3. Project Map

Configure your projects in `mastermind/core/projects/_registry.md`.

| Project | Path | Role |
|---------|------|------|
| *(Configure in _registry.md)* | | |

---

## 4. How to Use

### When Starting a Task
1. Read mastermind.md (this file).
2. Read `mastermind/core/projects/[PROJECT].md` for the project you're working in.
3. Read that project's master (README, docs, etc.).
4. Execute. Update artifacts. Run totality check.

### When Adding a New Idea
1. Add to `mastermind/core/memory/main_memory.md` (New/Unprocessed if unsure).
2. Run Improvement Propagation — `mastermind/core/processes/improvement_propagation.md`.
3. The process evaluates against all projects; applies improvements; propagates; documents.
4. Result: Improvements applied; everything documented.

### Continuous Learning & Insight (Always Running)
1. Read `core/memory/main_memory.md`, `learned_context.md`, `epiphanies.md`; if present, `Learnings.md` (workspace root).
2. Cross-reference everything the user shares with accumulated knowledge.
3. Identify implications — what could come from it (positive or negative).
4. Explain comprehensively to the user when substantive implications exist.
5. Add new learnings to `learned_context.md` or `Learnings.md`.
6. Runs **in tandem** with creation, brainstorming, propagation — not instead of. See `core/processes/continuous_learning_insight.md`.

### When You Say "Improve the System"
1. Read mastermind.md, `mastermind/core/meta/improvement_process.md`.
2. Identify gaps, friction, missing triggers.
3. Improve mastermind.md, core/, project links.
4. Document in `mastermind/core/CHANGELOG.md`.

### When You Say "Improve Instructions"
1. Revise the project's master, AGENTS, or rules.
2. Apply 5W1H; totality check.
3. Document in project CHANGELOG.

---

## 5. Key Files

| File | Purpose |
|------|---------|
| mastermind.md | This file — central control |
| core/memory/main_memory.md | Main Memory — ideas, epiphanies, lessons |
| core/memory/learned_context.md | Learned Context — what AI has learned from user |
| core/processes/improvement_propagation.md | Improvement Propagation — runs on every new idea |
| core/processes/continuous_learning_insight.md | Continuous Learning — learns from everything; explains implications; runs always |
| core/projects/_registry.md | Project map |
| core/CHANGELOG.md | System change history |
| config/mission.md | Your mission (customize) |
| docs/ | Full documentation |
| docs/ecosystem/ | Strategy, Governor, modules, counter-narratives |
| scripts/mm.py, mm.bat | CLI: add, propagate, check, sync-links, scan, status |

---

## 6. Totality Check

Before finishing: Who? What? When? Where? Why? How?

---

## 7. Values

MASTERMIND is **voluntary, transparent, human-centered**. You choose. Free to use, free to leave. No compliance required. Question it, critique it, adapt it. See `mastermind/docs/ecosystem/05_LESSONS_FROM_SYSTEMS_CRITIQUE.md` if someone asks "Is this another controlling system?"

---

*MASTERMIND by David Edward Sproule & Cursor AI. Last updated: February 2026.*
