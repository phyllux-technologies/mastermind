# Rollout Checklist — MASTERMIND

**Purpose:** One document. Optimized order. For deployers ready to publish MASTERMIND or sell modules.

*MASTERMIND · Full Integration · Modules · Web*

---

## Quick Reference

| Decision | Recommendation | Why |
|----------|----------------|-----|
| **Missions** | Option A: Single mission + sub-goals | Fast. Edit one file. Works today. |
| **Merchant** | Gumroad or LemonSqueezy | Easiest. No code. First product in hours. |
| **Web** | Add MASTERMIND link to your site | Minimal change. Link to repo + docs. |
| **First win** | MASTERMIND repo public + link | Proves the path. Builds momentum. |

---

## Phase 1: Core Rollout

### Step 1.1: Create Mission File

Copy `config/mission.example.md` → `config/mission.md`. Edit with your missions.

**Example structure:**

```markdown
# Mission

> [Your overarching mission]

## Sub-missions
- **Project A:** [Description]
- **Project B:** [Description]
- **MASTERMIND:** Coordination that improves all systems.
```

- [ ] mission.md created and filled

---

### Step 1.2: Create GitHub Repo

1. github.com → New repository
2. Name: `mastermind` or `mastermind-coordination`
3. Private first; public when ready
4. Don't initialize with README (we have one)

**Then run:**

```powershell
cd your-workspace/mastermind
git init
git add .
git status   # Verify no config/mission.md, no secrets
git commit -m "Initial commit: MASTERMIND v0.1.0 — coordination system for improving all work"
git remote add origin https://github.com/[your-org]/mastermind.git
git branch -M main
git push -u origin main
```

Replace `[your-org]` with your GitHub org/username. Replace `your-workspace` with your path.

- [ ] Repo created
- [ ] Pushed to GitHub

---

### Step 1.3: Sanitize Before Public

**Run pre-publish audit:**

```powershell
python mastermind/scripts/mm.py pre-publish
```

Scans for workspace-specific paths and Stripe keys. Exits 1 if issues found.

- [ ] `mm pre-publish` passes (or issues fixed)
- [ ] README repo URL updated when known

---

### Step 1.4: Go Public + Add Link

1. GitHub repo → Settings → Danger zone → Change visibility → Public
2. Add Topics: `productivity` `ai` `coordination` `workflow`
3. Copy repo URL
4. Add link from your website (ecosystem page, products, etc.)

- [ ] Repo public
- [ ] Topics added
- [ ] Link added on your site

---

### Step 1.5: Verify

```powershell
cd your-workspace
python mastermind/scripts/mm.py check
python mastermind/scripts/mm.py sync-links
python mastermind/scripts/mm.py status
```

- [ ] mm check passes
- [ ] sync-links OK
- [ ] No unprocessed ideas in Main Memory

---

## Phase 2: Web + Merchant Prep

### Step 2.1: Products/Ecosystem Page

Add MASTERMIND to your site: repo link, docs, install steps.

- [ ] Site has live MASTERMIND link
- [ ] (Optional) products/ecosystem page

---

### Step 2.2: Choose Merchant Platform

Sign up for one:
- **Gumroad** — gumroad.com. Simple. ~10% + payment fees.
- **LemonSqueezy** — lemonsqueezy.com. Similar. Good for digital.

- [ ] Account created
- [ ] Copy MERCHANT_SETUP_TEMPLATE → MERCHANT_SETUP.md, fill in (add to .gitignore)

---

### Step 2.3: Master Web Repo (Optional)

If you run multiple products from one web repo, plan migration. See docs/ecosystem/07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md.

- [ ] (Deferred) Plan migration
- [ ] (Deferred) Create master web repo

---

## Module Readiness — Never Caught Off Guard

**Goal:** When a customer wants to buy, you have everything ready.

### What Each Module Needs Before You Can Sell It

| Item | Check |
|------|-------|
| README.md | What it does. Install steps. How to use. |
| Delivery package | ZIP or folder. All files. No private paths. |
| Attribution | CREDITS.md. Sources (Pirsig, Quantonics, etc.). |
| Product on Gumroad/LS | Title, description, price. File attached. |
| Test install | You installed it. It works. |
| Refund policy | 14 days (or your choice). Documented. |

### What's Ready Now

