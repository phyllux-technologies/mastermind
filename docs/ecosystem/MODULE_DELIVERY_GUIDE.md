# Module Delivery Guide — Ready to Ship

**Purpose:** Define what "ready to dish out" means. Ensure no surprises when customers buy. Every module has the same structure.

**Related:** 03_SELLABLE_IMPROVEMENT_MODULES, MERCHANT_SETUP_TEMPLATE, ROLLOUT_CHECKLIST.

---

## What a Customer Gets

**Every module = one ZIP (or private repo link) containing:**

```
module-quality-lens/
├── README.md              # What it does, install steps, 1–2 pages
├── LICENSE.txt            # REQUIRED. Terms. Personal use only. See MODULE_PROTECTION.
├── config/                 # (if module adds config)
│   └── quality-lens.yaml
├── templates/              # (if module adds templates)
│   └── propagation-questions.md
└── CREDITS.md              # Attribution (Pirsig, Quantonics, etc.)
```

**Protection:** Every ZIP must include LICENSE.txt. See docs/ecosystem/MODULE_PROTECTION.md for anti-piracy measures.

**Minimum for any module:** README.md with (1) what it does, (2) how to install, (3) how to use.

---

## Launch Order (Recommended)

From 03_SELLABLE_IMPROVEMENT_MODULES §8. Start with lowest complexity.

| # | Module | Complexity | What to Prepare |
|---|--------|------------|-----------------|
| 1 | **Quality Hierarchy** | Low | Guide + level tags for Main Memory + propagation eval questions |
| 2 | **DQ/SQ Lens** | Low | Guide + DQ/SQ tags + propagation eval questions |
| 3 | **Atomic Main Memory** | Medium | Guide + atomic linking template + propagation tweaks |
| 4 | **Governor** | Medium | Guide + audit/rollback concepts (see 01_GOVERNOR) |
| 5 | **Second Brain Mode** | Medium | Guide + CODE workflow integration |
| 6 | **ENGENICA Polish** | Medium | Guide + how to invoke ENGENICA from propagation |
| 7 | **Lexical Chain for Main Memory** | High | Guide + concept-extract flow + convergence logic |
| 8 | **Care Lens** | Low | Guide + care/attention eval questions |
| 9 | **Flux Mode** | High | Guide + flux concepts, threading |
| 10 | **Tacit Capture** | Low | Guide + prompts, personal/shared tags |

---

## Per-Module Readiness Checklist

**Before you can sell a module, every box must be checked:**

- [ ] **README.md** — What it does (1 para). Install steps (numbered). How to use (brief).
- [ ] **LICENSE.txt** — In every ZIP. Personal use only. No distribution. See MODULE_PROTECTION.
- [ ] **Delivery package** — ZIP or folder. All files. No private paths.
- [ ] **Attribution** — CREDITS or attribution in README. Pirsig, Quantonics, etc.
- [ ] **Product listing** — Gumroad/LS: title, description, price, delivery method.
- [ ] **Test install** — You or a friend installed it. It works.
- [ ] **Refund policy** — Documented (e.g. 14 days, no-questions).

---

## Pricing Suggestions (You Decide)

| Tier | Price Range | Example |
|------|-------------|---------|
| Single module (low complexity) | $19–49 | Quality Hierarchy, Care Lens |
| Single module (medium) | $49–99 | ENGENICA Polish, Governor |
| Single module (high) | $99–149 | Lexical Chain, Flux Mode |
| Bundle (3 modules) | $79–129 | Quality + DQ/SQ + Care |
| All modules | $199–299 | Full pack |

**Start low.** Validate demand. Raise later.

---

## Delivery Flow (When Customer Pays)

1. **Platform sends receipt** — Customer gets email from Gumroad/LS.
2. **You deliver** — Depends on your setup:
   - **ZIP:** Upload ZIP to Gumroad as product file. Auto-delivered.
   - **Link:** Email customer link to Google Drive / Dropbox / private repo.
   - **Repo:** Add customer email to private GitHub repo. Send invite.
3. **Customer downloads** — Unzips. Follows README.
4. **Support** — Email for questions. Or link to FAQ/docs.

**Gumroad/LemonSqueezy:** Can attach file to product. Purchase = instant download. No manual step.

---

## Module Package Template (Copy Per Module)

Create `modules/MODULE_NAME/` with:

**README.md template:**
```markdown
# [Module Name] — MASTERMIND Add-on

Adds [one-sentence value] to your coordination system.

## Install

1. Copy `config/` contents to your MASTERMIND `core/config/modules/`.
2. Add the propagation questions from `templates/` to your improvement_propagation.
3. Restart or re-read as needed.

## Use

[2–3 sentences on how to use it.]

## Attribution

[Pirsig / Quantonics / etc. — credit sources.]
```

**CREDITS.md** — List attributions. Required for Quantonics, Pirsig, etc.

---

## What to Prepare Now (Pre-Customer)

1. **First 3 modules packaged** — Quality Hierarchy, DQ/SQ Lens, Care Lens (all low complexity).
2. **Gumroad/LS account** — Created. One test product.
3. **Delivery tested** — You bought your own product. Got the ZIP. Installed.
4. **Support channel** — Email or simple contact form. Documented.

**When customer #1 comes:** You're ready. No scrambling.

---

*Module Delivery Guide. Last updated: February 2026.*
