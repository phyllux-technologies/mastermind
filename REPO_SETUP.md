# Repo Setup — When You Create the GitHub Repo

**Purpose:** Checklist for initializing the MASTERMIND repo. Use when you create the repository.

---

## Before First Push

- [ ] Create repo on GitHub (private for now, per your plan).
- [ ] `git init` in mastermind/ folder.
- [ ] `git add .`
- [ ] `git status` — verify no private files (config/mission.md, config/local_config.md should be in .gitignore).
- [ ] `git commit -m "Initial commit: MASTERMIND v0.1.0 — coordination system for improving all work"`
- [ ] `git remote add origin https://github.com/[your-org]/mastermind.git`
- [ ] `git branch -M main`
- [ ] `git push -u origin main`

---

## Before Public Rollout

- [ ] **Sanitize:** Replace workspace-specific paths with generic (e.g. `workspace/` or `your-workspace/`) in docs.
- [ ] **Sanitize:** 07_ROLLOUT, 04_MASTER_SCRUTINY use workspace-specific paths — replace or add "customize for your setup" note.
- [ ] Review all files for private/sensitive content (paths, names, etc.).
- [ ] Ensure README has correct repo URL (update when known).
- [ ] CREDITS.md and LICENSE are correct.
- [ ] docs/03_DEPLOYMENT.md rollout checklist completed.
- [ ] Make repo public.
- [ ] Add topics: productivity, ai, coordination, workflow, knowledge-management
- [ ] Consider: GitHub Discussions, Issues templates (optional)

---

## README Badge (Optional)

When repo is public, you can add:

```markdown
[![MASTERMIND](https://img.shields.io/badge/MASTERMIND-Coordination%20System-blue)](https://github.com/[your-org]/mastermind)
```

---

*Repo setup guide. Last updated: February 2026.*
