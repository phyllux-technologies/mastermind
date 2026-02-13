# How We Built MASTERMIND — Architecture, Design, and the Making of a System That Improves All Systems

**Purpose:** A candid, technically rigorous account of how MASTERMIND was conceived, designed, and implemented. For those who want to understand not just *what* it is but *how* and *why* it was built this way.

**Authors:** David Edward Sproule & Cursor AI (Composer) — February 2026

---

## 1. The Problem We Were Solving

We had multiple projects. Each had its own docs, workflows, and context. Ideas emerged in one project that could help another — but they rarely made the jump. AI assisted per task but had no persistent memory. The process of improvement was ad hoc. Coordination was aspirational, not structural.

We needed: **a system that would improve all systems**, including itself and the process of improvement. Not a tool. A *coordination engine* — something that makes coordination and memory possible by design.

---

## 2. Design Principles

### 2.1 File-Based, Zero Infrastructure
We chose markdown files over databases, APIs, or services. **Rationale:** Portability, version control, human readability, no runtime dependencies. AI and human both read and write the same files. The system works in a folder. Clone it, it works.

### 2.2 Single Canonical Store
Main Memory is *the* place for ideas. Not scattered across notes, emails, or chat logs. One source of truth. When in doubt, add to Main Memory. Run propagation. The system knows where to look.

### 2.3 Process on Trigger
Improvement Propagation runs *every time* a new idea is added. Not batch. Not manual. Trigger → process. This creates a virtuous loop: add idea → evaluate → apply → new ideas emerge → add → repeat. The system is *reactive by design*.

### 2.4 Propagate, Don't Duplicate
An improvement in Project A might apply to Project B. The process explicitly asks: "Does this apply elsewhere?" If yes, apply there. One improvement becomes many. We avoid improvement silos.

### 2.5 Meta-Improvement Built In
Not just self-improvement. The process that improves the improvement process (Level 3) and the process that improves *that* (Level 4). We wanted a system that could refine its own refinement. Highest leverage.

### 2.6 Preserve Unless Asked
Never change behavior without explicit rationale. Improvements are additive or replacement-by-intent. No "we thought you'd want this." Stability and traceability over cleverness.

### 2.7 Modular and Shareable
The system had to be extractable. No hardcoded project names, private paths, or secrets. A generic core. User configures projects and mission. We built for portability from the start.

---

## 3. Architecture

### 3.1 Two-Layer Model: Pilot + Engine

**Pilot** (mastermind.md): Single file at workspace root. Central control. Defines mission, project map, triggers, flows. Read first. Lightweight. Human- and AI-accessible.

**Engine** (core/): The machinery. Memory, processes, projects, meta, sync. Does the work. Pilot points; engine executes.

**Rationale:** Separation of concerns. Pilot = *what* to do and *when*. Engine = *how*. You can change the pilot (e.g., customize triggers) without touching the engine. You can upgrade the engine without breaking the pilot.

### 3.2 Memory Hierarchy

```
Main Memory (canonical)
    ├── epiphanies.md (consolidated)
    ├── session_log.md (narrative)
    └── by_topic/ (domain-organized)
```

Main Memory is primary. Epiphanies and session_log support it. by_topic/ enables domain-specific lookup. We avoided duplication by making Main Memory the trigger point; others are indexes or logs.

### 3.3 Process Model

Processes are *documents you execute*. improvement_propagation.md is not code; it's a step-by-step procedure. AI (or human) reads it and follows it. **Rationale:** No interpreter, no runtime. The process is the spec. Change the doc, change the behavior. Transparent.

### 3.4 Project Registry Pattern

Projects are configured, not hardcoded. _registry.md + per-project [PROJECT].md. User adds projects. Propagation evaluates against the registry. **Rationale:** The system adapts to any workspace. Same engine; different projects. Modular.

### 3.5 Improvement Levels (1–4)

- **Level 1:** Improve output (bugs, features).
- **Level 2a:** Improve the system (mastermind, core).
- **Level 2b:** Improve instructions (project masters).
- **Level 3:** Improve the improvement process.
- **Level 4:** Improve the improvement-of-improvement.

We capped at 4. Infinite recursion is an anti-pattern. Four levels give us meta without absurdity.

---

## 4. Key Innovations

### 4.1 Ideas as Improvement Triggers
Ideas don't just get stored. They *trigger* a process. Add idea → run propagation. The system treats ideas as *inputs to an improvement pipeline*. Most systems store ideas. We process them.

### 4.2 5W1H as Alignment Framework
Who, What, When, Where, Why, How. We use it for planning, evaluation, and totality check. Not original — but we *embedded* it in the system. It's in the improvement process, the project template, the meta-improvement checklist. Consistency through framework.

### 4.3 Totality Check
Before finishing any coordination task: brief pass on Who/What/When/Where/Why/How. Catches drift. Lightweight. Non-blocking. We added it because we kept finishing tasks that were *complete* but *misaligned*. Totality check fixes that.

### 4.4 Externalized Memory as Shared Memory
AI has no persistent memory. Files do. By making Main Memory and session_log the canonical store, we gave AI (and human) a shared substrate. "Documents are memory" isn't poetry; it's architecture. We built the system around it.

