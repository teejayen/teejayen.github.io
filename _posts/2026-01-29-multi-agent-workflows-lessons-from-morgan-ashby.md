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

The system lives in `.claude/commands/` - four markdown files that define the entire workflow:

```
.claude/commands/
  ├── generate-article.md    # Orchestrator (~840 lines)
  ├── review-business.md     # Business focus agent
  ├── review-quality.md      # Quality standards agent
  └── review-substance.md    # Slop detection agent
```

The orchestrator runs an 8-phase workflow:

```
Orchestrator (/generate-article)
    ├── Phase 1: Research & topic selection
    ├── Phase 2: Deep research (WebSearch)
    ├── Phase 3: Draft generation
    ├── Phase 4: Launch parallel review agents
    │       ├── /review-business (0-10 pts)
    │       ├── /review-quality (0-10 pts)
    │       └── /review-substance (0-10 pts)
    ├── Phase 5: Consolidate feedback & revise
    ├── Phase 6: Format for Jekyll & save
    ├── Phase 7: Git commit & push
    └── Phase 8: Output summary with scores
```

Critical instruction in the orchestrator: "DO NOT present draft to user until ALL reviews complete." The parallel agents must finish before consolidation begins.

## The Scoring Rubrics

Each agent scored against specific criteria. Not vibes - structured evaluation.

**Business Focus Agent (0-10 points)**

| Criteria | Points | What it catches |
|----------|--------|-----------------|
| Business relevance | 0-3 | Missing "so what?" for business readers |
| Target audience alignment | 0-2 | Too technical, no strategic framing |
| Strategic insights | 0-3 | No actionable recommendations |
| Real-world examples | 0-2 | All theoretical, no concrete cases |

Red flags: "Purely technical with no business context", "No actionable insights", "Missing ROI discussion"

**Quality Standards Agent (0-10 points)**

| Criteria | Points | What it catches |
|----------|--------|-----------------|
| Australian English | 0-3 | "optimize" instead of "optimise" |
| Banned phrases | 0-2 | "unlock potential", "game-changing" |
| Blog formatting | 0-3 | Missing front matter, bad hierarchy |
| Readability | 0-2 | Walls of text, excessive jargon |

Every American spelling gets flagged. Every banned phrase gets flagged. Zero tolerance.

The banned phrase list includes: "embark on a journey", "unlock potential", "leverage synergy", "paradigm shift", "thought leader", "the future of X is here", and the classic AI slop opener "In today's rapidly evolving landscape..."

**Substance Agent (0-10 points)**

| Criteria | Points | What it catches |
|----------|--------|-----------------|
| Specificity vs vagueness | 0-3 | "Studies show..." without citation |
| Critical perspective | 0-2 | Uncritical hype repetition |
| Depth of analysis | 0-3 | Surface-level description only |
| Evidence and sourcing | 0-2 | "Experts agree..." without naming them |

This agent detects slop patterns: lists without depth, every paragraph starting with "Moreover", excessive buzzwords, no concrete examples. The output literally says "SLOP PATTERNS FOUND" with a list.

## Why Parallel Review?

Sequential review is slow and loses context. By the third revision pass, the AI has forgotten what it was originally trying to say.

Parallel review:

- **Speed**: 3 agents × 2 minutes sequentially = 6 minutes. 3 agents simultaneously = 2-3 minutes. 50-67% time savings on review phase alone.
- **Independence**: Each agent evaluates without being influenced by other feedback. The substance agent doesn't know the quality agent already flagged something.
- **Specificity**: Narrow scope means deeper expertise. The business agent doesn't waste tokens on spelling.

Total workflow time: 12-15 minutes per article (optimised) vs 22-32 minutes (baseline). The parallelisation matters.

## The Persona: Morgan Ashby

Morgan Ashby isn't just a name - it's a complete character definition in `research/persona-morgan-ashby.md`:

