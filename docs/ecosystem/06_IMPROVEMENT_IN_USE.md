# Improvement in Use — Dogfooding MASTERMIND

**Purpose:** Apply the improvement process to itself. Use what we build. Test it. Assess true value. Refine before public release. **MASTERMIND improves MASTERMIND.**

**Related:** improvement_propagation.md, improvement_process.md, 04_MASTER_SCRUTINY_PROMPT.md

---

## The Principle

> A system that improves all systems must improve itself. If we don't use it on itself, we don't believe it.

**Improvement in Use** = dogfooding + value assessment + safe iteration + rollout readiness.

---

## How It Works

### 1. Every Session: Use the System

| Action | When | How |
|--------|------|-----|
| **Add ideas** | When you have one | `mm add "idea"` or add to main_memory.md |
| **Run propagation** | After adding | `mm propagate` — evaluate against all projects |
| **Check structure** | Before finishing | `mm check` — totality pass |
| **Sync links** | When projects change | `mm sync-links` — MASTERMIND_LINK in all roots |
| **Status** | Anytime | `mm status` — unprocessed ideas, layout |
| **Improve the system** | When user says it | Read mastermind §4; identify gaps; improve; document |

### 2. Value Assessment: What Have We Built?

**Questions to ask periodically:**

| Question | How to Answer |
|----------|---------------|
| Does MASTERMIND actually improve coordination? | Use it. Did ideas propagate? Did projects stay aligned? |
| Does it reduce cognitive load or add it? | If adding ideas and running propagation feels like friction, simplify. |
| Would someone pay for modules? | Sellable modules doc exists. Test with one real user. |
| Is the CLI useful? | Use `mm add`, `mm propagate`, `mm check` every session. If not, improve or remove. |
| Do the docs help? | Could a stranger install and use MASTERMIND from docs alone? |
| Are we mission-aligned? | Mutual flourishing. Does MASTERMIND serve that or distract? |

**Document answers** in session_log.md or main_memory.md. Update the system based on findings.

### 3. Safe Path to Release

- **Don't ship broken.** Run `mm check` before any publish.
- **Don't ship private.** Rollout Checklist in 03_DEPLOYMENT.md — remove paths, names, secrets.
- **Don't ship untested.** Use MASTERMIND yourself for 2+ weeks. Add ideas. Run propagation. Fix what breaks.
- **Ship incrementally.** Private repo first. Then shared with one trusted person. Then public.

### 4. Meta-Improvement Loop

```
Use MASTERMIND → Discover friction → Add idea to Main Memory → Run propagation
     → Apply improvement → Document → Use again → Repeat
```

**Improve the improvement process** when:
- Propagation feels redundant or slow
- CLI commands are unclear
- Docs contradict each other
- A step always gets skipped (maybe it shouldn't exist)

---

## Checklist: Am I Improvement-in-Use Compliant?

- [ ] I add new ideas to Main Memory (or mm add) when they occur
- [ ] I run propagation (mm propagate) when ideas are added
- [ ] I run mm check before considering work "done"
- [ ] I use the system for real coordination, not just documentation
- [ ] I assess value: Does this actually help? Would others find it valuable?
- [ ] I document learnings in session_log and CHANGELOG

---

## What Gets Better

When improvement-in-use is active:

1. **MASTERMIND** — Processes, CLI, docs improve because we feel the pain.
2. **888** — Coordination engine gets refined by actual use.
3. **Projects** — PHYLLUX, BWURM, ENGENICA, etc. get improvements from propagated ideas.
4. **You** — You learn what works. Process becomes muscle memory.
5. **Future users** — They inherit a system that's been stress-tested.

---

*Improvement in Use. Last updated: February 2026.*
