---
layout: post
title: "The BRIEF framework: how to get genuinely useful output from AI"
date: 2026-02-28
ai: written
---

Most people's experience with AI goes like this: type something vague into ChatGPT, get something generic back, conclude AI is overrated. The problem isn't the AI. It's the input.

The difference between "AI gives me rubbish" and "AI gives me something I can actually use" is almost always the quality of what you give it to work with. I've been working on a simple framework to make that difference concrete -- something I could share with others that takes about 60 seconds to learn and immediately changes the output.

## The briefing metaphor

Imagine you've just hired a sharp new employee. They're capable, they work fast, and they'll do exactly what you ask. But they've never met your customers, don't know your industry, haven't seen your templates, and have zero context about the situation.

If you say "write me an email," you'll get a generic email that could have come from any business on earth. If you brief them properly -- the situation, what you need, who it's for, what good looks like, and what to avoid -- you'll get something useful.

AI works exactly the same way. The quality of the output is directly proportional to the quality of the brief.

## Why I built BRIEF

The most popular prompting framework out there is CRAFT -- Context, Role, Ask, Format, Tone. It was a reasonable starting point. But the research has moved past it, and I kept running into the same problems: the "Role" element doesn't actually work the way people think it does, and the framework doesn't account for what the research says matters most.

[Wharton's Generative AI Lab](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5324706) tested expert personas ("Act as a senior accountant") across six AI models with roughly 5,000 runs per model. The result: **no statistically significant improvement in accuracy from persona assignment** in five of the six models tested. Telling AI to "be an expert" doesn't make it smarter. It changes the style, not the substance.

What does work? [Anthropic's documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) recommends explaining *why* you need something -- the AI generalises from the explanation far better than from a costume. And [Microsoft Research](https://arxiv.org/abs/2505.02832) found that AI performance drops by about 39% in multi-turn conversations compared to getting everything in one message.

So I built a replacement. Something grounded in the actual evidence, structured around how AI actually works, and simple enough to teach anyone in a minute. I call it BRIEF -- because that's exactly what you're doing. Writing a brief, not a prompt.

## BRIEF: write a brief, not a prompt

| Element | What it means |
|---------|--------------|
| **B**ackground | The situation, context, and any relevant information -- documents, data, history, constraints |
| **R**esult | What specifically you want. Be precise and literal -- the AI will take you at your word |
| **I**ntent | Why you need it and who will read or use the output |
| **E**xample | One or two examples of what good output looks like |
| **F**ence | Boundaries -- what to avoid, length limits, format requirements, things that would make it wrong |

Every element earns its place through evidence:

- **Background** addresses the context engineering shift. All major AI vendors rank context as the single biggest determinant of output quality.
- **Result** addresses specificity -- the most reliably validated technique across all the research.
- **Intent** replaces Role with something that actually improves output. Explaining *why* and *for whom* shapes the response more reliably than "act as a..."
- **Example** is the most underused technique. Every vendor recommends 1-2 examples for format alignment. Diminishing returns after 3-4.
- **Fence** covers the gap that most frameworks miss -- boundaries and constraints are as important as instructions.

## Worked example 1: trades -- reviewing a scope of works

**Without BRIEF:**
> Review this scope of works for a switchboard upgrade.

The AI will give you a generic summary. Useless.

**With BRIEF:**

> **Background:** I run a small electrical business in Brisbane doing residential and light commercial work. A builder has sent me a scope of works for a switchboard upgrade at a new townhouse development -- 6 units, each requiring a new board with safety switch, smoke alarm circuits, and EV charger provision. The builder has a history of claiming things were in scope when they weren't.
>
> **Result:** Review this scope of works and identify anything vague, missing, or likely to cause a variation dispute.
>
> **Intent:** This is for me to raise with the builder before I quote. I want to lock down the scope so there are no surprises. I need to know exactly what's included and what's not before I commit to a price.
>
> **Example:** A gap might look like: "No mention of existing switchboard condition -- if removal and disposal is required, that's a variation." Or: "EV charger provision is listed but cable run distance is not specified -- this could vary by $800 per unit."
>
> **Fence:** Format as a numbered list sorted by financial risk (highest first). Be direct -- no waffle. Don't rewrite the scope, just flag the problems.
>
> [Paste the scope of works document here]

The output will flag specific risks: ambiguous cable run distances, undefined disposal requirements, missing detail on smoke alarm interconnection, no mention of meter board access arrangements. Each one is a potential variation dispute you'd catch before quoting, not after.

## Worked example 2: professional services -- drafting an engagement letter

**Without BRIEF:**
> Write an engagement letter for a new accounting client.

Generic boilerplate. Every firm has a dozen of these already.

**With BRIEF:**

> **Background:** I'm a partner at a mid-tier accounting firm in Brisbane. We've taken on a new client -- a family trust with a corporate trustee, approximately $4M turnover, three beneficiaries. The client is considering a restructure to improve asset protection and is also behind on their FY25 tax returns. First meeting went well but the client seemed unclear on what our role would be versus their lawyer's.
>
> **Result:** Draft an engagement letter covering both the overdue tax returns and the initial restructure scoping work. Include fees, scope, exclusions, and standard terms.
>
> **Intent:** This is going directly to the client. They're new to the firm, detail-oriented, and need clear boundaries on what we're covering versus what needs legal advice. Getting the scope right upfront prevents scope creep later.
>
> **Example:** Our engagement letters typically open with a brief summary of the agreed scope, then break into sections: Services, Fees, Exclusions, Terms, and Acceptance. Fees are quoted as a range for the tax returns and hourly for the restructure scoping.
>
> **Fence:** Keep under two pages. Use professional but accessible language -- this client is not an accountant. Do not provide legal advice or recommend a specific restructure option. Make clear that legal advice on the restructure is the client's responsibility. Reference the Tax Practitioners Board Code of Professional Conduct where relevant.

The output gives you a structured letter that covers scope boundaries, differentiates your role from the lawyer's, quotes fees appropriately, and reads like something your firm would actually send. You'll still review every word -- but you started 80% done instead of staring at a blank page.

## Worked example 3: retail/hospo -- responding to a negative Google review

**Without BRIEF:**
> Write a response to a negative Google review.

Corporate-sounding damage control. The kind of response that makes people trust you less, not more.

**With BRIEF:**

> **Background:** I own a casual Italian restaurant in the Brisbane suburbs. A customer left a 2-star review saying they waited 40 minutes for mains on a Saturday night and the waiter seemed disinterested. We were short-staffed that night -- two call-ins. The food itself wasn't mentioned negatively.
>
> **Result:** Draft a response to this review.
>
> **Intent:** This response will be read by the reviewer, but more importantly by every future customer who reads our reviews before deciding where to eat. I need to show we take it seriously without being defensive. I want them to come back, and I want other readers to see a business that genuinely cares.
>
> **Example:** Our review responses are always first-person from "Marco" (me). They're short, honest, and sound like a real person -- not a PR team. Something like: "Appreciate you telling us -- Saturday was rough and your experience wasn't what we aim for."
>
> **Fence:** Under 80 words. Don't make excuses about the staffing situation -- own it. Don't offer a discount (cheapens the brand). Do invite them back personally. Sound genuine, not corporate. No "we strive to provide the best experience" language.

The output sounds like a real person who gives a damn. Short, honest, and human. That's the response that makes future customers trust you -- not the corporate template.

## Common mistakes

**Treating the output as final.** AI gives you a first draft. Always. Review it, edit it, add your expertise. This is especially true for anything with compliance, legal, clinical, or financial implications.

**Not checking facts.** AI invents things confidently. It fabricates Australian Standards numbers, makes up case law, gets addresses wrong, and hallucinates statistics. Anything factual needs verification.

**Skipping the Background.** The B in BRIEF does 80% of the heavy lifting. Most people skip it entirely, then wonder why the output is generic. The more relevant context you provide, the better the output. Every time.

**Having a back-and-forth conversation instead of one good brief.** Microsoft Research found a 39% performance drop in multi-turn conversations. Don't drip-feed information across multiple messages. Put everything in one comprehensive brief. If the AI goes wrong, start a new conversation rather than trying to correct course.

## The three principles

Whatever framework you use, these three findings from the research matter most:

**1. Front-load everything.** Give the AI everything it needs in your first message. One comprehensive brief beats ten short messages.

**2. Explain why, not who.** "This is for a nervous first-time client who needs reassurance" works better than "You are a senior consultant." Purpose shapes the output. Personas don't improve accuracy.

**3. Start fresh when it goes wrong.** If the AI has misunderstood, don't try to steer it back. Open a new conversation, paste your brief with a note about what to avoid, and let it start clean.

## Try it now

Pick a real task sitting on your desk right now. Not a test -- something you actually need to do. Draft the BRIEF:

1. **Background:** What's the situation?
2. **Result:** What specifically do you want?
3. **Intent:** Why do you need it and who's it for?
4. **Example:** What does good look like?
5. **Fence:** What should the AI avoid?

Paste it into ChatGPT, Claude, or whatever tool you have open. Compare the output to what you'd get from "write me an email."

The difference will be obvious.
