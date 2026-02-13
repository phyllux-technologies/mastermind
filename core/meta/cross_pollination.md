# Cross-Pollination — MASTERMIND (Modular) ↔ Workspace System

**Purpose:** Keep MASTERMIND (modular, for others) and a workspace-native coordination system in sync. Each can help the other. Run this check periodically if you use both.

**Trigger:** When improving either system, or every few sessions.

---

## The Two Layouts

| System | Location | Purpose |
|--------|----------|---------|
| **MASTERMIND** | mastermind/ (this repo) | Modular, portable. For others to install. core/, templates/, config/. |
| **Workspace-native** | your-workspace/workspace-engine/ | Workspace-bound. Full ecosystem, project registry, pilot file. |

Keep both if you use them. They serve different needs: portable vs. workspace-bound.

---

## Cross-Pollination Process

1. **Compare** — scripts/mm.py, processes, meta, docs in both.
2. **Identify** — What would help the other? CLI, process steps, error handling.
3. **Assess safety** — No workspace-specific paths or private data into modular.
4. **Add if safe** — Implement. Preserve each system's identity.
5. **Document** — Note in CHANGELOG or session_log.

---

## Safety Rules

- **Workspace → MASTERMIND:** No workspace-specific paths, project names, or private content. Use relative paths, examples.
- **MASTERMIND → Workspace:** Safe to add. Windows compatibility matters for both (`[OK]` not `✓`).
- **CLI parity:** Same commands. Feature differences OK if intentional.

---

*Run every now and then. Both systems improve. Last: February 2026.*
