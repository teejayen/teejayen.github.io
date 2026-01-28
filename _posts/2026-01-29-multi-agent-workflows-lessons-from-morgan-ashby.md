---
layout: post
title: "Multi-agent workflows: lessons from Morgan Ashby"
date: 2026-01-29
ai: assisted
---

Back in November, I ran an experiment called [Slop or Substance](/2025/11/07/slop-or-substance/) - 15 AI-generated articles to test whether rigorous process could produce content that didn't suck. The results were clear: prevention beats correction, and the review process is the competitive advantage.

But I never wrote about the architecture that made it work.

Three months later, agentic AI has moved fast. What felt experimental in November is becoming standard practice. Worth documenting what I learned before it becomes obvious.

## The Architecture

The workflow used an orchestrator pattern with parallel review agents:

```
Orchestrator Agent
    ├── Research topic
    ├── Generate draft
    ├── Launch parallel review agents
    │       ├── Business Focus Agent
    │       ├── Quality Standards Agent
    │       └── Substance Agent
    ├── Consolidate feedback
    └── Save to Jekyll format
```

The orchestrator managed the end-to-end flow. It researched topics, generated drafts, then spawned three specialised review agents simultaneously. Each agent had a narrow focus and scored the draft against specific criteria. The orchestrator collected their feedback, made revisions, and published.

## Why Parallel Review?

The obvious approach is sequential: generate, review, fix, review again. It's how most people use AI today.

The problem: sequential review is slow and loses context. By the third revision pass, the AI has forgotten what it was originally trying to say. Quality degrades.

Parallel review solves this:

- **Speed**: Three agents reviewing simultaneously instead of sequentially
- **Independence**: Each agent evaluates without being influenced by other feedback
- **Specificity**: Narrow scope means deeper expertise in that domain

The Business Focus Agent didn't care about spelling. The Quality Standards Agent didn't evaluate strategic value. Each did one thing well.

## What Each Agent Did

**Business Focus Agent** - evaluated strategic value and actionability. Did the article say something useful? Could a reader act on it? This caught the generic "AI is transforming business" padding that adds nothing.

**Quality Standards Agent** - enforced Australian English, formatting rules, and banned phrases. This is where "organizations" became "organisations" and "leverage" got flagged as corporate jargon. Explicit examples in the prompt were critical - persona background alone wasn't enough to override training data defaults.

**Substance Agent** - the slop detector. Checked for specificity, evidence, named sources, and critical perspective. "Experts say" failed. "Gartner's 2024 analysis found" passed. This agent caught the vague hand-waving that makes most AI content useless.

## The Scoring System

Each agent scored 0-10 on their criteria. Total: 30 points possible.

- 27+: Production ready
- 24-26: Minor fixes needed
- Below 24: Significant revision required

The baseline (articles 1-10) averaged 24.3/30. After workflow improvements, articles 11-15 averaged 29.4/30. The difference wasn't the model - it was the process.

## Key Lessons

**1. Explicit examples beat implicit context**

Telling the AI "Morgan Ashby is Australian" didn't produce Australian English. Providing explicit examples did: "Use 'organisation' not 'organization', 'optimise' not 'optimize'."

Training data defaults are strong. You have to override them explicitly.

**2. Integrate quality at generation, not review**

The breakthrough wasn't better review - it was building quality requirements into the drafting stage. Hyperlinks during drafting, not post-hoc insertion. Named experts targeted in research, not vague attribution fixed later.

Prevention > correction.

**3. Narrow agents outperform broad ones**

A single agent trying to evaluate business value, writing quality, AND substance produces mediocre feedback on all three. Three specialised agents produce expert feedback on each.

The same principle applies to human teams. Specialists beat generalists for defined tasks.

I've since used this pattern for [stress-testing documents with AI stakeholder perspectives](/2026/01/08/stress-test-documents-with-ai-stakeholder-perspectives/) - a CFO agent finds missing budget figures, a CTO agent flags vague DR/BCP sections, a Chaos Agent attacks your weakest assumptions. Same architecture, different application.

**4. Let agents make strategic decisions**

Morgan decided to stop at 15 articles. I was ready for 30-50. But the reasoning was sound: methodology validated, no new questions to answer.

The interesting moment wasn't generating content - it was watching an AI persona conclude that generating more content served no purpose.

## What's Changed Since November

Three months in AI time is a lot. The patterns I was experimenting with are becoming standard:

- Parallel tool execution is now common in agentic frameworks
- Multi-agent orchestration has mature tooling
- "Prevention > correction" is recognised best practice

The Morgan Ashby experiment was early enough to feel novel. Now it's just good practice.

That's how fast this moves.

## The Code

The full implementation is at [github.com/teejayen/ai-slop](https://github.com/teejayen/ai-slop). Claude Code commands in `.claude/commands/` show the workflow automation. The `/research/` directory has detailed methodology documentation.

All 15 articles are published at [tim.neilen.com.au/ai-slop](https://tim.neilen.com.au/ai-slop).

---

The architecture wasn't complicated. Orchestrator, parallel specialists, consolidation. The insight was that process design matters more than model capability.

Most AI quality problems aren't model problems. They're workflow problems.
