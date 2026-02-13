# Improvement Propagation Process

**Purpose:** Use Main Memory and everything in it to apply improvements to individual projects and the system as a whole. **Runs every time a new idea is added to Main Memory.**

**Trigger:** New entry in `core/memory/main_memory.md` (especially **New / Unprocessed** section).

**CLI:** Run `mm propagate` for a guided run — prints steps and paths.

---

## Overview

![6-step propagation workflow](../../assets/mastermind-propagation-steps.png)

1. **Read** Main Memory (and epiphanies, session_log, by_topic as needed).
2. **Evaluate** each idea/epiphany/lesson/insight against every project and the system.
3. **Apply** improvements where they fit.
4. **Propagate** — If an improvement applies to one project, check if it applies to others.
5. **Document** everything. Spread through the system. Improve the system itself.

---

## Step-by-Step Process

### Step 1: Read Main Memory
- **Read** `core/memory/main_memory.md` fully.
- **Read** `core/memory/epiphanies.md`, `session_log.md`, and `learned_context.md` for context.
- **Identify** all entries in **New / Unprocessed** and any not yet fully propagated.
- **List** the ideas/epiphanies/lessons/insights to evaluate.

### Step 2: Evaluate Against Each Target

![Evaluation matrix](../../assets/mastermind-evaluation-matrix.png)

For each idea, ask (customize targets from your `_registry.md`):

| Target | Question |
|--------|----------|
| **Project A** | Does this improve [Project A's focus]? |
| **Project B** | Does this improve [Project B's focus]? |
| **Core / MASTERMIND** | Does this improve coordination, memory, processes, or the system itself? |
| **Mission** | Does this advance your mission (see config/mission.md)? |

If **yes** to any → proceed to apply.

### Step 3: Apply the Improvement
- **Make** the concrete change (code, docs, instructions, config).
- **Preserve** existing behavior unless the improvement explicitly replaces it.
- **Document** in the relevant CHANGELOG (project or core).
- **Update** BUGS.md if fixing a bug; move from Open to Fixed.

### Step 4: Propagate to Other Targets
- **Ask:** Does this improvement apply to other projects or parts?
- **Apply** to those targets. **Document** each application.
- **Update** project masters, AGENTS, rules as needed.

### Step 5: Document and Spread
- **core/CHANGELOG.md** — System-level changes under [Unreleased].
- **Project CHANGELOG** — Project-specific changes.
- **session_log.md** — Log this propagation run.
- **main_memory.md** — Move entry from New/Unprocessed to appropriate section; mark Status = propagated.
- **Improve the system** — If the insight improves mastermind, core structure, or processes, make those changes.

### Step 6: Improve All Aspects
- **Ask:** Did this improvement suggest further improvements?
- New ideas → add to Main Memory → run again (one cycle per trigger unless user requests continued propagation).
- **Totality check** — Who, What, When, Where, Why, How.

---

## When to Run

| Trigger | Action |
|---------|--------|
| **New idea added** | Run this process. |
| **"Run propagation"** | Run this process. |
| **"Check main memory"** | Read main memory; run if New/Unprocessed has entries. |
| **After significant session** | Add learnings to main memory; run process. |
| **Periodic (e.g., weekly)** | Optional: re-evaluate recent entries. |
| **Improvement in Use** | Use MASTERMIND on itself. See docs/ecosystem/06_IMPROVEMENT_IN_USE.md. |

---

## Output Checklist

- [ ] Main Memory updated (New cleared or entries moved).
- [ ] All applicable improvements applied to projects.
- [ ] CHANGELOG(s) updated.
- [ ] session_log.md has propagation run entry.
- [ ] Totality check passed.

---

## Constraints

- **Preserve unless asked** — Don't change behavior without explicit rationale.
- **One propagation cycle per trigger** — Unless user requests continued propagation.
- **Mission alignment** — Only apply improvements that advance your mission.
- **Document everything** — No improvement without traceability.

---

*MASTERMIND Core. Runs on every new idea. Improves everything. Last updated: February 2026.*
