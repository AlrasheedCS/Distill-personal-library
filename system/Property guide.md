# Property guide

Keep the keys stable so templates and Bases agree.

| Property | Type | Meaning |
| --- | --- | --- |
| `type` | Text | `chat`, `article`, `idea`, `question`, `topic`, `project`, `prompt`, `howto`, `wiki`, `search`, `search-raw` |
| `source` | Text | Chats: `chatgpt`, `codex`, `claude` or `claude-code`. Other sources: publication or website |
| `url` | Text | Original conversation or source URL |
| `saved` | Date | Date captured into this vault, YYYY-MM-DD |
| `chatgpt_project` | Text | Exact project name in ChatGPT or Claude; blank when none (key kept for compatibility) |
| `pinned` | Checkbox | Snapshot of the chat's pinned/starred status |
| `status` | Text | Chats: `inbox`, `saved`, `distilled`, `archived` |
| `topics` | List | Prefer links to topic notes; keep spelling consistent |
| `projects` | List | Links to local project notes |
| `why_saved` | Text | What makes the note worth keeping |
| `example` | Checkbox | True only for demonstrations; excluded from live Bases |
| `tags` | Tags | Optional cross-cutting labels. `#sensitive` = private (health, money, family): AIs never send it to outside services unless you include it |
| `search_by` | Text | Searches: which tool ran it and on what (e.g. Grok on your X following list) |
| `origin` | Text | Searches: where the original was saved (e.g. Apple Notes, note title) |
| `destination` | Text | Where a note should eventually live (e.g. `coding vault`) |
| `kind` | Text | Chats: `chat` (regular), `project` (in a ChatGPT or Claude project) or `code` (Claude Code or Codex session). Project and code notes also get `cssclasses: [project-chat]` or `[code-session]` for a badge |
| `depth` | Text | Chats: `full` (every prompt listed) or `compact` (very long chats: end result + insights from the whole chat) |
| `review` | Text | **Yours.** `to review` · `reviewed` · `skip` (don't need to review). Blank = not decided |
| `priority` | Text | **Yours.** `high` · `medium` · `low`. Blank = none |
| `about` | Text | Chats: one line on what the chat was (or turned out to be) about |
| `main_insight` | Text | Chats: the single most useful takeaway |
| `chat_id` | Text | Conversation ID from ChatGPT or Claude; the stable identity for imported chats |
| `transcript` | Text | Chats: link to the full transcript in `sources/chats/<app>/raw/` |
| `purpose` | Text | Prompts: what the prompt is for |
| `variables` | List | Prompts: placeholders to fill in |
| `source_chats` | List | Prompts: links to the chats a prompt came from |
| `sources` | List | How-tos and agent wiki pages: links to the notes they draw on |
| `tested` | Checkbox | How-tos: `true` only once you've actually done it and it worked |

For ideas use `draft` or `evergreen`; for questions `open` or `answered`; for projects `active`, `paused`, or `done`; for prompts and how-tos `draft` or `keeper`. Do not use these values for chat statuses unless you also change the Base filters.

In source mode, write lists as `[]` or YAML list items. Quote wikilinks in YAML, for example `topics: ["[[agent/topics/<Topic>]]"]`. Keep booleans unquoted: `pinned: true`. Dates are capture dates, not the conversation creation date.

**Finds** (`type: find`, in `sources/finds/`): `source` (x, github, web), `author`, `url`, `about`, `published`, `saved`, `captured_via`, `projects`, `topics`, plus your `review` and `priority`.

**Keepers** (`type: keeper`, in `keepers/`): `area`, `kind` (pick, tip, prompt, how-to, verdict, list), `verdict` (the finding in one line), `confirmed`, `recheck` (date to check it's still true), `sources`, `status` (current or outdated).

[[Home]]
