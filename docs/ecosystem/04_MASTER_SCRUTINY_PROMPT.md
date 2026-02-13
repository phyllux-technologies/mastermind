# Master Scrutiny Prompt — Full Project Audit & Repair

**Purpose:** Insanely comprehensive prompt for scrutinizing, fixing, and improving the entire MASTERMIND project. Run this on yourself and execute. Include ENGENICA, lexical chain, and all learned concepts. Maximum impact.

**Use:** Give this prompt to an AI agent. The agent then runs through every phase below, documents findings, fixes issues, and acts.

---

## PHASE 0: CONTEXT LOAD

Before acting, read and internalize:

1. **MASTERMIND** — `mastermind/README.md`, `mastermind/core/`, `mastermind/docs/`, `mastermind/docs/ecosystem/`
2. **888** — `888/README.md`, `888/memory/main_memory.md`, `888/processes/improvement_propagation.md`
3. **ENGENICA** — `00_ACTIVE_PROJECTS/ENGENICA/ENGENICA_DOCUMENTATION.md`, `ENGENICA_DOCUMENTATION_VALIDATED.md`
4. **Lexical Chain** — `LEXICAL_CHAIN_EXPLORATION.md`, `00_ACTIVE_PROJECTS/BWURM-7/content-studio/docs/LEXICAL_CHAIN_INTEGRATION.md`
5. **Registry** — `888/projects/_registry.md` — PHYLLUX, BWURM, ENGENICA links
6. **Sellable Modules** — `mastermind/docs/ecosystem/03_SELLABLE_IMPROVEMENT_MODULES.md`
7. **Improvement in Use, Rollout, Meta-system** — `06_IMPROVEMENT_IN_USE.md`, `07_ROLLOUT_AND_WEB_ECOSYSTEM_STRATEGY.md`, `08_SYSTEM_FOR_MASTERMIND_CALIBER_PRODUCTS.md`
8. **All images** — `mastermind/assets/mastermind-*.png`

---

## PHASE 1: SCRUTINIZE DOCUMENTATION

For every `.md` file in `mastermind/`, `888/` (excluding duplicates, archive):

- [ ] **Spelling** — Run spell-check. Fix typos: "improbmets" → "improvements", "improbemts" → "improvements", etc.
- [ ] **Grammar** — Fix fragments, run-ons, agreement errors.
- [ ] **Broken links** — All `[text](path)` resolve. Fix or remove.
- [ ] **Image paths** — All `![](path)` point to existing files. Use `../assets/` or `../../assets/` correctly from doc location.
- [ ] **Consistency** — MASTERMIND vs Mastermind vs mastermind. Pick one (MASTERMIND for product name, mastermind/ for folder).
- [ ] **Outdated refs** — "24 images" → actual count. "45-image plan" → update if expanded.
- [ ] **Missing content** — Gaps, TODOs, placeholders. Fill or mark explicit.

**Output:** `SCRUTINY_REPORT_DOCS.md` with list of fixes applied.

---

## PHASE 2: SCRUTINIZE IMAGES

For every image in `mastermind/assets/mastermind-*.png`:

- [ ] **Spelling in images** — Images with text: check every word. Common errors: "improbmets", "improbemts", "propgate", "propogate", "seperately", "occured", "recieve", "acheive", "thier", "teh", "adn", "taht".
- [ ] **Regenerate if broken** — If spelling error, wrong concept, or visual flaw: regenerate with corrected description. Keep same filename.
- [ ] **Alt text** — Ensure all doc references have meaningful alt text for accessibility.
- [ ] **Consistency** — Color palette (blue, teal), style (clean, minimal), branding.

**Image checklist (sample — apply to all):**
- mastermind-hero.png — "A system that improves all systems" (no typos)
- mastermind-quote-*.png — Quote text correct
- mastermind-module-*.png — Module names correct
- mastermind-social-*.png — Share text correct
- mastermind-inspire-*.png — Inspirational text correct
- mastermind-banner-*.png — Banner text correct
- mastermind-value-*.png — Value prop text correct
- mastermind-cta-*.png — CTA text correct
- mastermind-built-on-*.png — Attribution names correct

**Output:** `SCRUTINY_REPORT_IMAGES.md` with: (1) images checked, (2) images regenerated and why, (3) any deferred.

---

## PHASE 3: SCRUTINIZE CODE

For `mastermind/scripts/mm.py`, `888/scripts/mm.py`:

- [ ] **Logic** — add, propagate, check, sync-links, scan, status. Edge cases.
- [ ] **Encoding** — UTF-8 everywhere. Windows cp1252 safe (use [OK] not ✓).
- [ ] **Paths** — Works for 888 and mastermind layouts. No hardcoded d:\Workspace.
- [ ] **Error handling** — Missing files, empty registry, malformed tables.
- [ ] **Docstrings** — Clear, accurate.

**Output:** Fix inline. Note in report if major changes.

---

## PHASE 4: INTEGRATE ENGENICA

