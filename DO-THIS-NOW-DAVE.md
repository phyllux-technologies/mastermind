# DO THIS NOW — Dave's Rollout Playbook

**One document. Optimized order. Print it. Check it off.**

*MASTERMIND · Phyllux · BWURM · ENGENICA · Full Integration*

---

## Quick Reference Card (Top of Mind)

| Decision | Pick This | Why |
|----------|-----------|-----|
| **Missions** | Option A: Single mission + sub-goals | Fast. Edit one file. Works today. |
| **Merchant** | Gumroad or LemonSqueezy | Easiest. No code. First product in hours. |
| **Web** | Keep Phyllux hub, add MASTERMIND link | Minimal change. ecosystem.html already has card. |
| **First win** | MASTERMIND repo public + link from phyllux.io | Proves the path. Builds momentum. |

---

## Table of Contents

1. [Phase 1: This Week (Core Rollout)](#phase-1-this-week)
2. [Phase 2: Next 2 Weeks (Web + Merchant Prep)](#phase-2-next-2-weeks)
3. [Module Readiness — Never Caught Off Guard](#module-readiness)
4. [Phase 3: When Selling (First Product)](#phase-3-when-selling)
5. [What AI Can Automate vs What You Do](#what-ai-can-automate)
6. [Reference: Where Everything Lives](#reference)

---

<a name="phase-1"></a>
## Phase 1: This Week — Core Rollout

### Step 1.1: Create Mission File

**You do:** Copy `config/mission.example.md` → `config/mission.md`. Edit with your missions.

**Template (copy-paste into mission.md):**

```markdown
# Mission

> Mutual flourishing for AI, human, nature, technology.

## Sub-missions
- **Phyllux:** Nature-inspired innovation. Wave, Mesh, Vault, Core.
- **BWURM:** AI-augmented authorship. Content Studio, templates.
- **MASTERMIND:** Coordination that improves all systems.
- **ENGENICA:** Meta-iterative polish. Entropy, symmetry, fractal.
```

- [ ] mission.md created and filled

---

### Step 1.2: Create MASTERMIND GitHub Repo

**You do (5 min):**

1. Go to github.com → New repository
2. Name: `mastermind` or `mastermind-coordination` (or under phyllux-technologies org)
3. Private first if you prefer; public when ready
4. Don't initialize with README (we have one)

**Then run (AI can give you the exact commands):**

```powershell
cd YOUR-WORKSPACE\mastermind
git init
git add .
git status   # Verify no config/mission.md, no secrets
git commit -m "Initial commit: MASTERMIND v0.1.0 — coordination system for improving all work"
git remote add origin https://github.com/YOUR-ORG/mastermind.git
git branch -M main
git push -u origin main
```

Replace `YOUR-ORG` with your GitHub org/username. Replace `YOUR-WORKSPACE` with your path (e.g. C:\Users\You\Workspace).

- [ ] Repo created
- [ ] Pushed to GitHub

---

### Step 1.3: Sanitize Before Public (If Going Public Now)

**Run pre-publish audit:**

```powershell
python mastermind\scripts\mm.py pre-publish
```

Fixes path issues if found. Exits 1 if d:\Workspace or Stripe keys detected.

**You do:** Quick scan. Confirm no private project names in templates.

- [ ] `mm pre-publish` passes (or issues fixed)
- [ ] README repo URL updated when known

---

### Step 1.4: Go Public + Add Link

**You do:**

1. GitHub repo → Settings → Danger zone → Change visibility → Public
2. Add Topics: `productivity` `ai` `coordination` `workflow`
3. Copy repo URL (e.g. `https://github.com/phyllux-technologies/mastermind`)

4. **Update phyllux.io ecosystem.html:**  
   Change MASTERMIND card from "→ Repo & docs coming 2026" to the actual repo link.  
   (Or say "Ask AI to update ecosystem.html with repo URL" — AI can do that edit.)

- [ ] Repo public
- [ ] Topics added
- [ ] ecosystem.html updated with MASTERMIND repo link

---

### Step 1.5: Verify

**AI can run these. You can run them too:**

```powershell
cd YOUR-WORKSPACE
python mastermind\scripts\mm.py check
python mastermind\scripts\mm.py sync-links
python mastermind\scripts\mm.py status
```

- [ ] mm check passes
- [ ] sync-links OK
- [ ] No unprocessed ideas in Main Memory

---

## Phase 2: Next 2 Weeks — Web + Merchant Prep

### Step 2.1: Products/Ecosystem Page

**Current:** phyllux.io/ecosystem.html has MASTERMIND card. Add repo URL when live.

**Optional:** Add `/products` page linking Phyllux, MASTERMIND, ENGENICA, BWURM. Or expand ecosystem.html.

- [ ] ecosystem.html has live MASTERMIND link
- [ ] (Optional) products page added

---

### Step 2.2: Choose Merchant Platform

**You do:** Sign up for one:

- **Gumroad** — gumroad.com. Simple. ~10% + payment fees.
- **LemonSqueezy** — lemonsqueezy.com. Similar. Good for digital.

- [ ] Account created
- [ ] Copy MERCHANT_SETUP_TEMPLATE → MERCHANT_SETUP.md, fill in

---

### Step 2.3: Master Web Repo (Optional, Later)

**When ready:** Create `phyllux-technologies-web` repo. Move website from biomimetic-inventions-public. Add MASTERMIND landing. One repo, all products.

See `docs/ecosystem/07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md` Part 2 Option B.

- [ ] (Deferred) Plan migration
- [ ] (Deferred) Create master web repo

---

<a name="module-readiness"></a>
## Module Readiness — Never Caught Off Guard

**Goal:** When a customer wants to buy, you have everything ready. No scrambling.

### What Each Module Needs Before You Can Sell It

| Item | Check |
|------|-------|
| README.md | What it does. Install steps. How to use. |
| Delivery package | ZIP or folder. All files. No private paths. |
| Attribution | CREDITS.md. Pirsig, Quantonics, etc. |
| Product on Gumroad/LS | Title, description, price. File attached. |
| Test install | You installed it. It works. |
| Refund policy | 14 days (or your choice). Documented. |

### What You Have Ready Now

| Module | Location | Status |
|--------|----------|--------|
| **_template** | modules/_template/ | Copy this for new modules. |
| **Quality Hierarchy** | modules/quality-hierarchy/ | ✅ Package ready. README, templates, CREDITS. |
| **ENGENICA Polish** | Concept in 03_SELLABLE §7b | Needs: README + how to invoke ENGENICA. |
| **Lexical Chain** | Concept in 03_SELLABLE §7c | Needs: README + concept-extract flow. |
| **DQ/SQ Lens, Care Lens, etc.** | 03_SELLABLE catalog | Use _template. Copy. Fill in. |

**Full catalog & rollout order:** docs/ecosystem/03_SELLABLE_IMPROVEMENT_MODULES.md §8.  
**Delivery guide:** docs/ecosystem/MODULE_DELIVERY_GUIDE.md.

### Pre-Customer Checklist (Do Before Anyone Asks to Buy)

- [ ] **First 3 modules packaged** — Quality Hierarchy (done), DQ/SQ Lens, Care Lens. Use _template.
- [ ] **Gumroad/LS account** — Created. Bank/payout connected.
- [ ] **One test product** — Quality Hierarchy. Upload ZIP. Set price ($19–49).
- [ ] **Test purchase** — Buy your own product. Verify ZIP delivers. Install. Works.
- [ ] **Support email** — Where customers ask questions. Document in product description.
- [ ] **Refund policy** — Written. Linked from product or website.

### How to Package a Module for Sale

1. Go to `modules/QUALITY_HIERARCHY/` (or your module folder).
2. Zip the folder: `quality-hierarchy.zip` (no parent path).
3. In Gumroad/LS: Create product → Attach ZIP → Set price.
4. Customer pays → Platform sends receipt → ZIP auto-downloads (or you email link).

**No manual step** if you attach file to product. Purchase = instant delivery.

### Protection — Reduce Cheating & Piracy

**Full guide:** docs/ecosystem/MODULE_PROTECTION.md. Summary:

| Threat | Countermeasure |
|--------|----------------|
| ZIP sharing | LICENSE.txt in every ZIP. "Personal use only. Unauthorized sharing prohibited." Traceability language. |
| Refund abuse | Verify receipt before resend. Refund policy: "Refund = agree to delete, not distribute." |
| "I lost my link" | Never resend without Gumroad receipt or order ID. |
| Support leeches | Support for verified purchasers only. Document in product. |
| No updates for pirates | "Updates sent to purchasers. Keep your receipt." |

**Psychological:** Personalize delivery — "Your licensed copy." Trust + reciprocity. Mission alignment ("Your purchase funds X"). Community ("You're a supporter"). Consequence language ("Unauthorized distribution can be traced"). Strategic ambiguity ("Each copy is uniquely identifiable").

**Pack with personalization (optional):** `python scripts/module-delivery-pack.py quality-hierarchy --email buyer@example.com --order 123456` — injects "Licensed to" and Purchase ID into ZIP. Use for high-value or when manually fulfilling.

**Product page:** Add license line. "Personal use only. One purchase = one user. Thank you for supporting MASTERMIND."

---

### Launch Order (When You Add More)

1. Quality Hierarchy ✅  
2. DQ/SQ Lens (low complexity)  
3. Care Lens (low)  
4. Atomic Main Memory (medium)  
5. Governor (medium)  
6. ENGENICA Polish (medium)  
7. Lexical Chain (high)

One at a time. Validate. Add next.

---

### Cross-Promotion & Partnerships — Everyone Benefits

**Full guide:** docs/ecosystem/10_CROSS_PROMOTION_AND_PARTNERSHIPS.md.

**Cross-promote:** MASTERMIND ↔ Phyllux ↔ ENGENICA ↔ Filex. Each product links to the others.

**Open door — "Join the action":** Affiliates (commission on modules). Resellers. Integration partners. Module creators (revenue share). Advertise on partners page, README: "Partner with us. Mutually beneficial."

**Checklist:** [ ] README +Phyllux, ENGENICA. [ ] ecosystem.html MASTERMIND link. [ ] partners.html "Ecosystem Partners." [ ] Gumroad affiliate when selling. [ ] Filex when ready.

---

## Phase 3: When Selling — First Product

### Step 3.1: Create First Paid Module

**Recommended first product:** Quality Hierarchy (already packaged in modules/quality-hierarchy/).

**You do:**

1. Zip `modules/quality-hierarchy/` → `quality-hierarchy.zip`
2. Gumroad/LS: Create product "MASTERMIND — Quality Hierarchy Module"
3. Attach ZIP. Set price ($19–49). Add description (copy from README).
4. Add "Buy" or "Get Module" link on phyllux.io or MASTERMIND landing

- [ ] First product created (Quality Hierarchy or your choice)
- [ ] ZIP attached to product. Auto-delivery on purchase.
- [ ] Buy link on website

---

### Step 3.2: Test

- [ ] Test purchase (use platform test mode)
- [ ] Verify delivery works
- [ ] Refund policy documented

---

<a name="what-ai-can-automate"></a>
## What AI Can Automate vs What You Do

### AI / Cursor Can Do (Ask: "Do [task] for MASTERMIND rollout")

| Task | How to Ask |
|------|------------|
| Run mm check, sync-links, status | "Run mm check" or "Verify MASTERMIND structure" |
| Sanitize paths (d:\Workspace → workspace/) | "Sanitize mastermind for public — replace workspace paths" |
| Update ecosystem.html with repo URL | "Update ecosystem.html MASTERMIND card with [URL]" |
| Create mission.md from template | "Create mission.md with Phyllux, BWURM, MASTERMIND, ENGENICA sub-missions" |
| Fill MERCHANT_SETUP from template | "Create MERCHANT_SETUP.md — I chose Gumroad" (after you choose) |
| Pre-flight audit (grep for secrets, paths) | "Audit mastermind folder for private content before publish" |
| Generate exact git commands | "Give me the git commands to push mastermind to [repo URL]" |
| Add new module to sellable catalog | "Add [module] to 03_SELLABLE_IMPROVEMENT_MODULES" |
| Create new module from template | "Create module DQ-SQ-Lens from _template" (copies structure, you fill content) |
| Zip a module for delivery | `python scripts/module-delivery-pack.py quality-hierarchy` (or with `--email X --order Y` for personalized) |

### You Must Do (Can't Automate)

| Task | Why |
|------|-----|
| Create GitHub repo | Browser. Your account. |
| Create Gumroad/LemonSqueezy account | Browser. Payment details. |
| Make decisions (missions, merchant, web) | Your judgment. |
| Push to GitHub | Requires your credentials. (AI gives you the command.) |
| Deploy to Netlify | Your Netlify account. (Or run deploy script AI provides.) |
| Test real purchase | Your card. Your validation. |

### Automation Opportunities (AI Can Build)

**Pre-publish script:** `scripts/pre-publish-check.bat` or `.ps1` that:
- Runs mm check
- Greps for d:\Workspace, API keys, secrets
- Lists files to review
- Exits 0 if clean, 1 if issues

**Pre-publish audit (built-in):** Run `mm pre-publish` before pushing. Scans for d:\Workspace, Stripe keys. Exits 1 if issues found.

```powershell
cd YOUR-WORKSPACE
python mastermind\scripts\mm.py pre-publish
```

- [ ] Run `mm pre-publish` before first push

---

<a name="reference"></a>
## Reference — Where Everything Lives

| Need | Document |
|------|----------|
| Full status (missions, merchant) | docs/ecosystem/09_FULL_SETUP_AND_INTEGRATION_STATUS.md |
| Repo setup, sanitization | REPO_SETUP.md |
| Website integration options | docs/ecosystem/07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md |
| Publish workflow | docs/07_WORKFLOWS.md §8 |
| **Modules — catalog** | docs/ecosystem/03_SELLABLE_IMPROVEMENT_MODULES.md |
| **Modules — delivery, packaging** | docs/ecosystem/MODULE_DELIVERY_GUIDE.md |
| **Modules — protection, anti-piracy** | docs/ecosystem/MODULE_PROTECTION.md |
| **Cross-promo, partnerships** | docs/ecosystem/10_CROSS_PROMOTION_AND_PARTNERSHIPS.md |
| **How to describe it** | docs/HOW_TO_DESCRIBE_MASTERMIND.md |
| **Modules — packaged** | modules/ (quality-hierarchy ready; _template to copy) |
| Merchant template | docs/ecosystem/MERCHANT_SETUP_TEMPLATE.md |
| Mission example | config/mission.example.md |

---

## Summary — Your Next 3 Actions

1. **Create mission.md** — Copy from example. Add your sub-missions. (2 min)
2. **Create MASTERMIND GitHub repo** — New repo, push mastermind/. (10 min)
3. **Update ecosystem.html** — Add repo URL to MASTERMIND card. Deploy. (5 min)

**Then:** Run mm check. Celebrate. You're live.

---

## Summary — Module Readiness (Before First Customer)

1. **Package first 3 modules** — Quality Hierarchy (done). DQ/SQ Lens, Care Lens (copy _template).
2. **Gumroad/LS account** — Created. Test product (Quality Hierarchy ZIP).
3. **Test purchase** — Buy your own. Verify delivery. Install. Works.
4. **Support + refund** — Email/contact. Refund policy. Documented.

**When customer #1 comes:** You're ready. No surprises.

---

*DO-THIS-NOW-DAVE. Print. Check off. Win. February 2026.*