- 34-year-old business analyst from Ultimo, Sydney
- BCom (USYD), Grad Dip Data Analytics (UTS)
- 5 years evaluating AI pilots at Tech Central startups
- Key observation: "80% of AI business content is generic slop"
- Interests: Critical tech commentary, single-origin filter coffee, Blue Mountains hiking

The persona drives content decisions. Morgan prefers "real challenges over hype", prioritises Australian angles, avoids listicles and uncritical vendor content.

But here's what I learned: **persona background doesn't override training data defaults**.

Telling the AI "Morgan is Australian" produced American English 70% of the time. The fix was explicit examples in the generation prompt:

```
BEFORE: "Morgan is Australian, use Australian English"

AFTER: "Use Australian English: organisations not organizations,
        whilst not while, optimise not optimize, defence not defense"
```

Result: 30% → 100% Australian English compliance.

Same pattern for sourcing. AI defaults to organisational sources ("McKinsey found...") because they're more common in training data. Explicit instruction to target named individuals fixed it.

## Prevention > Correction

The breakthrough wasn't better review agents. It was building quality requirements into the drafting stage.

**Hyperlinks**: Baseline workflow inserted links during review. Improved workflow captured URLs during research, integrated during drafting. Result: 60% → 100% of articles with proper hyperlinks on first draft.

**Named sources**: Baseline workflow accepted "experts say" and fixed it in review. Improved workflow required named individuals during research phase. Result: 40% → 100% with named expert quotes.

**Australian English**: Baseline workflow flagged American spellings in review. Improved workflow enforced correct spellings at generation. Result: Zero post-review fixes needed.

The principle: every quality requirement you can enforce at generation saves time and improves outcomes. Review should validate, not fix.

## The Results

Baseline (articles 1-10): 24.3/30 average. 70% required manual fixes. 5-10 minutes cleanup per article.

After workflow improvements (articles 11-15): 29.4/30 average. Zero post-review fixes. Three consecutive perfect scores.

The difference: +5.7 points (+24% quality increase), 37-53% time reduction.

## Key Lessons

**1. Narrow agents outperform broad ones**

A single agent evaluating business value, writing quality, AND substance produces mediocre feedback on all three. Three specialised agents produce expert feedback on each.

I've since used this pattern for [stress-testing documents with AI stakeholder perspectives](/2026/01/08/stress-test-documents-with-ai-stakeholder-perspectives/) - a CFO agent finds missing budget figures, a CTO agent flags vague DR/BCP sections, a Chaos Agent attacks your weakest assumptions. Same architecture, different application.

**2. Training data defaults are strong**

Explicit examples beat implicit context every time. Don't describe what you want - show examples of correct output.

**3. Review is the product**

Without the multi-agent review, estimated baseline quality ~20/30. With review: 24-30/30. The review methodology transforms mediocre AI output into production-ready content.

**4. AI finds natural stopping points**

Morgan decided to stop at 15 articles. Reasoning: methodology validated, no new questions to answer. I was ready for 30-50, but the logic was sound.

## What's Changed Since November

Three months in AI time is significant. The patterns I was experimenting with are becoming standard:

- Parallel tool execution is common in agentic frameworks
- Multi-agent orchestration has mature tooling
- "Prevention > correction" is recognised best practice

The Morgan Ashby experiment was early enough to feel novel. Now it's just good practice.

## The Code

The full implementation is at [github.com/teejayen/ai-slop](https://github.com/teejayen/ai-slop):

- `.claude/commands/` - All four agent definitions
- `/research/` - Methodology documentation, persona definition, findings
- `_posts/` - All 15 generated articles

All 15 articles Morgan "published" are live at [tim.neilen.com.au/ai-slop](https://tim.neilen.com.au/ai-slop).

---

The architecture isn't complicated. Orchestrator, parallel specialists, consolidation. The insight is that process design matters more than model capability.

Most AI quality problems aren't model problems. They're workflow problems.
