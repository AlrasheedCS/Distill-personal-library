# How this vault works

Distill is your **AI library**: mainly your **ChatGPT, Codex, Claude and Claude Code chats** (what each was about, its main insight, your prompts and what came back), plus **AI searches and research** you ran with Grok, ChatGPT and others, and the occasional **find from X or the web**. The best of it becomes your own **how-tos** and **prompts**. Deep research and article writing live in a different vault.

> [!tip] The short version
> Chats come in only when you approve them → an AI writes a short, scannable note for each → it drafts how-tos and prompts → you keep, edit or skip them.

## The big picture

```text
Your chats (ChatGPT · Codex · Claude · Claude Code)
        │  you approve which ones
        ▼
sources/chats/<app>/raw/   full transcript, never edited
sources/chats/<app>/       one note per chat: About · Main insight · Prompts and answers
   └ projects/<name>/       project chats, with a hub page per project
   └ code/ · codex/         Claude Code and Codex sessions
        │  an AI drafts
        ▼
agent/outputs/             how-to and prompt drafts waiting for you
agent/wiki/                themes that recur across chats
        │  you keep the good ones
        ▼
howto/   prompts/   ideas/   questions/   ← yours
```

This follows Karpathy's "LLM wiki" pattern (raw sources → AI-maintained wiki → index and log) with Steph Ango's addition: your own notes stay separate, and nothing enters them without your review.

## Where things live

| Folder | What's in it | Who writes it |
| --- | --- | --- |
| `sources/chats/chatgpt/` | ChatGPT and Codex chats. Hub: [[ChatGPT home]] | AI, on import |
| `sources/chats/claude/` | Claude and Claude Code chats. Hub: [[Claude home]] | AI, on import |
| `sources/chats/<app>/projects/<name>/` | Chats from a ChatGPT or Claude project, plus a hub page per project. Marked with a **PROJECT** badge | AI, on import |
| `sources/readwise/` | Your Readwise Reader highlights (Books, Articles, Tweets, Podcasts), synced by the Readwise plugin. Read-only for AIs; the same library also syncs to your notes vault | Readwise sync |
| `sources/chats/claude/code/` · `sources/chats/chatgpt/codex/` | Claude Code and Codex sessions, in a lighter format (goal, outcome, decisions, what broke and the fix) with a slim transcript. Marked with a **CODE** badge. Real coding projects get a short note here linking to your coding vault | AI, on import |
| `sources/chats/<app>/raw/` | Full transcripts, word for word | AI, never edited after |
| `sources/searches/` | **Not chats:** research you ran with AI search (Grok, ChatGPT on X and the web) saved from elsewhere; original in `raw/`. Hub: [[sources/searches/Searches]] | AI, when you hand it over |
| `sources/finds/` | Occasional finds from X or the web (threads, posts, pages) that belong with your AI chats and research | You, the Clipper, or an AI when you hand it over |
| `howto/` | Know-how you've kept: setups, workflows, steps that worked | **You** |
| `prompts/` | Reusable prompts you've kept | **You** |
| `ideas/` · `questions/` · `topics/` · `projects/` · `inbox/` | Your own thinking and work | **You** |
| `agent/` | AI drafts (`outputs/`), cross-chat themes (`wiki/`), AI topic maps (`topics/`), open questions (`questions/`), `index.md`, `log.md` | AI |
| `system/` | Guides, templates and examples, table views, clipper template, prompts, scripts, archive | Setup only |
| [[AGENTS]] | The rules every AI follows here | Setup only |

Folders say what a note **is**. Properties and links say what it **relates to**: use `topics` to group chats by subject, not more folders.

## How a chat gets in

> [!important] Only chats you approve
> Nothing is imported automatically. You either ask for a specific chat, or tick it on a list.

| Way | Best for | Gets full text? |
| --- | --- | --- |
| Say **"save this to my vault"** in a Claude chat (desktop app, linked to this Mac) | Claude chats, anytime | ✅ |
| Ask **Codex** to follow [[system/prompts/Save this chat]] | Chats Codex can see | ✅ |
| **Export** from ChatGPT or Claude → an AI lists every chat with tick boxes → you tick → it imports those | Your backlog; ChatGPT in general | ✅ |
| **Web Clipper** button on chatgpt.com or claude.ai | Grabbing a link quickly | Link only; text arrives with the next export |

Chat imports keep notes and text transcripts. Photos, screenshots, downloads and raw export data stay in the original chat/archive outside the vault; use **Open in ChatGPT/Claude** for details. Import a specific attachment only when you ask for it.

Details: [[system/Capture chats]].

## What a chat note looks like

```text
# Title
> Open in Claude / ChatGPT · Full transcript   (link line at the top)
## About            Started as … / Turned into …
## Main insight     the one takeaway
## My highlights    yours: what you highlight yourself (AIs never touch it)
## Prompts and answers
### 1. …            your prompt, word for word → the answer, de-bloated: every option, list, step, number kept
### 2. …            (each prompt folds)
## More             other insights · Unverified claims · next actions · link back
```

