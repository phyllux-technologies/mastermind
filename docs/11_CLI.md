# CLI — Command-Line Interface

**Purpose:** Automate common MASTERMIND tasks. Helps the system improve itself.

![CLI commands](../assets/mastermind-cli-commands.png)

---

## Commands

| Command | Purpose |
|---------|---------|
| `mm add "idea"` | Add idea to Main Memory (New/Unprocessed) |
| `mm propagate` | Interactive propagation guide |
| `mm check` | Validate structure; totality check |
| `mm sync-links` | Copy MASTERMIND_LINK to all project roots |
| `mm scan` | Show unprocessed ideas |
| `mm status` | Quick system status |
| `mm pre-publish` | Audit before public push (paths, secrets) |

---

## How to Run

From mastermind/ or workspace root:

```bash
# Windows
mm.bat add "your idea"

# Unix/macOS
./mm add "your idea"

# Or directly
python mastermind/scripts/mm.py add "your idea"
```

---

## Requirements

- Python 3.11+
- No external dependencies (stdlib only)

---

*MASTERMIND CLI. By David Edward Sproule & Cursor AI. Last updated: February 2026.*
