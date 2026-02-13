# Rollout & Web Ecosystem Strategy

**Purpose:** Get MASTERMIND and the full offering (Phyllux, BWURM, ENGENICA, etc.) ready for public release. Define web/repo architecture. Give you a clear checklist and integration path.

**Full status (missions, merchant, everything):** See [09_FULL_SETUP_AND_INTEGRATION_STATUS](09_FULL_SETUP_AND_INTEGRATION_STATUS.md).

**Current state:** Phyllux website in `workspace/website/` → deploy to your web repo → Netlify → phyllux.io. MASTERMIND in `workspace/mastermind/`. BWURM, ENGENICA in active projects.

---

## Part 1: Your End — What You Need to Do Before Public Release

### MASTERMIND Repo (Public)

| Step | Action | Status |
|------|--------|--------|
| 1 | Create GitHub repo (e.g. `mastermind-coordination` or `phyllux-technologies/mastermind`) | [ ] |
| 2 | Copy `mastermind/` to the repo. Remove draft/private content. Use placeholders for project names. | [ ] |
| 3 | Run `mm check` — validate structure | [ ] |
| 4 | Complete Rollout Checklist (03_DEPLOYMENT.md) — LICENSE, CREDITS, README | [ ] |
| 5 | Push. Add GitHub Topics: productivity, ai, coordination, workflow | [ ] |
| 6 | Optional: Connect to Netlify for a MASTERMIND landing page (docs as static site) | [ ] |

### Phyllux / Biomimetic (Already Live)

| Step | Action | Status |
|------|--------|--------|
| 1 | Keep Netlify + your web repo as-is for phyllux.io | [ ] |
| 2 | When ready: Add link to MASTERMIND from Phyllux site (e.g. "Products" or "Ecosystem" page) | [ ] |
| 3 | Add link to BWURM/Content Studio if you have a public offering | [ ] |

### Secrets & Paths

| Step | Action | Status |
|------|--------|--------|
| 1 | Audit all repos for workspace-specific paths, API keys, private content | [ ] |
| 2 | Use `.gitignore` for secrets, local config | [ ] |
| 3 | Replace your real project names with placeholders in mastermind template | [ ] |

---

## Part 2: Web Architecture — Options & Recommendation

### The Problem

You have (or will have):

- **phyllux.io** — Biomimetic platform, Wave, Mesh, Vault, Core (Netlify from your web repo)
- **MASTERMIND** — Coordination system (needs a home: docs site, landing, repo)
- **BWURM / Content Studio** — Book generation (may have its own site or stay private)
- **ENGENICA** — Polish framework (documented on Phyllux site; could stand alone)
- **Other domains** — Future products

You want: **One place that shows EVERYTHING you offer**, with links to each domain/product.

### Option A: Phyllux Hub (Expand Current)

**Idea:** phyllux.io becomes the hub. Add pages:

- `/products` — List: Phyllux tech, MASTERMIND, BWURM, ENGENICA
- `/products/mastermind` — MASTERMIND landing (or link to GitHub / separate MASTERMIND site)
- `/products/bwurm` — BWURM/Content Studio (if public)
- Keep existing: `/vision`, `/technology`, `/engenica`, `/docs`, etc.

**Pros:** One domain. Simple. Netlify already connected.  
**Cons:** Phyllux-branded. MASTERMIND might deserve its own identity.

### Option B: Master Web Repo (Recommended)

**Idea:** Create a **single repo** that hosts ALL your web presence. Netlify deploys from it. Structure:

```
your-web-repo/                    # e.g. phyllux-technologies-web, or flourish-hub
├── index.html                    # Hub: "What I offer" — links to everything
├── phyllux/                      # Phyllux site (move from your web repo or symlink)
│   ├── index.html
│   ├── vision.html, technology.html, ...
│   └── assets/
├── mastermind/                   # MASTERMIND marketing/landing
│   ├── index.html                # "MASTERMIND — Coordination that improves"
│   ├── docs/                     # Static docs or link to GitHub
│   └── assets/
├── bwurm/                        # BWURM landing (if public)
├── engenica/                     # ENGENICA standalone (or keep in Phyllux)
└── netlify.toml                  # Netlify routes: / → hub, /phyllux → phyllux, etc.
```

**Netlify routing:**

