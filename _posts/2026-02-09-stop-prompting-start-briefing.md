---
layout: post
title: "Stop prompting AI. Start briefing it."
date: 2026-02-09
ai: written
---

Most people's first experience with AI goes like this: open ChatGPT, type "write me an email," get back something generic and useless, close the tab, conclude AI is overrated.

The problem isn't the AI. It's the input.

The difference between rubbish output and genuinely useful output is almost entirely about what you give it to work with. So I built a framework to make that concrete.

## BRIEF: write a brief, not a prompt

The most popular prompting framework out there is CRAFT -- Context, Role, Ask, Format, Tone. The problem is that [Wharton's Generative AI Lab](https://gail.wharton.upenn.edu/research-and-insights/playing-pretend-expert-personas/) tested the "Role" element across six models with thousands of runs and found no statistically significant improvement in accuracy. Telling AI to "act as an expert" changes the style, not the substance.

What does work? [Anthropic's research](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) shows that explaining *why* you need something shapes the output far more reliably than assigning a persona. And [Microsoft Research](https://www.microsoft.com/en-us/research/publication/llms-get-lost-in-multi-turn-conversation/) found that AI performance drops by about 39% in back-and-forth conversations compared to getting everything in one message.

So I replaced CRAFT with something grounded in the evidence. I call it BRIEF -- because that's exactly what you're doing. You're not writing a prompt for a machine. You're writing a brief for a capable colleague who knows nothing about your situation.

| Element | What it means |
|---------|--------------|
| **B**ackground | The situation, context, and any relevant information -- documents, data, history, constraints |
| **R**esult | What specifically you want -- be precise and literal, the AI will take you at your word |
| **I**ntent | Why you need it and who will read or use the output |
| **E**xample | One or two examples of what good output looks like |
| **F**ence | Boundaries -- what to avoid, length limits, format requirements, things that would make it wrong |

Every element earns its place:

- **Background** does 80% of the heavy lifting. All major AI vendors rank context as the single biggest determinant of output quality. Most people skip it entirely, then wonder why the output is generic.
- **Result** addresses specificity -- the most reliably validated technique across all the research.
- **Intent** replaces Role with something that actually works. Explaining *why* and *for whom* shapes the response more reliably than "act as a..."
- **Example** is the most underused technique. 1-2 examples dramatically improve format alignment. Diminishing returns after 3-4.
- **Fence** covers the gap most frameworks miss entirely. Boundaries and constraints are as important as instructions.

## Example 1: client email for an accounting firm

**Without a brief:**
> Write an email to a client about a new notice of assessment.

Generic, vague, could have come from any firm on earth.

**With a brief:**

> **Background:** I'm an accountant at a small practice in Brisbane. We lodged a client's FY25 tax return three weeks ago. The ATO has issued a notice of assessment showing a $4,200 tax debt due in 21 days. The client is a sole trader (landscaping business) who tends to get stressed about tax bills. They didn't set aside provisional tax because it was a bigger year than expected -- they took on a large commercial contract in Q4.
>
> **Result:** Draft an email letting them know the notice of assessment has come through, what they owe, when it's due, and what their options are.
>
> **Intent:** This client is going to be surprised by the amount. I need the email to be clear and calm -- not alarming. I want them to feel like we're across it and there's a path forward, not like they're in trouble.
>
> **Example:** Our client emails are short, first-name basis, and written in plain English -- not tax jargon. We typically open with the key information, then explain what it means and what to do next.
>
> **Fence:** Don't suggest they should have planned better. Don't go into detail about how provisional tax works (I'll explain on the phone). Don't mention penalties -- there aren't any yet. Keep under 200 words. Mention that a payment plan is available if they need one, but don't push it.

Same AI. Dramatically different output. Because the second version gives it something to work with.

## Example 2: social media for a BJJ gym

**Without a brief:**
> Write a social media post for my gym.

Generic fitness content. Could be any gym, anywhere. "Crush your goals! Join today!"

**With a brief:**

> **Background:** I run a Brazilian Jiu-Jitsu gym in Brisbane's south side. We're a competition-focused club but we get a lot of beginners who are nervous about their first class. Our biggest drop-off is people who enquire but never show up. January is our busiest enquiry month.
>
> **Result:** Write a social media post targeting people who've been thinking about trying BJJ but haven't walked through the door yet.
>
> **Intent:** This is for Instagram and Facebook. The audience is adults (25-45) who are curious but intimidated. I want them to feel like the first class isn't as scary as they think. The goal is to get them to DM us or book a trial.
>
> **Example:** Our best-performing posts are honest and slightly self-deprecating. One that worked well: "Everyone's first roll looks the same -- confused, tired, and wondering why they didn't start sooner." We avoid anything that sounds like a franchise gym.
>
> **Fence:** No "warrior" or "unleash your potential" language. No stock-photo energy. Don't mention pricing. Keep under 100 words. No hashtag spam -- three max.

The output sounds like it came from someone who actually runs a BJJ gym. Because the brief gave it everything it needed to write like one.

## Example 3: reviewing a scope of works for an electrician

This one shows BRIEF isn't just for writing -- it works for analysis too.

**Without a brief:**
> Review this scope of works for a switchboard upgrade.

Generic summary.

**With a brief:**

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

The output flags specific risks: ambiguous cable run distances, undefined disposal requirements, missing detail on smoke alarm interconnection, no mention of meter board access arrangements. Each one is a potential variation dispute you'd catch before quoting, not after.

## Common mistakes

**Treating the output as final.** AI gives you a first draft. Always. Review it, edit it, add your expertise. Especially anything with compliance, legal, clinical, or financial implications.

**Not checking facts.** AI invents things confidently. It fabricates Australian Standards numbers, makes up case law, gets addresses wrong, and hallucinates statistics. Anything factual needs verification.

**Skipping the Background.** The B in BRIEF does 80% of the heavy lifting. The more relevant context you provide, the better the output. Every time.

**Having a back-and-forth instead of one good brief.** Don't drip-feed information across multiple messages. Put everything in one comprehensive brief. If the AI goes wrong, start a new conversation rather than trying to correct course.

## Three principles

**1. Front-load everything.** Give the AI everything it needs in your first message. One comprehensive brief beats ten short messages.

**2. Explain why, not who.** "This is for a nervous first-time client who needs reassurance" works better than "You are a senior consultant." Purpose shapes the output. Personas don't.

**3. Start fresh when it goes wrong.** If the AI has misunderstood, don't try to steer it back. Open a new conversation, paste your brief with a note about what to avoid, and let it start clean.

## The framework is free. The skill is practice.

Almost half of Australians have [recently used a generative AI tool](https://digitalinclusionindex.org.au). Most got underwhelming results - not because the tools don't work, but because nobody showed them how to brief them properly.

The core skill isn't technical. It's the ability to describe what you want clearly enough that someone else could do it. If you can brief a new employee, you can brief an AI. If you can explain a job to a customer, you can explain it to ChatGPT.

BRIEF is five elements. Takes 60 seconds to learn. The difference in output is immediate.
