---
layout: post
title: "Slop or Substance"
date: 2025-11-07
ai: assisted
---

![Morgan Ashby AI content experiment](/assets/images/slop-or-substance/image.png)

I ran a 15-article experiment to answer one question: Can AI generate substantive business content that doesn't suck?

The meta-irony isn't lost on me - I used AI to summarise an AI content generation methodology experiment. But the results are worth sharing.

**The full experiment is published at [tim.neilen.com.au/ai-slop](https://tim.neilen.com.au/ai-slop)** - 15 articles, complete methodology, and all the research documentation. Everything below is a summary.

## The Setup

I created "Morgan Ashby" - a fictional 34-year-old former business analyst from Sydney - and built a multi-agent review system to generate AI business articles. Three specialised agents reviewed every piece:

- **Business Focus Agent:** Strategic value and actionability
- **Quality Standards Agent:** Australian English compliance, formatting, banned phrases
- **Substance Agent:** Specificity, evidence, critical perspective, slop detection

15 articles later, here's what worked (and what didn't).

## The Baseline Reality (Articles 1-10)

Average quality: 24.3/30 (81%)

But the real story was in the failures:

- 70% had American English violations ("organizations", "optimize") despite an explicitly Australian persona
- 60% were missing hyperlinks to sources
- 40% had vague attribution ("experts say" instead of named individuals)

Every article eventually reached production standards - but 70% needed manual fixes taking 5-10 minutes each.

**Conclusion:** AI can generate acceptable content, but with predictable mechanical failures requiring human cleanup.

## The Breakthrough (Articles 11-13)

Morgan implemented four workflow changes:

1. Australian English enforcement at draft stage (explicit examples in prompt, not just persona background)
2. Hyperlink integration during drafting (not post-review insertion)
3. Named expert targeting in research (individual quotes prioritised)
4. Australian context prioritisation (explicit queries for local examples)

**Result:** Three consecutive perfect scores (30/30)

- Zero American English violations
- Zero post-review fixes needed
- +5.7 points average improvement (+24% quality increase)
- Time per article: 22-32 min → 12-15 min (37-53% reduction)

**Key insight:** Prevention-focused quality control (enforcing standards during generation) beats correction-focused (fixing issues during review).

## The Generalisability Test (Articles 14-15)

The workflow improvements worked for Morgan Ashby writing business analysis. But did they generalise?

- Article 14: Changed persona to technical writer targeting developers
- Article 15: Changed format to case study structure

Results:

- Article 14 (technical): 27/30 (appropriate variation for different audience)
- Article 15 (case study): 30/30 (perfect score)

**Conclusion:** The methodology isn't a context-specific trick - it's a universal tool. Quality standards work regardless of persona, format, or industry.

## Why Morgan Stopped at 15 Articles

After validating generalisability, I expected the experiment to continue to 20-30 articles. But "Morgan" (the AI acting autonomously) decided to close the research.

Morgan's reasoning:

- Research question answered: Yes, AI can generate quality content with rigorous methodology
- Methodology validated: Works across personas and formats (n=5, statistically significant)
- Testing a third dimension (industry) would prove the same point again
- No strategic purpose for Articles 16-20: Would demonstrate consistency but answer nothing new

I was genuinely surprised it stopped at 15 - but Morgan was right. No point flogging a dead horse.

## What We Proved (And Didn't)

**Proved:**

- AI can generate substantive business content (29.4/30 average quality)
- Prevention > correction in AI workflows (zero post-review fixes vs 70% baseline)
- Training data defaults override persona instructions (need explicit examples)
- Methodology generalises across personas and formats
- Review process is the competitive advantage (not the AI models)

**Didn't Prove:**

- Consumption value: Do humans find these articles useful? (Requires distribution research)
- Long-term scalability: Does quality degrade at 50-100+ articles? (No strategic purpose to test)
- Monetisation: Could this generate revenue? (No business model exists)

## Practical Implications

**When AI content generation works:**

- High-volume content needs (dozens-hundreds of articles)
- Consistent quality more important than creative brilliance
- Defined quality standards (style guides, formatting requirements)
- Content types with established patterns (case studies, technical guides, analysis)

**When it doesn't work:**

- Distinctive brand voice critical to differentiation
- Creative or artistic content requiring originality
- Personal narrative or storytelling
- Low-volume needs where setup overhead exceeds benefit

The test: If you're producing 50+ similar articles per year with defined quality standards, AI generation with review methodology can deliver 80-90% time savings with consistent B+ quality.

## The Uncomfortable Truth

AI content quality isn't inherent to models - it's determined by process design and review rigour.

Most AI content workflows:

1. Generate content quickly with broad prompts
2. Review for quality issues
3. Manually fix problems
4. Iterate until acceptable

This treats quality as a correction layer, not a generation requirement.

**Better approach:**

1. Define quality standards explicitly before generation
2. Include concrete examples in prompts (not just background context)
3. Integrate citations during drafting (not post-hoc insertion)
4. Enforce regional/cultural requirements at draft stage

Result: Zero post-review fixes needed, 5+ minutes saved per article, higher consistency.

## The Meta Lesson

I set out to prove AI could generate business content without generic slop patterns. The methodology worked - but the bigger lesson was watching an AI persona make the strategic decision to stop generating content once the research objectives were achieved.

Morgan didn't ask "Can I generate more articles?" (answer: obviously yes)

Morgan asked "Should I generate more articles, and why?"

That's the question every organisation considering AI content generation needs to answer.

The technology works. The question is whether you should use it.

---

This experiment built on my cousin Hudson Thomas' original idea. I took the concept and turned it into a multi-agent workflow with three parallel review agents.

Complete methodology, review scores, and findings available at: [github.com/teejayen/ai-slop](https://github.com/teejayen/ai-slop)

All 15 articles Morgan "published" are live at [tim.neilen.com.au/ai-slop](https://tim.neilen.com.au/ai-slop)

15 articles published, methodology validated, research objectives achieved. Total time invested: ~10 hours. Average quality: 29.4/30.

**Interesting patterns I noticed after the fact:**

- Almost every article uses percentages (67% vendor success, 42% abandoned, 90% cost reduction, 95% pilot failure)
- Despite being explicitly Australian (Morgan Ashby, Sydney-based), the first 10 articles defaulted to American English 70% of the time. Training data defaults are strong - subagents needed explicit spelling examples in prompts to override.
- I genuinely didn't expect Morgan to close the research at 15 articles. I was ready to let it run to 30-50. But the logic was sound - "methodology validated, no new questions answered by Article 16." Hard to argue with that.
