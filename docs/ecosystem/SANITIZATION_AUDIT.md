# Sanitization Audit — Before Public Release

**Purpose:** Every internal item assessed. RECYCLE = reshape for customers. REMOVE = delete or gitignore. KEEP = already fine.

**Status:** Audit complete. Execute below.

---

## Summary

| Category | Action | Count |
|----------|--------|-------|
| RECYCLE (reshape) | 6 | |
| REMOVE (trash) | 1 | |
| SANITIZE (minimal edit) | 8 | |

---

## 1. RECYCLE — Reshape for Customers

### 1.1 DO-THIS-NOW-DAVE.md → ROLLOUT_CHECKLIST.md
**Current:** Internal playbook for Dave. Paths, org names, phased rollout.
**Action:** Create `docs/ecosystem/ROLLOUT_CHECKLIST.md` — generic version. Strip "Dave", use `[your-org]`, `[your-workspace]`. Keep phase structure, module readiness, merchant prep. Remove DO-THIS-NOW-DAVE from repo; add to .gitignore so you keep a local copy.

### 1.2 cross_pollination.md
**Current:** "MASTERMIND ↔ 888", workspace-specific paths.
**Action:** Reshape to "Syncing MASTERMIND with a Workspace System". Replace 888 with "workspace-native layout" or "your workspace engine". Generic path examples. Keeps the value: users who run both modular + workspace setup get sync guidance.

### 1.3 09_FULL_SETUP_AND_INTEGRATION_STATUS.md
**Current:** "Audience: You (David)". Internal paths, 888 references.
**Action:** Change audience to "Deployers and maintainers". Replace workspace-specific paths with `your-workspace/`. Generalize "888 docs" to "workspace layout docs".

### 1.4 main_memory.md
**Current:** Ideas table has session-specific entries (888, ENGENICA, dates). Epiphany mentions "e.g. Meshuggah".
**Action:** Reset Ideas to template (one generic example). Generalize epiphany: "From critique of oppressive systems" (keeps the lesson, optional band credit elsewhere).

### 1.5 session_log.md
**Current:** 2026-02-12 entry with 888 paths, internal artifacts.
**Action:** Reset to template + one anonymized example session (ecosystem build, images, counter-narratives — no 888 paths, no internal repos).

### 1.6 Meshuggah Attribution
**Current:** 05_LESSONS, HOW_WE_BUILT_IT, CHANGELOG, etc. name the band.
**Action:** KEEP in 05_LESSONS — it's attribution, not instruction. The value (counter-narratives, themes) is already customer-facing. Fans appreciate; others skip. Optional: add subtle nod in CREDITS under "Inspirations" if you want to showcase without being didactic.

---

## 2. REMOVE

### 2.1 DO-THIS-NOW-DAVE.md
**Action:** `git rm DO-THIS-NOW-DAVE.md`. Add to .gitignore. You keep a local copy. Replace with ROLLOUT_CHECKLIST for repo.

---

## 3. SANITIZE — Minimal Edits

### 3.1 Paths
Replace workspace-specific paths with `your-workspace/` or `workspace/` in:
- docs/ecosystem/07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md
- docs/ecosystem/04_MASTER_SCRUTINY_PROMPT.md
- config/config.example.md
- REPO_SETUP.md (sanitization checklist)
- core/meta/cross_pollination.md (when reshaping)

### 3.2 biomimetic-inventions-public
**Current:** Internal GitHub repo name for Phyllux web.
**Action:** Replace with `[your-phyllux-web-repo]` or `phyllux-web` in docs. Or keep if it's not sensitive (repo names can be generic).

### 3.3 mm.py
**Action:** Exclude mm.py from path scan (it contains the detection pattern). Keep path scan for other files. `888` in mm.py stays — supported layout name.

### 3.4 CHANGELOG, SCRUTINY_REPORT, etc.
**Action:** Replace "888 registry" with "workspace registry" or "project registry" where it reads internal. ENGENICA references can stay (it's a product).

---

## 4. KEEP — No Change

- **David Edward Sproule** — Creator. LICENSE, CREDITS. Keep.
- **phyllux.io, phyllux-technologies** — Product/org. Keep.
- **Phyllux, BWURM, ENGENICA, MASTERMIND** — Ecosystem products. Keep.
- **05_LESSONS Meshuggah attribution** — Value extracted. Attribution is credit, not instruction. Keep.

---

*Audit complete. Execute in order. Last updated: February 2026.*
