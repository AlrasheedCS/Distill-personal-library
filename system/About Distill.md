---
type: guide
summary: "What Distill is for, what goes in it, and how it relates to your other vaults."
---

# About Distill

**Distill is your AI library: mainly AI chats and AI searches and research, plus finds from your feed (mostly X bookmarks) for your projects and setups, and your Readwise highlights.**

1. **AI chats** (most of it): conversations with ChatGPT, Codex, Claude and Claude Code worth keeping, each with a full transcript and a short, high-signal note: what it was about, its main insight, every prompt with its answer de-bloated.
2. **AI searches and research**: outputs from searches you ran with Grok, ChatGPT and others (on X and the web) and saved somewhere like Apple Notes. No chat link, so they're kept apart from chats.
3. **Finds from your feed**, mostly X bookmarks: posts, threads, repos and tools about your projects, workflows and setups, with your own take. Each find is a small note in `sources/finds/` and shows up on the projects it serves.
4. **Projects** you research with AI: each project note gathers its chats, finds, ideas and your notes.

The useful know-how from all three becomes how-tos and prompts.

It is not where you write, think long-form or build projects. Those have their own vaults.

## What goes in

- **Chats you approved**: you asked to save one, or ticked it on an import list. Nothing comes in automatically.
- **Their transcripts**, word for word, never edited.
- **AI searches and research** you hand over, in `sources/searches/` (original kept word for word in `raw/`).
- **Occasional finds from X or the web**, in `sources/finds/`.
- **How-tos and prompts** you kept from those chats.
- **The AI's layer** (`agent/`): topic maps, open questions, cross-chat patterns, and drafts waiting for your review.

## What doesn't go in

- Important, timeless notes and tips → **your notes vault** (you decide what goes there).
- Your own writing, articles, life notes, general reading and quotes → **your notes vault**. (Here only the X or web finds that belong with your AI chats and research.)
- Coding projects in detail (decisions, checks, sessions, handoffs) → **your coding vault**.
- Code itself → its own repository, never a vault.

## The three vaults

| Vault | It holds | In one line |
| --- | --- | --- |
| **Your notes vault** | Your thinking, writing, life, reference, your own prompt library and ideas | **You** |
| **Distill (Chats)** (this one) | AI chats (mainly), AI searches and research, occasional finds from X and elsewhere, plus how-tos and prompts drawn from them | **Your AI library** |
| **Your coding vault** | Coding and CS projects: goals, decisions, checks, sessions, handoffs | **Your code work** |

How they connect:
- Another vault links to a chat here with `obsidian://open?vault=Distill&file=<path>`.
- A project hub in your coding vault links the chats that shaped it; Your notes vault keeps a one-line record of each project.
- Chats stay here even when they're about writing or code; the other vaults link to them instead of copying them.
- All three use the same line labels: `[source]` · `[inferred]` · `[mine]` (plus `[verified]` here).

> [!note]- Still to decide
> Whether ideas, prompts and how-tos drawn from chats should be promoted into **your notes vault** (one home for your own material) instead of Distill's own `ideas/`, `prompts/` and `howto/`. If so, those folders here can be scaled back; see [[system/Scale back]].

## Where to go next

[[Home]] · [[system/How this vault works|How this vault works]] · [[system/Index|Index]] · [[system/Features|Features]] · [[AGENTS]]