ENGENICA (ACINEgNE backwards) — meta-iterative AI framework. Spectographic analysis (entropy, symmetry, fractal). MoQ, Quantonics. Optimizes PHYLLUX, Content Studio.

**Actions:**

1. **Add ENGENICA to 888 registry** — If not present, add ENGENICA project. Path: `00_ACTIVE_PROJECTS/ENGENICA`.
2. **Add ENGENICA to mastermind sellable modules** — ENGENICA as an optional polish module: run ENGENICA on Main Memory entries or propagated outputs. "ENGENICA Polish" — entropy, symmetry, fractal optimization for text/artifacts.
3. **Document ENGENICA–MASTERMIND link** — In ecosystem strategy or new doc: MASTERMIND coordinates; ENGENICA polishes. Propagation output → ENGENICA optional pass.
4. **Add to module catalog** — `ENGENICA Polish Module` — integrates ENGENICA analysis/polish into propagation pipeline. Premium.

**Output:** Registry update, sellable modules update, new section or doc.

---

## PHASE 5: INTEGRATE LEXICAL CHAIN

Lexical Chain: tools in sequence. Raw → Completeness Validator → ENGENICA → Validator → Utopia → Content Studio → Concept Extractor → Outline → FAQ → Glossary → Index → Convergence → Cycle Guard → Export.

**Concepts to absorb:**

- **Virtuous loop** — Validator + ENGENICA + convergence detect. MASTERMIND propagation IS a virtuous loop. Document the parallel.
- **Concept extraction** — Main Memory ideas could be concept-extracted → outline → FAQ. Novel module: "Lexical Chain for Main Memory."
- **Convergence/cycle guard** — When does propagation stop? Avoid infinite propagation. Governor + convergence logic.
- **Tool chaining** — MASTERMIND as orchestrator. Propagation can invoke: Validator, ENGENICA, Concept Extractor as optional stages.
- **Studio Bridge** — Content Studio already runs Validator+ENGENICA. MASTERMIND could reference this as integration pattern.

**Actions:**

1. **Add "Lexical Chain Module" to sellable modules** — Optional: run concept extractor, outline synthesizer, FAQ generator on Main Memory or propagated docs.
2. **Document virtuous loop parallel** — Improvement Propagation = virtuous loop. Link to lexical chain virtuous_loop.
3. **Governor + convergence** — Governor doc: add convergence/cycle guard concept from lexical chain.
4. **Cross-reference** — MASTERMIND ↔ Content Studio ↔ Lexical Chain. Ecosystem diagram update.

**Output:** Sellable modules update, Governor doc update, ecosystem diagram/text update.

---

## PHASE 6: FIX WHAT'S WRONG

Synthesize findings from Phases 1–5. Create a single TODO list. Execute in order:

1. **Critical** — Broken links, broken images, broken code.
2. **High** — Spelling, grammar, wrong counts, missing ENGENICA/lexical chain.
3. **Medium** — Consistency, alt text, doc polish.
4. **Low** — Nice-to-haves.

Apply every fix. Document in `SCRUTINY_REPORT_FINAL.md`.

---

## PHASE 7: ACT UPON IT

After fixes:

1. **Run `mm check`** — Both 888 and mastermind. Must pass.
2. **Run `mm sync-links`** — MASTERMIND_LINK to all projects.
3. **Add to Main Memory** — "Master Scrutiny executed: ENGENICA and lexical chain integrated; images scrutinized; docs fixed."
4. **Update CHANGELOG** — mastermind/core/CHANGELOG.md, 888/CHANGELOG.md.
5. **Totality check** — Who, What, When, Where, Why, How.

---

## PHASE 8: REGENERATE BAD IMAGES

For each image flagged in Phase 2 with spelling or content errors:

1. Read the current image (or infer from filename and doc context).
2. Write corrected `GenerateImage` description — fix all spelling, improve clarity.
3. Regenerate. Overwrite or replace.
4. Confirm doc references still work.

**Batch:** Do not skip. Quality over speed.

---

## EXECUTION ORDER

```
0. Load context (read all key docs)
1. Scrutinize docs → fix
2. Scrutinize images → list issues → regenerate bad ones
3. Scrutinize code → fix
4. Integrate ENGENICA
5. Integrate lexical chain
6. Fix what's wrong (consolidated)
7. Act (mm check, sync-links, Main Memory, CHANGELOG, totality)
8. Regenerate any remaining bad images
```

---

## SUCCESS CRITERIA

- [ ] No broken links in mastermind/, 888/
- [ ] No spelling errors in docs or image text
- [ ] All images exist and render
- [ ] ENGENICA present in registry and/or sellable modules
- [ ] Lexical chain concepts in sellable modules and Governor
- [ ] mm check passes
- [ ] mm sync-links succeeds
- [ ] CHANGELOG updated
- [ ] Totality check passed

---

*Master Scrutiny Prompt. Run on yourself. Get busy. Last updated: February 2026.*