| Module | Location | Status |
|--------|----------|--------|
| **_template** | modules/_template/ | Copy this for new modules. |
| **Quality Hierarchy** | modules/quality-hierarchy/ | ✅ Package ready. README, templates, CREDITS. |
| **ENGENICA Polish** | Concept in 03_SELLABLE §7b | Needs: README + how to invoke. |
| **Lexical Chain** | Concept in 03_SELLABLE §7c | Needs: README + concept-extract flow. |
| **DQ/SQ Lens, Care Lens, etc.** | 03_SELLABLE catalog | Use _template. Copy. Fill in. |

**Full catalog:** docs/ecosystem/03_SELLABLE_IMPROVEMENT_MODULES.md §8.  
**Delivery guide:** docs/ecosystem/MODULE_DELIVERY_GUIDE.md.

### Pre-Customer Checklist

- [ ] **First 3 modules packaged** — Quality Hierarchy (done), DQ/SQ Lens, Care Lens.
- [ ] **Gumroad/LS account** — Created. Bank/payout connected.
- [ ] **One test product** — Quality Hierarchy. Upload ZIP. Set price ($19–49).
- [ ] **Test purchase** — Buy your own product. Verify ZIP delivers. Install. Works.
- [ ] **Support email** — Where customers ask questions.
- [ ] **Refund policy** — Written. Linked from product or website.

### How to Package a Module for Sale

1. Go to `modules/quality-hierarchy/` (or your module folder).
2. Zip the folder: `quality-hierarchy.zip` (no parent path).
3. Gumroad/LS: Create product → Attach ZIP → Set price.
4. Customer pays → Platform sends receipt → ZIP auto-downloads.

**Protection:** See docs/ecosystem/MODULE_PROTECTION.md.

---

## Phase 3: When Selling — First Product

### Step 3.1: Create First Paid Module

**Recommended:** Quality Hierarchy (already packaged).

1. Zip `modules/quality-hierarchy/` → `quality-hierarchy.zip`
2. Gumroad/LS: Create product "MASTERMIND — Quality Hierarchy Module"
3. Attach ZIP. Set price ($19–49). Add description (from README).
4. Add "Buy" link on your site

- [ ] First product created
- [ ] ZIP attached. Auto-delivery on purchase.
- [ ] Buy link on website

---

### Step 3.2: Test

- [ ] Test purchase (use platform test mode)
- [ ] Verify delivery works
- [ ] Refund policy documented

---

## What AI Can Automate vs What You Do

### AI Can Do

| Task | How to Ask |
|------|------------|
| Run mm check, sync-links, status | "Run mm check" or "Verify MASTERMIND structure" |
| Sanitize paths | "Sanitize mastermind for public — replace workspace paths" |
| Create mission.md from template | "Create mission.md with my sub-missions" |
| Fill MERCHANT_SETUP from template | "Create MERCHANT_SETUP.md — I chose Gumroad" |
| Pre-flight audit | "Audit mastermind folder for private content before publish" |
| Generate git commands | "Give me the git commands to push mastermind to [URL]" |
| Create new module from template | "Create module [name] from _template" |
| Zip a module | `python scripts/module-delivery-pack.py quality-hierarchy` |

### You Must Do

| Task | Why |
|------|-----|
| Create GitHub repo | Browser. Your account. |
| Create Gumroad/LemonSqueezy account | Browser. Payment details. |
| Make decisions (missions, merchant, web) | Your judgment. |
| Push to GitHub | Requires your credentials. |
| Test real purchase | Your validation. |

---

## Reference — Where Everything Lives

| Need | Document |
|------|----------|
| Full status (missions, merchant) | docs/ecosystem/09_FULL_SETUP_AND_INTEGRATION_STATUS.md |
| Repo setup, sanitization | REPO_SETUP.md |
| Website integration options | docs/ecosystem/07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md |
| Modules catalog | docs/ecosystem/03_SELLABLE_IMPROVEMENT_MODULES.md |
| Modules delivery, packaging | docs/ecosystem/MODULE_DELIVERY_GUIDE.md |
| Modules protection | docs/ecosystem/MODULE_PROTECTION.md |
| Cross-promo, partnerships | docs/ecosystem/10_CROSS_PROMOTION_AND_PARTNERSHIPS.md |
| How to describe MASTERMIND | docs/HOW_TO_DESCRIBE_MASTERMIND.md |
| Mission example | config/mission.example.md |

---

*Rollout checklist for MASTERMIND. Print. Check off. Win. February 2026.*
