---
layout: post
title: "Stress test your documents with AI stakeholder perspectives"
date: 2026-01-08
ai: assisted
---

There's a specific dread to presenting a budget proposal. You know your material. You've done the work. But somewhere in that document is a gap you can't see - and your CFO will find it in the first five minutes. 

The problem: I'm too close to my own work. I know what I mean, but will they see the gaps? Will I walk into a meeting and get blindsided by "what's the ROI on this?" or "what happens if you're hit by a bus?

So I tried something: before presenting to real stakeholders, I had AI review the document *as* those stakeholders.

This is inspired by the same logic behind Andrej Karpathy's [LLM Council](https://github.com/karpathy/llm-council) - multiple perspectives catch what a single viewpoint misses. Karpathy uses different AI models reviewing each other's work. I'm using one model [Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5) wearing different hats (prompts).

## The technique

Instead of asking AI to "review this document" (which gives generic feedback), I asked it to adopt specific perspectives. Each one sees your document through a different lens:

**Chairman / Board Member**
Thinks about governance, risk, and whether this is a sound investment. Will ask: "What happens if this fails? What's the contingency? Is this the right use of capital?" Catches missing risk registers, vague success metrics, and proposals that don't tie back to business strategy.

**CFO / Finance**
Follows the money. Wants to see total cost of ownership, not just the ask. Will ask: "What's the ROI? What's the payback period? What are the ongoing costs?" Catches missing budget figures, hidden costs, and proposals that don't quantify benefits.

**COO / Operations**
Thinks about execution and day-to-day impact. Will ask: "How does this affect the business? Who supports this? What's the rollout plan?" Catches unrealistic timelines, missing support models, and change management gaps.

**External CTO / Technical Advisor**
Brings industry perspective and technical rigour. Will ask: "Is this architecture sound? How does this compare to industry benchmarks? What's the technical debt situation?" Catches over-engineering, under-engineering, and approaches that don't match company scale.

**Business Owner / Founder**
Cares about the business holistically. Will ask: "Does this make our people more productive? What's the risk if we don't do this? Are we investing enough or too much?" Catches proposals that are IT-centric rather than business-aligned.

**CISO / Security**
Thinks about risk, compliance, and what could go wrong. Will ask: "What's the attack surface? How does this affect our compliance posture? What data is exposed?" Catches security gaps, compliance blind spots, and proposals that create technical debt in the name of speed.

**Chaos Agent**
Deliberately adversarial. Assumes your proposal will fail and works backwards. Will ask: "Why won't this work? What are you not telling me? What's the weakest assumption here?" Catches optimistic projections, unstated risks, and confirmation bias. This one is powerful - it forces you to defend your own logic.

Here's an example prompt for the Chaos Agent:

```
You are a deliberately adversarial reviewer. Your job is to assume this proposal will fail and work backwards to explain why.

Review this document with deep skepticism. Attack the weakest assumptions. Find the gaps the author is hoping nobody notices.

Focus on:
- Optimistic projections that lack evidence
- Dependencies that could break the entire plan
- Risks that are downplayed or missing entirely
- What happens when key people leave, budgets get cut, or timelines slip
- The question the author is most afraid of being asked

Do not be polite. Do not hedge. If something is weak, say it's weak. If an assumption is unsupported, call it out directly.

End with: "The single most likely reason this fails is..."
```

Each perspective catches different things. A CFO notices missing budget figures. A CTO flags that your DR/BCP section is vague. A COO asks how you'll support 300 users with 2 IT staff.


## What I found

I ran 9 perspective reviews across 5 document versions. Here's what the first round caught:

| Perspective | Gaps Found |
|-------------|------------|
| Chairman | Budget missing, staffing plan vague, no ROI articulation |
| CTO | DR/BCP targets undefined, key person risk not addressed |
| COO | Onboarding automation in wrong quarter, support model missing |
| Business Owner | Engineer productivity section absent, no governance model |

Every single one of these would have come up in the actual meeting. Instead of getting blindsided, I addressed them in advance.

The document went from a technical delivery plan to a business-aligned strategy. Version 1 was "here's what IT will do." Version 5 was "here's what IT needs to deliver this, here's the investment required, here are the risks, here are the decisions we need from you."


## Tips

- **Be specific about context** - Company size, growth trajectory, industry all matter
- **Ask for criticism explicitly** - "Be critical" gets better feedback than "please review"
- **Run perspectives in parallel** - No need to do them sequentially 
- **Look for patterns** - If 4 out of 5 perspectives flag the same gap, fix it
- **Don't over-rotate** - You know your stakeholders better than the AI does

This won't replace real stakeholder feedback. But it's a useful step before you walk into the room. Catch the obvious gaps first, so the real conversation can focus on the hard questions.