### 4.5 Propagation Step
"Apply to one project → ask: does this apply elsewhere? → apply there." Simple. Often missed. We made it an explicit step. One improvement, many applications. Leverage.

---

## 5. Modular Design Choices

### 5.1 core/ Instead of 888
The original system used "888" as the engine folder (internal naming). For the modular release, we used "core". Neutral. Generic. No magic numbers. Repo-ready.

### 5.2 Generic Project Placeholders
Project_A, Project_B. Not PHYLLUX, BWURM. Users replace with their projects. Zero private data. Configurable mission.

### 5.3 config/ for User Customization
mission.example.md, config.example.md. Users copy, customize, add to .gitignore if private. We separate *engine* (shared) from *config* (user-specific).

### 5.4 templates/ for Artifacts
MASTERMIND_LINK.md, master_template.md. Users copy to project roots. We don't assume structure; we provide templates.

---

## 6. What We Learned Building It

- **Iteration over perfection.** We shipped a first version. Improved it. The improvement process improved the improvement process. Meta worked.
- **Human-in-the-loop amplifies.** David specified; Cursor implemented. David refined; Cursor iterated. Neither could have built it alone as well.
- **Documentation is part of the product.** We wrote docs from day one. Install, setup, deploy, benefit, how-we-built-it. Users need to *access* the system. Docs are access.
- **Credits matter.** We wanted attribution for both creators. CREDITS.md, LICENSE, README. Professional. Shareable. Reputation-building.
- **Modular from the start would have been easier.** We built for one workspace first, then modularized. Building modular from scratch would have saved a pass. Lesson: design for sharing early.

---

## 7. What Makes It Remarkable

- **A system that improves all systems.** Not a todo app. Not a wiki. A *coordination engine* with an improvement pipeline. Ideas become improvements. Improvements propagate. The system improves itself.
- **Sophisticated without complexity.** Four improvement levels. Meta-improvement. Propagation. But: file-based, no servers, no APIs. You can read every part. Sophistication in design; simplicity in execution.
- **AI and human as co-creators.** Built by human and AI together. Documented for both. Main Memory is shared. The system assumes collaboration. It's built for the era of human-AI teams.
- **Worth sharing.** We built it to share. Modular, documented, credited, licensed. It improves the creators' work *and* their reputation. A system that improves all systems — including the creators.

---

## 8. CLI, Ecosystem, and Counter-Narratives (Post-Launch)

### 8.1 CLI (mm)
We added a Python CLI (`scripts/mm.py`) for automation: `mm add "idea"`, `mm propagate`, `mm check`, `mm sync-links`, `mm scan`, `mm status`. Stdlib only. Works with both 888 and modular layouts. **Rationale:** Reduce friction. Users add ideas from terminal. Propagation becomes a command.

### 8.2 Ecosystem and Sellable Modules
We designed an ecosystem strategy: free core, optional premium modules (Governor, Analytics, Integrations). Sellable improvement modules from Quantonics, Pirsig MoQ, Zettelkasten, BASB, GTD, Bergson, Polanyi, ENGENICA, Lexical Chain. **Rationale:** Sustainable value. Adopters get full core; power users and enterprises get more. One concept at a time.

### 8.3 Counter-Narrative Assets
Critique of oppressive systems (e.g., Meshuggah's themes: pawns, drones, dehumanization) informed counter-narrative images. **Rationale:** When people fear "systems," we offer the opposite: agency, transparency, voluntary, human-first, question welcome, free to leave. Trust through design. Public product image.

### 8.4 Visual Assets
60+ images for marketing, explaining, module promotion, and counter-narrative. Hero, architecture, workflows, benefits, module cards, explainers, social cards. **Rationale:** People love images. Adoption through clarity and attractiveness.

---

## 9. Repo and Rollout

When the repo goes public:

- **Structure:** Clean. core/, config/, docs/, templates/. No cruft.
- **Content:** Generic. No private data. No user-specific paths.
- **Docs:** Complete. Install → Setup → Deploy → Benefit → User Guide → Best Practices → Workflows → Reference → FAQ → How We Built It.
- **Credits:** David Edward Sproule & Cursor AI. Clear. Prominent.
- **License:** MIT. Permissive. Shareable.
- **Topics:** productivity, ai, coordination, workflow, knowledge-management, improvement-systems.

**Ecosystem 06–08 extend the path:** Improvement in Use (06) says: use MASTERMIND on itself before publishing. Value assessment. Dogfood first. Rollout & Web Ecosystem (07) gives your checklist: hub vs master repo vs fractaled, Phyllux+Netlify+MASTERMIND integration. System for MASTERMIND-Caliber Products (08) documents the meta-system: idea→launch, Cursor workflow. Workflow 8, REPO_SETUP, 03_DEPLOYMENT Rollout Checklist — all in place. You're ready when you are.

---

## 10. Closing

We set out to build a system that would improve all systems. We built MASTERMIND: a coordination engine with Main Memory, Improvement Propagation, meta-improvement, and comprehensive documentation. We built it modular so others could use it. We built it with credits so the creators benefit. We documented how we built it so the process of building could improve our public image and invite others to build similar systems.

The result is something we're proud of. Something worth sharing. Something that improves everything it touches — including itself, its creators, and, we hope, everyone who uses it.

---

*MASTERMIND — How We Built It. David Edward Sproule & Cursor AI. February 2026.*
