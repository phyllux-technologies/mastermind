# Governor — Safety & Counterbalance System

**Purpose:** Companion to MASTERMIND that provides oversight, audit, rollback, and control. Prevents undesired outcomes from Improvement Propagation. Premium module concept.

**Status:** Design document. For future implementation or partnership.

**Relationship:** Governor counterbalances MASTERMIND. MASTERMIND propagates; Governor governs.

---

## 1. Why Governor Exists

| Risk | Governor Response |
|------|-------------------|
| Propagation applies changes to wrong projects | Audit trail; rollback documentation |
| Too many changes in one run | Thresholds; confirmation gates |
| Unintended side effects | Review gates before high-impact targets |
| "Runaway" propagation | Brakes: max projects per run, mandatory review |
| Compliance / enterprise needs | Audit logs, approval workflows |

Governor does not replace MASTERMIND. It adds a layer of control for users who want it.

---

## 2. Components

### 2.1 Propagation Audit Trail

- **What:** Log every propagation run: timestamp, ideas evaluated, projects targeted, changes applied.
- **Format:** Markdown + optional JSON for machine parsing.
- **Location:** `governor/audit/propagation_YYYY-MM-DD_HHMM.md`
- **Retention:** Configurable. Default: keep all.

### 2.2 Rollback Support

- **What:** Before/after snapshots or change summaries. Instructions for undoing a propagation.
- **How:** Document what was changed. User (or script) reverses manually or via tooling.
- **Scope:** Per-run rollback. Not automatic — deliberate, documented undo.

### 2.3 Thresholds and Brakes

- **Max projects per run:** "Don't touch more than N projects without explicit confirmation."
- **Max new files per run:** Limit scope of automated changes.
- **Protected projects:** List of projects that Governor never auto-modifies. Human-only.
- **Dry-run mode:** Show what *would* happen. No writes. User reviews first.

### 2.4 Review Gates

- **Before propagation to Project X:** Pause. Present summary. Require "yes" to proceed.
- **Configurable:** Per-project or global. "Always review before changing docs/", etc.
- **Integration:** CLI prompts. Future: IDE integration, web dashboard.

### 2.5 Convergence & Cycle Guard (from Lexical Chain)

- **Convergence Detector:** Compare propagation quality across runs. If improvement plateaus (|q_n - q_{n-1}| < ε), stop. Prevents infinite propagation.
- **Cycle Guard:** Track artifact hashes. If output equals a previous input (A → B → A), stop. "We've been here."
- **Source:** Lexical Chain (complete/) — virtuous_loop.py, convergence_detector.py, cycle_guard.py.

### 2.6 Dashboard (Future)

- **View:** Propagation history, audit entries, rollback status.
- **Filter:** By project, date, idea.
- **Actions:** Initiate rollback, export audit.

---

## 3. Governor + MASTERMIND Flow

![Governor as safety wrapper](../../assets/mastermind-governor-safety.png)

```
1. User adds idea to Main Memory
2. User runs "mm propagate" (or Improvement Propagation)
3. GOVERNOR: Check thresholds. Dry-run if configured.
4. GOVERNOR: If review gate → present summary → wait for approval
5. MASTERMIND: Apply improvements (per process)
6. GOVERNOR: Write audit entry. Log changes.
7. GOVERNOR: If rollback needed later → user follows rollback doc
```

Governor wraps MASTERMIND. Does not replace it.

---

## 4. Configuration (Conceptual)

```yaml
# governor/config.example.yaml (conceptual)
thresholds:
  max_projects_per_run: 5
  max_new_files_per_run: 20
  require_confirmation_above: 3

protected_projects: []
  # - "Production"
  # - "Legacy"

review_gates:
  before_projects: []
  dry_run_default: false

audit:
  enabled: true
  retention_days: 365
```

---

## 5. Implementation Phases

| Phase | Scope | Effort |
|-------|-------|--------|
| **1. Audit trail** | Log propagation runs to markdown. No code in MASTERMIND core. Separate script or mm hook. | Low |
| **2. Dry-run** | mm propagate --dry-run. Print what would happen. No writes. | Low |
| **3. Thresholds** | Config file. mm checks before propagating. | Medium |
| **4. Review gates** | Pause before certain projects. CLI prompt. | Medium |
| **5. Rollback docs** | Template for documenting undo steps. Manual. | Low |
| **6. Full Governor module** | Bundled. Installable. Premium. | High |

---

## 6. Positioning

- **For individuals:** Optional. Most won't need it. Power users and cautious adopters will value it.
- **For teams:** Valuable. Shared propagation; need audit and control.
- **For enterprises:** Required. Compliance, change management, approval workflows. Governor addresses that.

**Monetization:** Governor as premium module. Clear value: safety, audit, control.

---

*Governor Design. Part of MASTERMIND Ecosystem. Last updated: February 2026.*
