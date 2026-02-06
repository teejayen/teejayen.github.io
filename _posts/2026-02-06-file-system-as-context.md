---
layout: post
title: "File system as context"
date: 2026-02-06
ai: written
---

[Daniel Miessler](https://danielmiessler.com/blog/personal-ai-infrastructure) nailed the framing: your file system becomes your context system.

This changed how I think about AI assistants. Not what model. Not what interface. What *context* -- and where it lives. Others are arriving at the same conclusion independently -- Tim Kellogg with [Strix](https://timkellogg.me/blog/2026/01/09/viable-systems) (git-backed agent memory), LlamaIndex arguing that [files are all you need](https://www.llamaindex.ai/blog/files-are-all-you-need) for agent context. The tooling differs. The principle is the same.

## The old model is copy-paste

Traditional AI workflow: open chat, paste in context, get response, lose everything when the session ends. You're the memory layer. Every conversation starts from zero.

Even "memory" features in consumer AI tools feel like band-aids. The AI decides what to remember. You can't see it, can't edit it, can't version it. A black box that might recall something useful, or might not.

## The new model is file-native

Your file system already knows things. Project structures. READMEs. Decision records. Notes you've accumulated over years. The question isn't "how do I give the AI context" -- it's "how do I let the AI access context that already exists?"

This is what Claude Code gets right. The AI operates on your actual files, not copies of them. State persists in markdown and JSON that you control. When I start a session, Claude reads `state/focus.md` for current priorities, `state/journal.jsonl` for session history, `decisions/` for past reasoning. I don't paste. I don't re-explain. The file system *is* the context.

## Customisation through conversation

The other thing I've come to value: building the agent *with* the agent.

My setup isn't downloaded from a template. It emerged from hundreds of small iterations. I've [written about this evolution before](/2025/12/29/building-arc-a-thinking-partner-that-remembers/) -- it started as procedural slash commands I triggered manually, evolved to declarative skills the model invokes when it recognises the right moment, and now I'm experimenting with multi-agent teams where specialised agents coordinate on complex tasks. Each transition happened the same way: "This workflow isn't working." "What if we tried X?" "That broke Y, let's adjust."

This is only possible with a tool that exposes its own configuration. CLAUDE.md is just a markdown file. Skills are markdown files. Rules are markdown files. When something doesn't work, I can read the instruction that caused the behaviour, edit it, and see the change immediately. The customisation ceiling isn't whatever a product team exposed -- it's whatever you can imagine.

## Hooks: determinism where it matters

The gap between "AI should do this" and "AI reliably does this" is where things break.

[Hooks](https://code.claude.com/docs/en/hooks-guide) close that gap. They're shell commands that execute at specific points -- before tool use, after tool use, at session start, at session end. Deterministic control over non-deterministic behaviour.

Here's a concrete one. I maintain both public and private repositories. Some context -- employer names, private ventures, personal details -- should never leak into a public commit. Rather than relying on the AI to remember this, a pre-commit hook enforces it:

```bash
SENSITIVE_TERMS=("employer-name" "private-venture" "home-suburb")
STAGED=$(git diff --cached --name-only --diff-filter=ACM)

for term in "${SENSITIVE_TERMS[@]}"; do
    if echo "$STAGED" | xargs grep -l -i "$term" 2>/dev/null; then
        echo "BLOCKED: '$term' found in staged files" >&2
        exit 2
    fi
done
```

The AI can't bypass this. If a sensitive term appears in a staged file, the commit is blocked. The AI gets feedback explaining why, and adjusts. At session start, a different hook runs a Python script that checks for stale inbox items and surfaces open threads from the last conversation -- context loaded deterministically, not left to the model's judgment.

The principle: let the AI be creative where creativity helps, but enforce rules where rules matter.

## Git is for context, not just code

Session transcripts, state files, decision records, the instructions that shape the AI's behaviour -- all versioned. All diffable.

This matters when things go wrong. "The AI gave bad advice" is not debuggable. "The AI gave bad advice because `state/focus.md` showed outdated priorities" is. You can't git diff a chat history stored in someone else's database. But you can trace a file-native system the same way you'd trace a bug in code -- read the state at that point in time, understand what the AI saw, fix the input.

## The interface is the file system

The file system isn't a storage layer for AI context. It's the *interface* -- the shared surface where human knowledge and AI capability meet. Structure your files well, and the AI becomes a genuine collaborator with access to your actual knowledge.

Not a chat window you paste into. Not a black box that might remember. A file system that both of you can read, write, reason about, and debug when things go wrong.

If you're working with AI tools that operate on your file system: start treating your files as context, not just storage. Write a README that's actually for the AI. Put your decisions in markdown. Version your state. The returns compound -- every file you structure well makes the next conversation better.