Very long chats use a **compact** version instead: About · Main insight · **End result** · **Key insights from the whole chat** · **Turning points** (only the prompts that changed direction).

Claims an AI made without a source go in a yellow **Unverified** box. A chat answer is a lead, not a fact.

## Mark anything

Every chat, how-to, prompt and draft has two fields of yours (in the **Properties** block at the top of the note):
- `review`: `to review` · `reviewed` · `skip`
- `priority`: `high` · `medium` · `low`

Marked notes show up on [[Home]] (**Marked to review**) and in the **To review** and **High priority** views in [[Chats]]. AIs never change your marks.

## Your part: keep, edit or skip

1. Open [[Home]] → **Waiting for you** lists new drafts.
2. Keep the good ones: move a how-to into `howto/`, a prompt into `prompts/`. Edit them into your own words if you like.
3. Tick `tested` on a how-to once you've actually done it and it worked. **How-tos to test** on Home shows the rest.

Ten minutes a week is enough: [[system/Weekly reset]].

See a filled-in example of every template: [[system/template examples/Template examples]].

## Finding things

**[[system/Index]]** lists every note with a one-line summary. **[[agent/questions/Questions asked]]** lists every question you've asked in your chats, by topic, each linked to where you asked it. **[[agent/trails/Trails to follow]]** lists the links your chats pointed to (articles, papers, repos, discussions), by topic, to follow up on. All three are rebuilt by scripts.

**Keepers:** your best-of shelf in `keepers/` ([[keepers/Keepers]]): final findings in any area. Only you change it; AIs only propose candidates.

**Finds:** posts and pages from your feed live in `sources/finds/` (hub [[sources/finds/Finds]]), one note each, and show up on the projects they serve.

**Capture:** the iPhone share sheet and Quick Capture append to [[inbox/to sort]]; say "sort my inbox" and an AI follows [[system/prompts/Sort my inbox]].

**New AI chat?** Start with [[AGENTS]], then [[system/Handoff]] and [[system/Decisions]].

**Projects** live in `projects/`. A chat joins a project through its `projects` property; the project note lists its chats automatically.

> [!info]- Homes, search and views
> - **[[Home]]**: waiting drafts, recent chats, how-tos to test, recently kept, pinned chats.
> - **[[ChatGPT home]]** and **[[Claude home]]**: each app's chats, all / pinned / by project. **[[Chats]]**: every chat.
> - **Omnisearch** (command palette → *Omnisearch: Vault search*): typo-tolerant search, best match first.
> - **Smart Connections** (sidebar, currently off): related notes for whatever you're reading. Turn on in Settings → Community plugins.
> - **Notebook Navigator**: Apple Notes–style browsing with previews, pinned and recent notes.
> - **Quiet Outline** (right sidebar): jump to any heading in a long note; search headings.
> - **Graph view**: a map of how notes link.
> - **Random note**: open a random old note to revisit it (part of the Weekly reset).
> - Search tip: `section:(word)` finds a word inside one section of a long note; `path:"sources/chats/claude"` limits search to a folder.
> - Fold hotkeys: Settings → Hotkeys → search "fold" → assign *Fold all headings and lists* and *Unfold all*.
> - iPhone: use the share sheet → Obsidian to send a link or thought into `inbox/`.
> - Split a note that grew too big: select a section → command palette → *Note composer: Extract current selection*.
> - Headings fold: click the arrow beside any heading. Command palette → *Fold all headings and lists*.

## Several AIs, one rulebook

> [!info]- How AIs behave here
> Every AI (Claude, Codex, others) reads [[AGENTS]] first. Highlights:
> - Writes only to `sources/chats/`, `agent/`; your folders only when you ask.
> - **Their own area (`agent/`):** add and edit freely; delete only with your OK.
> - **Chat notes:** create for approved chats and add to them; rewriting or deleting needs your OK. **Transcripts** are never edited.
> - **Your folders, `system/` and settings:** nothing without your OK.
> - **Asking:** they name the exact files and the change; one yes covers that list (batches are fine). Suggestions can wait in [[agent/outputs/to-delete]].
> - Never changes your chats in ChatGPT or Claude.
> - Signs every action in [[agent/log]] with its name, e.g. "(codex)".
> - Labels every line on AI pages: `[source]` · `[inferred]` · `[mine]` · `[verified]`, the same labels as your notes vault.
> - Backs up (`agent/backups/`) and shows a sample before any batch change, then runs the health check.
> - Never sends `#sensitive` notes to outside services unless you include them.
> - Work one AI at a time to avoid clashes.

## Note states and properties

> [!info]- Status values and properties
> Chat `status`: `inbox` (waiting), `saved` (kept as a link), `distilled` (note written), `archived` (kept, inactive). These are vault states, not ChatGPT's or Claude's archive.
> `chatgpt_project` holds the project name from **either** app (the key kept its old name). `projects` links to your own project notes.
> Full list: [[system/Property guide]].

## Making it better later, or smaller

Ideas worth adding only when needed (qmd search and more): [[system/Improve later]]. Things that overlap or you may not need: [[system/Scale back]].

[[Home]] · [[Start here]] · [[AGENTS]]
