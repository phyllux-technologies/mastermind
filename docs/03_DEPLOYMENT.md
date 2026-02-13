# Deployment — How to Deploy MASTERMIND

**Purpose:** Deploy MASTERMIND for local use, team use, or as a shareable repo.

---

## Deployment Modes

### 1. Local (Single User)

**Use case:** You alone use MASTERMIND on your machine.

1. Install and setup as in 01_INSTALLATION and 02_SETUP.
2. Your `mastermind/` folder lives in your workspace. No server, no cloud.
3. Everything is file-based; no deployment infrastructure needed.
4. Optionally: Add `mastermind/` to git and push to a private repo for backup and versioning.

---

### 2. Team (Shared Repo)

**Use case:** A team shares one MASTERMIND instance.

1. Create a repo (GitHub, GitLab, etc.) with the MASTERMIND system.
2. Team members clone into their local workspace.
3. **Shared:** core/, docs/, templates/ — everyone uses the same engine.
4. **Local/custom:** config/mission.md, config/local_config.md — each person can customize (add to .gitignore if needed).
5. **Project-specific:** core/projects/_registry.md, core/memory/ — can be shared (everyone adds to Main Memory) or forked per team/person.

**Recommendation:** Keep core/ and docs/ in the shared repo. Keep config/mission.md and core/memory/ in a shared repo if the team collaborates on ideas; otherwise, each person has their own clone and their own memory.

**Trust:** For teams wary of "coordination systems," share docs/ecosystem/05_LESSONS_FROM_SYSTEMS_CRITIQUE.md. Voluntary, transparent, human-first. No compliance required.

---

### 3. Distributed (Fork and Customize)

**Use case:** Each person/org forks MASTERMIND and customizes for their own use.

1. Fork the MASTERMIND repo.
2. Customize: mission, project registry, docs (add org-specific content).
3. Optionally: Contribute improvements back upstream.
4. Each fork is independent; no shared state.

---

### 4. Template / Starter Kit

**Use case:** MASTERMIND as a "use this to get started" template.

1. User clones or downloads MASTERMIND.
2. Replaces placeholder projects with their own.
3. Fills in mission, registry.
4. Uses it. No need to contribute back; it's a starter.

---

## Repo Structure for Public Rollout

When you make the repo public:

```
mastermind/
├── README.md           # Overview, quick start, credits
├── LICENSE             # MIT
├── CREDITS.md          # Attribution
├── .gitignore
├── mastermind.md       # Pilot (copy to workspace root)
├── core/               # Engine — users don't typically modify
├── config/             # Examples only; users copy and customize
├── templates/          # MASTERMIND_LINK, etc.
├── assets/              # Images (hero, modules, counter-narrative)
└── docs/                # Full documentation + ecosystem/
```

**Do not include in repo:**
- Private/sensitive data
- User-specific paths (e.g., your-workspace/)
- Project names or content from your specific use case (use placeholders)
- API keys, secrets, credentials

---

## Rollout Checklist

- [ ] Remove all private/sensitive content
- [ ] Replace specific project names with placeholders
- [ ] Replace specific paths with generic instructions
- [ ] Verify CREDITS.md and LICENSE
- [ ] README is clear for first-time users
- [ ] docs/01_INSTALLATION through 04_BENEFITS are complete
- [ ] Repo is public (or shared with intended users)
- [ ] Consider: GitHub Topics (productivity, ai, coordination, workflow)
- [ ] docs/ecosystem/ included (strategy, Governor, modules, counter-narratives)
- [ ] assets/ with images for marketing and trust
- [ ] Run `mm check` — structure validated before publish

---

## Next Step

→ [04_BENEFITS.md](04_BENEFITS.md) — How to benefit from MASTERMIND.

**Full rollout & web integration:** See [07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md](ecosystem/07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md) — your checklist, Phyllux+Netlify+MASTERMIND, hub vs master repo.

---

*MASTERMIND Deployment. Last updated: February 2026.*
