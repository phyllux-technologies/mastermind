# Setup — How to Set Up MASTERMIND

**Purpose:** Configure MASTERMIND for your workspace and projects.

---

## Step 1: Copy the Pilot File

Copy `mastermind/mastermind.md` to your workspace root:

```bash
# From workspace root
cp mastermind/mastermind.md ./mastermind.md
```

Or on Windows:
```
copy mastermind\mastermind.md mastermind.md
```

Your workspace root should now have `mastermind.md` alongside your projects and the `mastermind/` folder.

---

## Step 2: Configure Your Mission

1. Copy `config/mission.example.md` to `config/mission.md`.
2. Edit `config/mission.md` to define your mission — what you're working toward, what "improvement" means for you.
3. Optionally, reference it in `core/projects/_registry.md`.

---

## Step 3: Configure Your Projects

1. Open `core/projects/_registry.md`.
2. Replace the placeholder projects (Project_A, Project_B) with your actual projects.
3. For each project, specify:
   - **Path** — Relative to workspace root (e.g., `projects/MyApp`, `00_ACTIVE/Website`)
   - **Role** — What the project does; why it matters
   - **Master** — Path to the project's main doc (README.md, master.md, etc.)
4. Create `core/projects/[PROJECT].md` for each project (use `_template.md` as a starting point).

---

## Step 4: Add MASTERMIND_LINK to Project Roots

For each project, copy `templates/MASTERMIND_LINK.md` to the project root:

```
your-project/
├── MASTERMIND_LINK.md   ← Add this
├── README.md
└── ...
```

Edit the link file to reference your project name in the path: `core/projects/YourProject.md`.

---

## Step 5: Configure Paths (If Needed)

If your layout differs from the default (e.g., MASTERMIND is not at `workspace/mastermind/`):

1. Copy `config/config.example.md` to `config/config.md` or `config/local_config.md`.
2. Update paths to match your structure.
3. Update references in mastermind.md and core files if necessary.

---

## Step 6: Add Cursor Rule (Optional but Recommended)

If you use Cursor IDE, create `.cursor/rules/mastermind.mdc` in your workspace root:

```markdown
---
description: MASTERMIND coordination — read mastermind.md for "new idea" or cross-project work
globs: ["mastermind.md", "mastermind/**", "**/MASTERMIND_LINK.md"]
---

# MASTERMIND Coordination

When working on mastermind.md, mastermind/, or MASTERMIND_LINK.md, or when the user says "new idea", "improve the system", or "read mastermind":

1. Read mastermind.md first.
2. For new idea: Add to mastermind/core/memory/main_memory.md → run mastermind/core/processes/improvement_propagation.md.
3. For improve the system: Follow mastermind.md §4.
4. Totality check before finishing.
```

---

## Verify Setup

- [ ] mastermind.md at workspace root
- [ ] config/mission.md customized
- [ ] core/projects/_registry.md lists your projects
- [ ] core/projects/[PROJECT].md exists for each project
- [ ] MASTERMIND_LINK.md in each project root
- [ ] Cursor rule added (if using Cursor)

---

## Next Step

→ [03_DEPLOYMENT.md](03_DEPLOYMENT.md) — Deploy locally, with a team, or as a repo.

---

*MASTERMIND Setup. Last updated: February 2026.*
