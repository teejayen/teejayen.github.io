---
layout: post
title: "AI is simple."
date: 2026-02-08
ai: written
---

I find using AI simple. Not the theory -- the practice. Describing what I want, iterating until something works. It feels natural. Like I've been training for this my whole life without knowing what I was training for.

I got my first computer at six. 1996. Some early Windows machine with a CRT monitor that weighed more than I did.

That was the early internet era. IRC channels and dial-up modems. GeoCities websites you built yourself. Napster and LimeWire and hoping the MP3 you downloaded was actually the song it claimed to be. Nothing came with instructions. You figured it out or you didn't.

By 8, I was building websites. By 12, I was the kid teachers asked when the projector wasn't working. Not because I knew anything special -- because I was willing to click around until something happened.

Eighteen years in IT as a career now. Systems administration, infrastructure, cloud migrations, security. Never a developer. Never learned to code properly. But always curious about how things work under the hood. Always willing to break something to understand it.

Here's my hypothesis: **if you grew up in that era -- tinkering, experimenting, comfortable with breaking things -- AI tools feel like a natural extension of what you've always done**.

Not because AI is simple technology. Because the *practice* of using AI maps onto patterns we've already internalised: describe what you want, evaluate the result, iterate, try again. That's the same loop I've been running since I was clicking around Windows 95.

## The terminal is home

