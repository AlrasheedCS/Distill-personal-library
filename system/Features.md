# Features

Every feature added to this vault, what it does, and what removing it would mean. **Tick "Remove?" on anything you don't like**, then ask an AI: *"remove the features I ticked in Features"*. It will name the exact files before changing anything. For overlaps only, see [[system/Scale back]].

## Structure

| Remove? | Feature | What it does | If removed |
| --- | --- | --- | --- |
| - [ ] | **Chat homes** ([[ChatGPT home]], [[Claude home]]) | One page per app: projects, code sessions, regular chats, pinned | Use [[Chats]] for everything |
| - [ ] | **Per-app chat folders** (`sources/chats/chatgpt/`, `claude/`) | Keeps each app's chats apart | All chats back in one folder; views still work |
| - [ ] | **Project folders + hub pages** (`…/projects/<name>/`) | Project chats grouped, each project with a summary page | Project chats become regular chats (project name stays as a property) |
| - [ ] | **Code folders** (`claude/code/`, `chatgpt/codex/`) | Claude Code and Codex sessions kept apart | They join regular chats |
| - [ ] | **Finds from X and the web** (`sources/finds/`) | Occasional threads, posts or pages that belong with your AI research | They'd go to your notes vault's clippings instead |
| - [ ] | **Searches** (`sources/searches/`) | AI search outputs you saved elsewhere (e.g. Grok on X), kept apart from chats | They'd go to your notes vault or your coding vault instead |
| - [ ] | **Raw transcripts** (`…/raw/`) | Word-for-word text copy of every imported chat | Notes keep summaries only; nothing to check against |
| - [ ] | **Text-only chat imports** | Images, downloads and export data stay in the original chat/archive; a specific attachment is copied only on request | Attachment handling needs a separate choice for each import |
| - [ ] | **How-tos** (`howto/`) | Practical know-how you keep, with a `tested` box | Keep how-tos as ideas or not at all |
| - [ ] | **Prompt library** (`prompts/`) | Reusable prompts you keep | Prompts stay inside chat notes only |

## Chat notes

| Remove? | Feature | What it does | If removed |
| --- | --- | --- | --- |
| - [ ] | **Link line at the top** (🔗 Open in… · Full transcript) | One click back to the chat and the transcript | Link stays at the bottom and in properties |
| - [ ] | **About** (Started as / Turned into) | What the chat was and became | Note starts with the main insight |
| - [ ] | **Main insight** | The one takeaway | — |
| - [ ] | **My highlights** | Your own section in every chat; AIs never write in it | Highlights stay as ==marks== in the text only |
| - [ ] | **Prompts and answers** | Each prompt word for word + the full de-bloated answer | Back to short takeaways, or summary only |
| - [ ] | **Compact mode** for very long chats | End result + key insights + turning points | Long chats get the full prompt list |
| - [ ] | **Unverified box** | Lists claims a chat made without a source | Claims sit in the text unmarked |
| - [ ] | **PROJECT / CODE badges** | Coloured label on the title of project and code chats | Only the folder and property show it |
| - [ ] | **Properties shown at the top** | All fields visible in each note | Hidden; see them in the Properties side panel |
| - [ ] | **Review / priority marks** (yours) | `to review` · `reviewed` · `skip`; `high` · `medium` · `low` | Fields and their views go |

## AI layer (`agent/`)

| Remove? | Feature | What it does | If removed |
| --- | --- | --- | --- |
| - [ ] | **AI topic maps** ([[agent/topics/Topics]]) | Topics with summaries and source links, kept up to date | Use your own `topics/` only |
| - [ ] | **Readwise sync** (`sources/readwise/`) | Your Reader highlights in the vault, with properties so Bases and search can use them | Keep them only in Readwise or only in your notes vault |
| - [ ] | **Code session format** ([[system/templates/Code session]]) | Lighter notes for Claude Code and Codex sessions: goal, outcome, decisions, fixes, prompts that worked; slim transcripts | Use the regular chat format |
| - [ ] | **Mac capture: Web Clipper → To sort** (`system/clipper/to-sort-clipper.json`) | One click adds the page or post (and any selected text) as a line in To sort | Paste into To sort by hand |
| - [ ] | **Keepers** ([[keepers/Keepers]]) | Your best-of shelf across all areas; only you change it; AIs only propose; deletions blocked by the commit script unless you confirm | Keep final findings inside chats and projects |
| - [ ] | **Known issues** ([[system/Known issues]]) | Problems found and not yet fixed, with how to fix each; any AI can pick one up | Keep them in the log only |
| - [ ] | **Status counts on Home** (`build_status.py`) | "About N captures waiting" in To sort and the number of drafts, refreshed on rebuild | Open To sort to check |
| - [ ] | **Finds** ([[sources/finds/Finds]]) | Posts and pages from your feed as small notes (post, My take, why it matters), listed on the projects they serve, with an Ideas section per project | Paste links into project notes yourself |
| - [ ] | **Notebook Navigator setup** | Reading/Full profiles, shortcuts, property browser, About previews, folder notes, Home as homepage | Navigator's defaults |
| - [ ] | **How I like to work** ([[system/How I like to work]]) | Your preferences, read by every AI at the start, so you don't repeat yourself | Tell each AI yourself |
| - [ ] | **[!ai] and [!mine] callouts** | See at a glance who wrote what: AI additions in your notes, your comments in AI notes | Plain text, no marking |
| - [ ] | **Version history (git)** (`system/scripts/vgit.sh`) | Every AI change is a named commit you can inspect and undo; history kept outside iCloud | Zip backups only |
| - [ ] | **Handoff and Decisions** ([[system/Handoff]], [[system/Decisions]]) | Let any new AI chat pick up the vault: state, open work, gotchas, and why things are built this way | Rely on AGENTS.md and the log only |
| - [ ] | **Weekly sort of To sort** ([[system/prompts/Sort my inbox]]) | On request, an AI proposes where each iPhone capture goes; you tick; it files them | Sort captures yourself |
| - [ ] | **Hover Editor** (plugin) | Hover a link to one of your notes (hold Cmd) for a popup you can pin, resize, stack and edit, like gwern.net | Built-in Page preview only |
| - [ ] | **Link Peek** (plugin, Mac only) | Hover a web link for a card with its title, description and image; hovering contacts that site | Plain links |
| - [ ] | **Trails to follow** ([[agent/trails/Trails to follow]]) | Links from your chats to read more on, by topic and kind, rebuilt by a script | Search chats for links instead |
| - [ ] | **Project notes** ([[projects/Projects]]) | A project note lists its chats automatically via the `projects` property | Use folders or tags |
| - [ ] | **Questions asked** ([[agent/questions/Questions asked]]) | Every prompt from your chats, by topic, linked to where you asked it; rebuilt by a script | Find old answers by searching chats instead |
| - [ ] | **Open questions** ([[agent/questions/Open questions]]) | Unresolved questions from chats, by topic | Questions stay inside chat notes |
| - [ ] | **Agent wiki** (`agent/wiki/`) | Patterns across several chats (e.g. *Comparing note-taking apps*) | No cross-chat pages |
| - [ ] | **Drafts for review** (how-to, prompt, idea, question candidates) | AI drafts; you keep, edit or skip | AI writes nothing for you to promote |
| - [ ] | **Index and log** ([[agent/index]], [[agent/log]]) | Catalog and history of everything the AI did | Harder to see what changed and why |
| - [ ] | **Import tick-box lists** | You choose which chats come in from an export | Exports import everything (not recommended) |
| - [ ] | **To-delete list** ([[agent/outputs/to-delete]]) | Suggested deletions waiting for your yes | Suggestions only in chat |

