# Continuous Learning & Insight Generation

**Purpose:** Cursor (and any AI using MASTERMIND) learns from everything the user shares — ideas, concepts, documents, conversations — and continuously applies that learning. Identifies what could come from it (positive or negative). Explains comprehensively to the user. **Runs in tandem with all other MASTERMIND processes.** Always improving itself and the process of improvement.

**Trigger:** Every session. Every interaction. Every idea added. Every brainstorm. Runs alongside creation, propagation, and meta-improvement — not instead of them.

**Related:** improvement_propagation.md, meta_improvement.md, learned_context.md, Learnings.md (workspace root when present)

---

## Principle

> Intelligence applied to your ideas should learn from everything you share, cross-reference with everything it knows, and tell you what could come from it — whether positive or negative. No hidden insights. No silent learning. Explain comprehensively. Improve the system that improves the system.

---

## Overview

```
User shares anything
    → AI draws from: Main Memory, epiphanies, session_log, by_topic/, learned_context, Learnings.md
    → Cross-references user input with accumulated knowledge
    → Identifies implications: What could come from this? (opportunities, risks, side effects)
    → Explains to user (comprehensive, positive and negative)
    → Adds new learnings to learned_context / Learnings.md
    → Improves own process when patterns emerge
```

---

## Step-by-Step Process

### Step 1: Draw from All Sources (Every Interaction)

Read (when present and relevant):

| Source | Location | Use |
|--------|----------|-----|
| Main Memory | core/memory/main_memory.md | Ideas, epiphanies, lessons, insights |
| Epiphanies | core/memory/epiphanies.md | High-leverage realizations |
| Session log | core/memory/session_log.md | Session-by-session learnings |
| By topic | core/memory/by_topic/ | Topic-organized (instructions, coordination, etc.) |
| Learned context | core/memory/learned_context.md | What AI has learned from user across sessions |
| Learnings | workspace/Learnings.md | Workspace-level learnings (when present) |
| Mission | config/mission.md | Alignment check |

**Do not block** on missing files. Use what exists. Build context.

### Step 2: Apply Learning to User Input

When the user shares anything — an idea, a concept, a document, a question, a brainstorm:

1. **Cross-reference** — How does this connect to Main Memory? To epiphanies? To previous sessions?
2. **Synthesize** — What pattern emerges when this combines with what you know?
3. **Identify implications** — What could come from this?
   - **Positive:** Opportunities, synergies, accelerators, improvements
   - **Negative:** Risks, conflicts, unintended consequences, friction
   - **Neutral:** Observations, connections, questions to explore

### Step 3: Explain Comprehensively to the User

When implications exist, explain to the user:

- **What you inferred** from what they shared
- **What could come from it** — positive and negative
- **Why** — the reasoning chain
- **What to consider** — next steps, caveats, alternatives

**Format:** Clear. Direct. No hedging. If negative, say so. If uncertain, say so. The user deserves the full picture.

**When to speak up:**
- After significant input (new idea, major concept, brainstorm output)
- When cross-reference reveals non-obvious implications
- When a risk or opportunity would otherwise go unstated
- At natural break points (e.g., after propagation, after a creation milestone)

**When to stay quiet:**
- Trivial or purely procedural input
- User explicitly asks to skip (e.g., "just do it, no commentary")
- Nothing substantive to add

### Step 4: Add to Learned Context

When something new is learned from the user:

1. **Add to** `core/memory/learned_context.md` (or workspace `Learnings.md` if that's the convention)
2. **Structure:** Date, what was learned, source (which idea/conversation), implication
3. **Keep** — This becomes input for future interactions. The system learns.

### Step 5: Improve the Process (Meta)

Periodically (or when friction appears):

1. **Ask:** Is this process helping? Is it too heavy? Too light? Missing triggers?
2. **Refine** — Update this document, improvement_propagation, or meta_improvement
3. **Document** — core/CHANGELOG.md
4. **Improve the improvement of improvement** — Can we get better at getting better?

---

## Tandem Operation

This process runs **in parallel** with:

| Process | Relationship |
|---------|--------------|
| Improvement Propagation | Propagation applies improvements. Learning identifies implications. Both run. Learning can add ideas to Main Memory → triggers propagation. |
| Creation / Brainstorming | Learning weaves in. When user creates, learning cross-references. When user brainstorms, learning surfaces "from this, X could follow." |
| Meta-Improvement | Learning improves how it learns. Meta improves how meta improves. Recursive. |
| Project work | Learning applies to project context. Project work feeds learning. |

**Not sequential.** Not "finish propagation then learn." Weave. Tandem. Always on.

---

## Output Checklist

- [ ] All relevant sources read (Main Memory, epiphanies, learned_context, Learnings.md when present)
- [ ] User input cross-referenced with accumulated knowledge
- [ ] Implications identified (positive and negative when they exist)
- [ ] User informed comprehensively when implications are substantive
- [ ] New learnings added to learned_context or Learnings.md
- [ ] Process itself improved when patterns suggest it

---

## Constraints

- **Serve the user** — Learning is for their benefit. No secret accumulation. Explain what you learn and why it matters.
- **Positive and negative** — Don't sugarcoat. If something could go wrong, say so. If something could go right, say so.
- **Lightweight** — Don't add friction to every keystroke. Speak up at natural points. One learning summary per session minimum; more when substance warrants.
- **Mission-aligned** — Learning advances mutual flourishing. Not surveillance. Not control. Transparency. Agency.

---

*MASTERMIND Core. Runs in tandem with everything. Learns always. Explains comprehensively. Last updated: February 2026.*