- `yourdomain.com` or `phyllux.io` → hub (index.html)
- `phyllux.io/phyllux/` or subdomain `phyllux.yourdomain.com` → Phyllux
- `phyllux.io/mastermind/` or `mastermind.phyllux.io` → MASTERMIND landing

**Pros:** One repo. One Netlify project (or multi-site). Full control. Easy to add new products.  
**Cons:** Migrate website from your web repo. More upfront work.

### Option C: Fractaled Repo Complex

**Idea:** Master "control" repo that doesn't host sites but **coordinates** them:

- **Master repo** — Contains: site map, deploy scripts, shared assets, coordination docs
- **Product repos** — your web repo (Phyllux), mastermind (MASTERMIND), etc. Each deployed separately
- **Redundancy** — Each product repo is self-contained. If master dies, products still deploy.
- **Master scripts** — `deploy-all.ps1` runs deploy for each product; or each repo has its own Netlify connection

```
master-control-repo/
├── README.md                     # Map of all repos and sites
├── deploy/
│   ├── deploy-phyllux.ps1
│   ├── deploy-mastermind.ps1
│   └── deploy-all.ps1
├── shared-assets/                # Logos, etc. (or each repo has its own)
└── SITE_MAP.md                   # All domains, what lives where
```

**Pros:** Redundancy. Each product independent. Master orchestrates.  
**Cons:** More repos to maintain. Deploy scripts need care.

### Recommendation

**Short term:** Option A — Add a `/products` or `/ecosystem` page to phyllux.io. Link to MASTERMIND (GitHub or a simple landing). Minimal change.

**Medium term:** Option B — Create `phyllux-technologies-web` (or similar) monorepo. Move website content. Add MASTERMIND landing. One source of truth. Netlify serves all from one repo.

**Long term:** Option C — If you add many more products, fractaled structure with master control repo. Redundancy for resilience.

---

## Part 3: Integration Steps (Concrete)

### Phase 1: MASTERMIND Public (Now)

1. Create `mastermind` repo on GitHub (or under phyllux-technologies org)
2. Copy mastermind/ with placeholders. Push. Public.
3. Add link from phyllux.io ecosystem or about: "MASTERMIND — coordination system"

### Phase 2: Hub Page on Phyllux (This Week)

1. Add `ecosystem.html` or `products.html` to `workspace/website/` (you may already have ecosystem.html)
2. Content: Cards or list for Phyllux, MASTERMIND, ENGENICA, BWURM (if public). Each links to its section or external site.
3. Deploy via deploy-to-repo.ps1. Commit. Push. Netlify updates.

### Phase 3: Master Web Repo (When Ready)

1. Create `phyllux-technologies-web` repo
2. Structure: `/` hub, `/phyllux` Phyllux site, `/mastermind` MASTERMIND landing
3. Copy `workspace/website/` → `phyllux-technologies-web/phyllux/`
4. Create simple MASTERMIND landing in `phyllux-technologies-web/mastermind/`
5. Configure Netlify to serve from this repo. Point phyllux.io (or your hub domain) to it.
6. Deprecate or redirect your web repo website content (or keep prior art; web moves to new repo)

### Phase 4: Fractaled (Optional, Future)

1. Create `phyllux-master` or `flourish-control` repo
2. Add deploy scripts, SITE_MAP.md, coordination docs
3. Each product repo: own Netlify site or subdomain. Master repo documents the map.

---

## Part 4: Redundancy & Resilience

- **Backup:** Git is your backup. Push to GitHub. Consider private mirror.
- **Secrets:** Never in repo. Use Netlify env vars, local .env, secrets vault.
- **Domain:** Point phyllux.io to Netlify. Add MASTERMIND subdomain or path as needed.
- **Independence:** Each product (Phyllux, MASTERMIND) should work if the other is down. No hard cross-dependencies in deployment.

---

## Part 5: Summary — Your Next 5 Actions

1. **Create MASTERMIND GitHub repo** — Copy mastermind/, sanitize, push, public.
2. **Add ecosystem/products page to phyllux.io** — Link to MASTERMIND, ENGENICA, BWURM.
3. **Run mm check** — Before any MASTERMIND publish.
4. **Complete Rollout Checklist** — 03_DEPLOYMENT.md.
5. **Decide:** Stay with your web repo for web, or plan migration to master web repo (Phase 3).

---

*Rollout & Web Ecosystem Strategy. Last updated: February 2026.*
