# Cross-Pollination — MASTERMIND (Modular) ↔ 888 (Workspace)

**Purpose:** Keep MASTERMIND (modular, for others) and 888 (workspace system) in sync. Each can help the other. Run this check periodically.

**Trigger:** When improving either system, or every few sessions.

---

## The Two Systems

| System | Location | Purpose |
|--------|----------|---------|
| **MASTERMIND** | mastermind/ (this repo) | Modular, portable. For others to install. core/, templates/, config/. |
| **888** | d:\Workspace\888 | Workspace-native. Full ecosystem, project registry, mastermind.md pilot. |

Keep both. Don't merge. They serve different needs: portable vs. workspace-bound.

---

## Cross-Pollination Process

1. **Compare** — scripts/mm.py, processes, meta, docs in both.
2. **Identify** — What would help the other? CLI, process steps, error handling.
3. **Assess safety** — No workspace-specific paths or private data into modular.
4. **Add if safe** — Implement. Preserve each system's identity.
5. **Document** — Note in CHANGELOG or session_log.

---

## Safety Rules

- **888 → MASTERMIND:** No workspace-specific paths, project names, or private content. Use relative paths, examples.
- **MASTERMIND → 888:** Safe to add. Windows compatibility matters for both (`[OK]` not `✓`).
- **CLI parity:** Same commands. Feature differences OK if intentional.

---

*Run every now and then. Both systems improve. Last: February 2026.*
