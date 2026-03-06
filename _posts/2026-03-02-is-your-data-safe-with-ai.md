---
layout: post
title: "Is your data safe with AI?"
date: 2026-03-02
ai: written
---

> Writing this from Bangkok airport, waiting for my flight to Chiang Mai. I've been thinking about this topic for weeks and the downtime felt like a good excuse to get it out of drafts. This stuff genuinely excites me — helping people get past the fear and into the doing.
>
> This post went through about 30 iterations with Claude before it got here. We went back and forth on the industry examples (cut most of them — they were repetitive), caught a contradiction with my own published work on the [BRIEF framework](/2026/02/09/stop-prompting-start-briefing.html), and tightened the whole thing up. I don't mind being public about that process — it's a good example of what working with AI actually looks like.

"Is my data safe?" comes before everything else. Before "where do I start?" Before "will it replace my staff?" It's the first question — and the right one.

The honest answer is: it depends on which version you're using.

## The two-tier problem

Most AI tools have a free tier and a paid tier. They work differently, and the difference matters.

**Free-tier tools** (ChatGPT Free, Claude Free, Gemini Free) may use your inputs to improve their models. The specifics vary by provider and change over time, but the general principle is the same: if you're not paying, your data may be used for training. The providers are upfront about this in their terms of service  - most people just don't read them.

**Business-tier tools** (ChatGPT Plus/Team/Enterprise, Claude Pro/Team, Microsoft Copilot for 365, Google Gemini Business) contractually guarantee that your data is not used for model training. Your inputs stay private. This is not a grey area - it's a legal commitment backed by enterprise contracts, data processing agreements, and in many cases SOC 2 compliance.

The practical rule is simple: **don't put anything confidential into a free-tier AI tool.** Client names, financial details, patient information, contract terms, employee records, strategic plans - none of it goes into the free version.

A business-tier subscription costs $30-50 per month per user. That's the price of data privacy. For what these tools save in time, it's not even a discussion.

## What "safe" actually means

When people ask "is my data safe?" they're usually asking several different questions at once. Worth separating them.

**"Will the AI learn from my inputs and repeat them to someone else?"**

On business-tier accounts: _most_ likely not. Your inputs are processed to generate a response and then, depending on the provider, either discarded or stored in your private workspace. They don't leak into other users' responses.

On free-tier accounts: your inputs may contribute to model training, which means the *patterns* in your data could theoretically influence future outputs. It's extremely unlikely that your specific client's name or financial details would appear in someone else's response. But "extremely unlikely" isn't the standard you want for confidential information.

**"Is my data stored somewhere I can't control?"**

Business-tier tools store data according to their data processing agreements. For Australian businesses, the key considerations are where the data is processed (usually US-based servers, though some providers offer regional hosting) and how long it's retained. Microsoft Copilot for 365 is notable here - it processes data within your existing Microsoft 365 tenant, subject to your existing data residency settings.

**"Could someone at the AI company read my data?"**

Business-tier providers have access controls and audit processes that prevent casual access. Could an engineer with sufficient access technically see your data? In most architectures, yes - in the same way an engineer at your email provider could technically read your email. The protections are contractual, procedural, and auditable, not absolute.

**"Does this comply with my industry's regulations?"**

This is where it gets industry-specific, and where you need to ~~do your own homework~~ ask AI to do the homework for you. Here's a prompt you can adapt using the [BRIEF framework](/2026/02/09/stop-prompting-start-briefing) — swap out the bracketed details for your situation:

> **Background:** I'm a [role, e.g. practice manager] at a [type of business, e.g. physiotherapy clinic] in [state, e.g. Queensland], Australia. We're considering using AI tools like [e.g. ChatGPT, Claude, Copilot] for [specific tasks, e.g. drafting patient recall messages, summarising clinical notes, writing referral letters].
>
> **Result:** A clear summary of the Australian regulations, professional body guidelines, and state-level legislation that govern how we can use AI tools with our business data — and what each means in practical terms.
>
> **Instructions:** Identify the specific Australian regulations, professional body guidelines, and state-level legislation that govern how we can use AI tools with our business data. For each, explain what it means in practical terms — what we can and can't do. Flag anything that's genuinely risky vs. areas where the rules are clear.
>
> **Examples:** We currently [describe a workflow, e.g. dictate clinical notes into our practice management system and manually write referral letters]. We want to know if using AI to assist with these tasks creates any regulatory exposure.
>
> **Format:** Give me a summary table of regulations and their practical implications, followed by a clear yes/no/maybe for each of our proposed use cases. Plain language — no legalese.

This won't replace legal advice for complex situations. But for most small businesses, it gets you 80% of the way to understanding your obligations in about two minutes.

## What this looks like in practice

The specifics vary by industry, but the pattern is the same: de-identify, use a business-tier account, and keep humans in the loop.

Here's a healthcare example that makes it concrete. A physio needs a referral letter. Instead of pasting in the patient's name, address, and Medicare number, they prompt:

*"Draft a referral letter for a 45-year-old male presenting with chronic lower back pain, L4/L5 disc protrusion confirmed on MRI, conservative treatment for 8 weeks with minimal improvement."*

AI gets everything it needs to write a good letter. No identifiable information leaves the building. The same principle works everywhere — an accountant replaces "Smith Family Trust" with "Client Trust," a real estate agent swaps "42 Boundary Road" with "[property address]," an NFP uses aggregated program data instead of individual participant details.

## The de-identification principle

This is the single most useful rule for AI data safety across every industry:

**The AI doesn't need to know who. It needs to know what.**

Replace names with roles ("the client," "the patient," "the vendor"). Replace addresses with descriptions ("a residential property in Brisbane's eastern suburbs"). Replace dollar amounts with ranges if the exact figure is sensitive.

You get 95% of the output quality with zero confidentiality risk. It takes 30 seconds of find-and-replace before you paste.

## The one-page AI policy

Every business using AI should have a simple internal policy. It doesn't need to be complicated. One page. Cover these five things:

1. **Approved tools.** Which AI tools are staff allowed to use? (Anthropic Claude, Google Gemini, Microsoft Copilot - whatever you've chosen.)
2. **What can go in.** General business tasks, de-identified information, publicly available content, internal process documentation.
3. **What can't go in.** Identified client/patient/customer data, financial details, confidential contract terms, employee personal information, anything subject to legal privilege.
4. **Review requirements.** All AI-generated output must be reviewed by a qualified person before use. AI is a first draft, never a final product.
5. **Responsibility.** Who's accountable if something goes wrong? (Usually: the person who used the tool and the person who approved the output.)

That's it. Print it, pin it up, revisit it every ~~six~~ **three** months as the tools evolve.

## The bottom line

AI data privacy is a solvable problem. It's not a reason to avoid the technology - it's a reason to use it deliberately.

The rules are straightforward:
- Pay for a business-tier account ($30-50/month)
- De-identify confidential information before you paste it in
- Don't put anything into AI that you wouldn't email to an external consultant
- Have a simple policy so your team knows the boundaries
- Review AI output before it goes anywhere

The businesses that figure this out don't avoid AI because of privacy concerns. They use AI confidently because they've addressed the concerns properly.

That's a much better position to be in.
