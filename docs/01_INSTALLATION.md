# Installation — How to Install MASTERMIND

**Purpose:** Get MASTERMIND onto your machine and into your workspace.

---

## Prerequisites

- A workspace (folder) where you keep your projects
- Optional: Cursor IDE (or any AI-assisted editor that can read markdown and follow instructions)
- No special runtimes required — MASTERMIND is file-based (markdown)

---

## Method 1: Clone from Git (Recommended)

```bash
# Navigate to your workspace
cd /path/to/your/workspace

# Clone the MASTERMIND repo (when public)
git clone https://github.com/[your-org]/mastermind.git

# Or, if you have it locally, copy the folder
cp -r /path/to/mastermind ./mastermind
```

---

## Method 2: Copy the Folder

![Install steps](../assets/mastermind-install-steps.png)

1. Download or copy the `mastermind` folder.
2. Place it inside your workspace directory.
3. Your structure should look like:
   ```
   your-workspace/
   ├── mastermind/      ← The MASTERMIND system
   │   ├── core/
   │   ├── config/
   │   ├── docs/
   │   └── ...
   └── your-projects/   ← Your actual projects
   ```

---

## Method 3: Use MASTERMIND as Workspace Root

If you want MASTERMIND to *be* your workspace:

1. Clone or copy into a folder (e.g., `mastermind/`).
2. Your projects live as subfolders (e.g., `mastermind/projects/` or sibling folders).
3. The `mastermind.md` pilot stays at the root of the `mastermind/` folder.
4. Update paths in `core/projects/_registry.md` to match.

---

## Verify Installation

1. **Check structure:** `mastermind/core/memory/main_memory.md` should exist.
2. **Check processes:** `mastermind/core/processes/improvement_propagation.md` should exist.
3. **Check docs:** `mastermind/docs/INDEX.md` should exist.
4. **Run** `mm check` (from workspace root) — validates structure. See [11_CLI](11_CLI.md).

---

## Next Step

→ [02_SETUP.md](02_SETUP.md) — Configure your projects and copy the pilot file.

---

*MASTERMIND Installation. Last updated: February 2026.*
