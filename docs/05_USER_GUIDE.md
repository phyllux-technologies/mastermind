# User Guide — Using MASTERMIND

**Purpose:** Complete guide to every component. See docs/01-04 for install, setup, deploy, benefits.

---

## 1. mastermind.md — Central Control

**Location:** Workspace root (copy from `mastermind/mastermind.md`)

Read first. Defines mission, project map, and how to use the system. Key sections: Mission, Architecture, Project Map, How to Use, Key Files, Totality Check.

---

## 2. Main Memory

**Location:** `core/memory/main_memory.md`

Canonical store for ideas, epiphanies, lessons, insights. Add here first. Run Improvement Propagation after each addition. Sections: New/Unprocessed, Ideas, Epiphanies, Lessons Learned, Insights.

---

## 3. Improvement Propagation

**Location:** `core/processes/improvement_propagation.md`

Runs on every new idea. Steps: Read Main Memory → Evaluate against each project → Apply improvements → Propagate to other parts → Document → Totality check. Triggers: new idea added, "run propagation", "check main memory".

---

## 4. Project Registry

**Location:** `core/projects/_registry.md`

Map of your projects. Customize with paths, roles, masters. Per-project files: `core/projects/[PROJECT].md`.

---

## 5. Meta (Improvement Process)

**Locations:** `core/meta/improvement_process.md`, `meta_improvement.md`

Levels 1–4: Improve output, improve system, improve instructions, improve the improvement-of-improvement. Read when you say "improve the system" or "improve the improvement process".

---

## 6. Supporting Files

- **epiphanies.md** — Consolidated epiphanies
- **session_log.md** — Session-by-session learnings
- **by_topic/** — Topic-organized (instructions, coordination)
- **sync/** — Templates (master_template, link_instructions)
- **config/** — Mission, configuration

---

## 7. Documentation

**docs/** — Full docs. INDEX, Installation, Setup, Deployment, Benefits, User Guide, Best Practices, Workflows, Reference, FAQ, How We Built It.

**docs/ecosystem/** — Strategy, Governor, sellable modules, Master Scrutiny prompt, lessons from systems critique (counter-narratives, trust), Improvement in Use (dogfooding), Rollout & Web Ecosystem (your checklist), System for MASTERMIND-caliber products.

---

## 8. Improvement in Use

Use MASTERMIND on itself. Add ideas, run propagation, assess value. See docs/ecosystem/06_IMPROVEMENT_IN_USE.md. Before public release: Run `mm check`, complete Rollout Checklist (03_DEPLOYMENT), REPO_SETUP sanitization.

---

## 9. Preparing for Public Release

- **REPO_SETUP.md** — Checklist for creating the GitHub repo; sanitization (paths, names) before public.
- **03_DEPLOYMENT** — Rollout Checklist. Run `mm check` before publish.
- **07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY** — Web/repo architecture, hub vs master repo, your next steps.

---

*MASTERMIND User Guide. Last updated: February 2026.*