## Rules for AIs ([[AGENTS]])

| Remove? | Feature | What it does |
| --- | --- | --- |
| - [ ] | **Approval-only chats** | No chat enters the vault unless you asked or ticked it |
| - [ ] | **Permissions by area** | AI edits freely only in `agent/`; your folders and `system/` need your OK; transcripts never change |
| - [ ] | **"A chat said X" + no source laundering** | AI pages link every claim to its chat; labels for AI inference and verified |
| - [ ] | **Keep guides current** | Any change updates the related guides in the same task |
| - [ ] | **Multi-AI rules** | Read the log first, sign entries, one AI at a time |
| - [ ] | **Line labels** `[source]` `[inferred]` `[mine]` `[verified]` | Every AI line on wiki/topic pages says where it comes from |
| - [ ] | **Backup + sample before batches** | Zip in `agent/backups/`, dry run, then the health check |
| - [ ] | **`#sensitive` tag** | Private notes never sent to outside services |

## Scripts (`system/scripts/`)

| Remove? | Feature | What it does |
| --- | --- | --- |
| - [ ] | **check_vault.py** | Health check: broken links, missing chat fields, unlabelled AI lines, files that won't load |
| - [ ] | **build_index.py** | Rebuilds [[system/Index]]: every note with a one-line summary |
| - [ ] | **build_questions.py** | Rebuilds Questions asked |
| - [ ] | **backup.py** | Zips the vault into `agent/backups/` before batch changes |

## Views and pages

| Remove? | Feature | What it does |
| --- | --- | --- |
| - [ ] | **Home dashboard** | Chat homes, Marked to review, Waiting for you, Recent chats, How-tos to test, Recently kept, Pinned |
| - [ ] | **Extra chat views** in Saved chats | Per app, per kind, To review, High priority, with Chat link as 2nd column |
| - [ ] | **Template examples** ([[system/template examples/Template examples]]) | A filled-in example of every template |
| - [ ] | **[[system/Improve later]]** | Upgrades to add only when needed |
| - [ ] | **[[system/Scale back]]** | Overlaps and leftovers you could remove |
| - [ ] | **Weekly reset** with random revisit | 10-minute routine incl. opening a random old note |

## Plugins and settings

| Remove? | Feature | What it does | Turn off in |
| --- | --- | --- | --- |
| - [ ] | **Notebook Navigator** | Apple Notes–style browser | Settings → Community plugins |
| - [ ] | **Quiet Outline** | Searchable outline for long notes | Settings → Community plugins |
| - [ ] | **Omnisearch** | Typo-tolerant, ranked search | Settings → Community plugins |
| - [ ] | **Style Settings** | Tweak the theme by clicking | Settings → Community plugins |
| - [ ] | **Smart Connections** (already off) | Related notes in a sidebar | — |
| - [ ] | **Graph view, Random note, Note composer, Slash commands** | Built-in extras switched on | Settings → Core plugins |
| - [ ] | **Fold arrows always visible + calmer callouts** | Apple Notes–style collapsing | Settings → Appearance → CSS snippets (`distill`) |
| - [ ] | **Web Clipper template** (ChatGPT) | One-click save of a ChatGPT chat link | Just don't import it |

## Save routes

| Remove? | Feature | What it does |
| --- | --- | --- |
| - [ ] | **"Save this to my vault"** (Claude skill) | Saves any Claude chat in the full format |
| - [ ] | **[[system/prompts/Save this chat]]** | The same procedure for Codex and other AIs |
| - [ ] | **[[system/prompts/Archive this chat]]** | Paste-in prompt when no AI can reach the vault |

[[Home]] · [[system/How this vault works]] · [[system/Scale back]]