The best AI tools live in the terminal. [Claude Code](https://docs.anthropic.com/en/docs/claude-code) -- the one I use daily -- is a command-line tool. That big black box with a blinking cursor where 99% of non-engineers freeze? For people like me, it's where we've always worked.

This matters because Claude Code isn't a chat interface where you type a question and get a response. It's agentic -- it reads your files, writes code, runs tools and commands, catches errors, and iterates. You describe the outcome you want. It figures out how to build it.

The experience is closer to pair programming than prompting. Except your partner has read every piece of documentation, never gets tired, and works at the speed of your description.

For someone who's spent two decades working in terminals, adding Claude to the environment felt less like learning a new tool and more like gaining a very capable colleague who already lives where I work.

## Vibe coding is real

This is what Andrej Karpathy called ["vibe coding"](https://x.com/karpathy/status/1886192184808149383) back in February 2025:

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."

[Collins Dictionary made it Word of the Year 2025](https://en.wikipedia.org/wiki/Vibe_coding). Not because it's a novelty -- because it describes something genuinely new. Non-developers building working software through conversation with AI.

The numbers back it up. In March 2025, Y Combinator's managing partner Jared Friedman [reported](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/) that **a quarter of their Winter 2025 batch had codebases that were 95% AI-generated**. Not hobbyists. Funded startups in the world's most competitive accelerator.

[That cohort grew 10% per week](https://www.cnbc.com/2025/03/15/y-combinator-startups-are-fastest-growing-in-fund-history-because-of-ai.html) -- the fastest in YC's history.

YC CEO Garry Tan: "What that means for founders is that **you don't need a team of 50 or 100 engineers.** You don't have to raise as much. The capital goes much longer."

The economics of building software changed. I'm living inside that change.

## What I've built

A few weeks ago I needed to batch-process 12,000 screenshots through a vision API -- extracting searchable content from years of accumulated screen captures. No vendor makes a tool for this. No off-the-shelf solution exists. Previously, I'd have had the idea and filed it under "would need a developer."

With Claude Code: I described what I wanted, directed the architecture, tested the output, iterated on the problems. Working tool in 30 minutes. [I called it vex](/2026/01/08/ship-tomorrow/). It runs locally. It does exactly what I need.

[Arc](/2025/12/29/building-arc-a-thinking-partner-that-remembers/) is another. A personal thinking partner -- markdown files, JSON state, git-backed persistence, Claude Code as the interface. It holds context between sessions, tracks decisions, detects patterns over time. No vendor builds personal knowledge management the way my brain needs it. So I built it myself.

Neither of these is impressive by a developer's standards. They'd look at the code and see rough edges, shortcuts, patterns they'd never use. That's fine. I'm not trying to be a developer. I'm solving specific problems that no developer was going to solve for me, because the problems are too personal, too niche, and too cheap to justify hiring someone.

That's the unlock though. Not becoming a developer. Becoming someone who can build the specific tools they need, when they need them, without waiting for permission or budget.

## The gap the vendors left

Enterprise software is built for the median customer. It has to be -- vendors need scale to justify the development cost. So you get 80% of what you need and work around the rest. Or you request a feature and wait two years. Or you export to Excel and do the actual work there.

Every industry has these gaps. The report your accounting software can't quite produce. The workflow your project management tool doesn't support. The integration between two systems that would save hours but nobody's going to build for just you.

Previously, filling a gap meant: hire developers, write specs, wait months, pay thousands. The economics only worked if the gap was big enough and the budget was there.

Now? Someone who understands the problem can build the solution in an afternoon. Not a prototype. Working software that solves their specific problem.

**The future isn't everyone using the same software. It's people building their own.**

Not for everything. You're not going to vibe-code an accounting platform. But the small, specific, personal tools that sit in the gaps between the enterprise systems you already use? Those are now buildable by anyone willing to describe what they need and iterate until it works.

## The operator skillset

I've been thinking about what specifically makes someone effective at this. It's not coding ability. I don't have that. It's something different:

**Describing problems clearly.** Eighteen years of writing tickets, specs, and documentation. Articulating what you want -- clearly enough that someone (or something) else could do it -- turns out to be the core skill of AI-assisted development.

**Evaluating output you didn't create.** When Claude Code writes a script, I can't verify every line. But I can evaluate whether the approach is sound, whether the output looks right, and whether the behaviour matches what I asked for. That's systems thinking, not programming.

**Comfort with iteration.** First attempt is never right. Neither is second. Third gets close. Fifth is good. This rhythm is familiar from every infrastructure project, every migration, every troubleshooting session of the last two decades.

**Willingness to break things.** Worst case, I delete the file and start over. This experimental mindset removes the paralysis of needing to get it right the first time. Git makes it cheap. AI makes it fast.

These aren't AI skills. They're the same skills I use debugging a production issue or writing a requirements doc. The difference is that those skills now let me build software -- something that was never on my career path.

## The current state is already enough

**Even if AI development stopped today, the current capabilities would be transformative.**

We're not waiting for AGI. We're not waiting for the next breakthrough. The models that exist right now are already powerful enough to let a non-developer build working tools, automate real workflows, and solve problems that would have required a development team two years ago.

The [biggest blockers to adoption](https://www.oreateai.com/blog/the-genai-divide-state-of-ai-in-business-2025/825dde8f02535e334982136fb473edb7) aren't the models -- they're organisational. Fragmented data pipelines. Low trust in automated outputs. Lack of traceability when things go wrong. Those are solvable problems. The core capability is here.

[Gartner reports](https://www.integrate.io/blog/no-code-transformations-usage-trends/) that 41% of employees are now "business technologists" -- workers outside IT building tech capabilities for business use. That number is going one direction.

The nurse who understands clinical workflows better than any software vendor. The logistics manager who's lived the edge cases. The accountant who knows exactly which reports the enterprise software can't quite produce. These people have always known what software *should* exist. Now they can build it.

## The thirty-year payoff

Using AI well turns out to require the exact skills that a generation of tinkerers built without knowing what they were building toward. Comfort with ambiguity. Willingness to experiment. The ability to describe a problem clearly and iterate toward a solution. No fear of the command line.

Those skills aren't rare because they're difficult. They're rare because most people's relationship with technology has been consumer, not creator. They use software. They don't tinker with it.

That's changing. The tools are getting more accessible. The interfaces are getting more forgiving. The barrier between "I have an idea" and "I have a working tool" has never been lower.

But right now, in this moment, there's an advantage for the people who've been practising this loop -- describe, evaluate, iterate -- for decades without knowing what they were practising for.

I find using AI simple. And I'm pretty sure I've been training for it since 1996.
