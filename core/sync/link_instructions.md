# Sync and Link Instructions

---

## Canonical Locations
| What | Where |
|------|-------|
| Central control | mastermind.md (workspace root) |
| Engine | mastermind/core/ |
| Main Memory | core/memory/main_memory.md |
| Project registry | core/projects/_registry.md |

---

## What Gets Synced (core → Project Roots)
1. **MASTERMIND_LINK.md** — Short file in each project root: points to mastermind.md and core.
2. **Project coordination** — core/projects/[PROJECT].md references each project.
3. **No duplication** — core holds canonical; projects reference it.

---

## What Projects Contribute
- **Learnings** → core/memory/main_memory.md or epiphanies.md
- **Session log** → core/memory/session_log.md
- **Registry updates** → core/projects/_registry.md

---

*MASTERMIND Core. Last updated: February 2026.*
