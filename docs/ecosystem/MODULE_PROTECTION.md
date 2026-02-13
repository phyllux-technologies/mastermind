# Module Protection — Reduce Piracy & Cheating

**Purpose:** Identify how people can cheat us, and deploy every practical countermeasure. Technical + psychological + operational. We can't prevent everything, but we make it hard, pointless, and psychologically costly.

**Honest reality:** Digital goods are copyable. Someone who has the ZIP can share it. We focus on: (1) reducing how many people try, (2) reducing how many succeed, (3) making paid purchase the obvious right choice.

---

## Part 1: Attack Vectors — How People Can Screw Us

| Vector | How It Works | Risk Level |
|--------|--------------|------------|
| **ZIP sharing** | Customer A buys. Emails ZIP to friend. Or posts on Discord/Reddit. | High — inherent to digital |
| **Repo leak** | If we use private GitHub, customer shares invite or clones and redistributes. | High if we use repo delivery |
| **Refund abuse** | Buy, download, request refund. Keep the file. | Medium — platforms limit this |
| **Chargeback** | Pay, download, dispute. Get money back. Keep file. | Medium — damages seller rep |
| **Fake "I paid"** | Email support: "I bought but lost the link." Hope we send again without verification. | Low — verify before resend |
| **Social engineering** | "Reviewer" / "influencer" asks for free copy. Shares it. | Low — vet or say no |
| **AI regurgitation** | Someone uses AI to reproduce content from our public catalog descriptions. | Low — our value is packaged, integrated |
| **License key sharing** | If we use keys, someone shares a valid key. | Medium if we add keys later |

**Biggest threat:** ZIP sharing. One purchaser, ten friends get it free. No technical way to stop a file from being copied once delivered.

---

## Part 2: Technical Countermeasures

### 2.1 Personalization (Traceability)

**Every delivered ZIP includes a `LICENSE.txt` with purchaser identity:**

```
MASTERMIND Module — Quality Hierarchy
Licensed to: buyer@email.com
Purchase ID: [Gumroad order number — last 6 digits]
Date: 2026-02-15

This copy is for personal use by the named licensee only.
Unauthorized distribution is prohibited. Your purchase ID is 
embedded here. If this file is shared without payment, we can 
trace it to the original purchaser.
```

**Effect:** Purchaser knows sharing = traceable. Creates psychological barrier. Doesn't stop determined sharer but stops casual "hey I'll send you my copy."

**Implementation:** Don't ship one static ZIP. Generate per-purchase ZIP with LICENSE.txt. Options:
- **Manual:** When order comes in, add LICENSE.txt, re-ZIP, send. (Friction.)
- **Gumroad overrides:** Gumroad allows different files per variant. Create "variant" per purchase? No — that doesn't scale.
- **Post-purchase automation:** Gumroad webhook → script adds LICENSE → uploads to Dropbox/Drive → emails customer. Complex.
- **Practical:** Ship standard ZIP. Add a `LICENSE.txt` that says "Your license is tied to your Gumroad receipt. Retain your receipt." Generic but still establishes terms. For high-value modules ($99+), consider manual personalization for first 50 sales.

**Recommendation:** Start with generic LICENSE.txt in every ZIP. Add personalization script when volume justifies it.

### 2.2 Watermarking

**Structured:** Embed purchaser email in a comment or metadata inside a config file. Human-readable. "If you share, we know who."

**Steganographic:** Hide in image or binary. Overkill for markdown. Skip.

**Recommendation:** For modules with config YAML, add `# Licensed to: [email]` at top. Generated at delivery. Deters casual sharing.

### 2.3 Time-Limited Download Links

**Gumroad/LemonSqueezy:** Some platforms allow download links to expire (e.g. 30 days). Customer must download before expiry. If they don't, they can request a new link (we verify purchase).

**Effect:** Reduces "I'll just share the Gumroad link" — link dies. They'd have to share the downloaded ZIP. Still possible, but one more step.

**Recommendation:** Enable if platform supports. 14–30 day expiry. "Download within 30 days. Request a new link anytime with your receipt."

### 2.4 Avoid Repo Delivery (Initially)

**Private repo per customer** = they get a clone link. Easy to share. Hard to revoke. Skip for $19–49 modules.

**Use ZIP only.** Simpler. No repo-invite management. File is file — but we control what's in it (LICENSE, terms).

### 2.5 Platform Protections

**Gumroad/LemonSqueezy:** They handle payment. We don't expose raw download URLs in public. Customer gets link only after payment. We can't prevent them from sharing the file after download — no platform can.

**Refund policy:** 14 days, no-questions. But: "Refund requests require deletion of the downloaded files. By requesting a refund, you agree you have not and will not retain or distribute the product." (In policy. Hard to enforce. Sets expectation.)

**Chargebacks:** Document everything. Product description clear. Receipt sent. If chargeback, provide evidence. Platforms usually side with seller if we have proof of delivery.

---

## Part 3: Psychological Countermeasures

### 3.1 Personalization = Ownership

**"This copy is yours."** Frame the delivery email: "Your licensed copy of Quality Hierarchy is attached. Thank you for supporting MASTERMIND."

**Effect:** People protect what they "own." Shared copy = "not mine." Reduces impulse to give away "your" thing.

### 3.2 Trust + Reciprocity

**In README or delivery:** "We trust you to use this for personal use only. Your purchase funds mutual flourishing — more modules, better tools, shared prosperity. Unauthorized sharing undermines that. Thank you for being a responsible supporter."

