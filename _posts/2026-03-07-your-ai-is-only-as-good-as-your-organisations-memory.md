---
layout: post
title: "Your AI is only as good as your organisation's memory"
date: 2026-03-07
ai: written
---

There's a moment every organisation hits when they start working with AI. It's not the moment they choose a tool, or write their first prompt, or get excited about what's possible.

It's the moment someone tries to brief the AI on how the business actually works, and realises nobody can.

Not because the AI is limited. Because the knowledge was never written down.

---

I've spent eighteen years in IT. In that time I've walked into dozens of environments where critical business processes lived in exactly one place: someone's head. The senior engineer who knew why the firewall rules were configured that way. The office manager who knew the real approval workflow, not the one in the policy document. The developer who left six months ago and took the deployment process with them.

This was always a problem. We just learned to work around it. You'd ask the right person, or you'd reverse-engineer it from what was already running, or you'd make your best guess and fix it when something broke.

AI doesn't let you do that anymore.

When you sit down to brief an AI — whether that's writing a system prompt, a CLAUDE.md file, or even just a detailed prompt for a single task — you're forced to articulate things that were previously implicit. The context that "everyone just knows." The exceptions to the documented process. The reasons behind decisions that were made three years ago by someone who's since moved on.

And if you can't articulate it, the AI can't use it. Simple as that.

### The knowledge gap was always there

This is what I find genuinely interesting about AI adoption. The tool doesn't create the gap — it reveals it.

When a business owner tells me "the AI doesn't understand our processes," my first question is always: could a new employee understand them? If you hired someone competent tomorrow and sat them down with your documentation, could they do the job?

Usually the honest answer is no. They'd need months of shadowing, hallway conversations, and learning by getting things wrong. We've just normalised that cost because it's spread out and invisible.

AI compresses that cost into a single, uncomfortable moment: the moment you try to write it down and can't.

### Documentation as infrastructure

I've started thinking about organisational documentation the way I think about infrastructure. Not as a nice-to-have. Not as something you'll get to when things slow down. As load-bearing architecture that everything else depends on.

Your network diagrams, your runbooks, your process documents, your decision logs — these aren't artifacts you produce for compliance or onboarding. They're the memory of the organisation. And like any memory, if you don't maintain it, it degrades.

The businesses I've seen get the most from AI aren't the ones with the most sophisticated tools or the biggest budgets. They're the ones that can actually describe how they work. That's it. That's the competitive advantage.

A five-person trades business with a clear, written process for quoting jobs will get more from AI than a fifty-person firm that runs on tribal knowledge and "just ask Sarah."

### What good organisational memory looks like

It's not a wiki that nobody updates. It's not a SharePoint graveyard. Good organisational memory is:

**Current.** Updated when things change, not quarterly in a review that nobody wants to do. The best approach I've seen is treating documentation like code — if the process changes, the docs change in the same step.

**Specific.** Not "we handle customer complaints promptly" but "complaints received via email go to the support queue, are triaged within 4 hours, and escalated to a team lead if unresolved after 48 hours." The AI doesn't need your mission statement. It needs your method.

**Honest.** Documenting how things actually work, not how you wish they worked. If the real process involves a workaround because the system doesn't support what you need, write down the workaround. That's the process.

**Accessible.** Stored somewhere that both humans and AI tools can reach. Markdown in a git repo. A well-structured shared drive. Plain text beats a locked-down proprietary format every time, because plain text is what AI can actually read.

### The messy middle, again

I keep coming back to this idea of the [messy middle]({% post_url 2026-02-26-the-messy-middle %}). The gap between "AI is amazing" and actually getting value from it in your specific context. Organisational memory is the messy middle. It's not exciting. Nobody's posting LinkedIn carousels about updating their process documentation. But it's the work that makes everything else possible.

When I built [Arc]({% post_url 2025-12-20-open-sourcing-arc %}), my personal thinking partner, the first thing I had to do was write down how I actually think and work. My principles, my preferences, my patterns. Not for the AI's benefit — for mine. The AI just gave me a reason to finally do it.

The same thing happens at the organisational level. AI gives you a reason to finally write down how your business works. Not because the AI demands it, but because trying to use AI without it makes the absence obvious in a way that's hard to ignore.

### Start before you're ready

If you're thinking about AI adoption — or you've already started and it's not clicking — don't start with the tool. Start with the memory.

Pick one process. The one that'd cause the most pain if the person who runs it left tomorrow. Write it down. Not perfectly, not comprehensively. Just honestly. What actually happens, step by step, including the weird bits.

Then do the next one.

You'll find that by the time you've documented three or four core processes, you've already built something more valuable than any AI tool could give you on its own. You've built the foundation that makes every tool — AI or otherwise — actually useful.

Your AI is only as good as what you can tell it. And what you can tell it is only as good as what you've bothered to remember.