**Effect:** Trust creates reciprocity. Many will honor it. Some won't. Net positive.

### 3.3 Mission Alignment

**"Your purchase funds X."** Be specific. "Funds development of Governor, Lexical Chain, and open-source improvements. Every paid module = more free core work."

**Effect:** Cheaters feel they're stealing from a mission, not a faceless corp. Some will self-deter.

### 3.4 Community Identity

**"You're a MASTERMIND supporter."** Email subject: "Welcome to the MASTERMIND community." Create supporters list (opt-in). "Early supporters get first access to new modules."

**Effect:** In-group. People don't steal from their tribe. Paid customers = tribe. Sharers = betraying tribe.

### 3.5 Consequence Language (Mild Deterrent)

**In LICENSE.txt and product page:** "Unauthorized distribution is prohibited. Violation may result in revocation of access to future products and updates."

**Effect:** Not legally bulletproof but creates "there are consequences" frame. Some will hesitate.

### 3.6 Scarcity / Value

**"Limited early-adopter pricing."** Or "First 100 supporters get lifetime updates."

**Effect:** Paid customers got something "special." Sharing devalues their special status. They're less likely to give that away.

### 3.7 Ease of Paying

**Make $19–49 impulse-level.** One click. No friction. Credit card or PayPal. Done.

**Effect:** If paying is easier than hunting for a pirated copy, many will just pay. Piracy often wins on convenience. We win on convenience.

### 3.8 "We Know" (Strategic Ambiguity)

**Don't say:** "We don't track sharing."  
**Say:** "Each licensed copy is uniquely identifiable. Unauthorized distribution can be traced."

**Effect:** We might not have full tech. But the statement creates uncertainty. Sharers wonder. Deterrent without heavy implementation.

---

## Part 4: Operational Countermeasures

### 4.1 Verify Before Resend

**"I lost my download"** → "Please forward your Gumroad receipt or order confirmation." No receipt = no resend.

**"I paid but never got it"** → Check platform. Verify payment. Resend if genuine. If they're trying to get a free copy, they won't have receipt.

### 4.2 Support for Licensed Users Only

**"Need help with installation?"** — Support email. We respond to paying customers. If someone emails with a question but has no purchase record, we can say: "We'd love to help. This module requires a license. Purchase here: [link]."

**Effect:** Shared ZIP doesn't come with support. Paying = support. Adds value to paid that pirates don't get.

### 4.3 Updates for Licensed Users Only

**"New version 1.1 with X improvement. Reply with your receipt to get the update."**

**Effect:** Pirated copy = no updates. Paying = ongoing value. Strong incentive to pay.

### 4.4 Bundles & Loyalty

**"Buy 3 modules, get the 4th half off."** Or "Supporters who purchased 2+ modules get early access to Lexical Chain."

**Effect:** Repeat purchasers are invested. Less likely to share. We reward loyalty.

---

## Part 5: What to Implement Now

### Must Have (Before First Sale)

| Item | Where | What |
|------|-------|------|
| **LICENSE.txt** | In every module ZIP | Terms. "Personal use only. No distribution. Retain your receipt." |
| **Product page copy** | Gumroad listing | "Licensed for personal use. Unauthorized sharing prohibited." |
| **Verify-before-resend** | Your process | Document: Never resend without receipt/order ID. |
| **Refund policy** | Gumroad + your site | "14 days. Refund = agree to delete files, not distribute." |

### Should Have (First 30 Days)

| Item | What |
|------|------|
| **Personalized LICENSE** | Add purchaser email to LICENSE.txt. Manual for first 20 sales; script later. |
| **Support = licensed only** | Document in product: "Support for verified purchasers." |
| **Updates = licensed only** | "Updates sent to purchasers. Keep your receipt." |
| **Delivery email tone** | Personal. Thank you. "Your copy." Community. |

### Nice to Have (Scale)

| Item | What |
|------|------|
| **Webhook personalization** | Gumroad webhook → script injects email → generates ZIP → sends. |
| **Watermark in config** | `# Licensed to: email` in YAML for modules that have config. |
| **Opt-in supporters list** | Email list. "You're in. Early access." Community. |

---

## Part 6: LICENSE.txt Template (Put in Every ZIP)

```
MASTERMIND Module — [MODULE NAME]
© [YEAR] David Edward Sproule. All rights reserved.

PERSONAL USE ONLY. This module is licensed for use by the 
purchaser only. Unauthorized copying, distribution, or sharing 
is prohibited.

Your purchase supports MASTERMIND development and mutual 
flourishing. Thank you for being a responsible supporter.

Keep your Gumroad/LemonSqueezy receipt. You may need it for 
support, updates, or re-downloads.

Questions: [your support email]
```

---

## Part 7: Product Page Copy (Gumroad/LS)

**Add to description:**

> **License:** Personal use only. One purchase = one user. Unauthorized distribution is prohibited. Your copy is for you. Support and updates are available to verified purchasers. Thank you for supporting MASTERMIND.

---

## Summary

**We can't stop all piracy.** Digital files copy. Accept that.

**We can:**
- Make paying easier and more rewarding than cheating
- Add traceability (LICENSE, personalization) so sharing feels risky
- Use psychology: trust, mission, community, consequences
- Operationally: verify before resend, support for buyers only, updates for buyers only
- Price right: $19–49 = impulse. Friction to find a pirate copy often exceeds $19

**Best defense:** Great product + fair price + community + "we trust you" + mild consequences. Most people will do the right thing. We optimize for the majority.

---

*Module Protection. Last updated: February 2026.*
