# Save this chat

The procedure any AI follows when the owner says **"save this chat to my vault"** or **"save my chat about X"**. Claude has the same steps built in as a skill. ChatGPT, Codex or another AI with access to this folder should follow this note. Asking to save a chat is the owner's approval for that one chat only.

> [!info]- Copy-paste version for a chat that can't read this file
> ```text
> Save this conversation to my Obsidian vault (Distill). First read AGENTS.md and system/prompts/Save this chat.md in the vault and follow them exactly. Don't change anything in the chat app.
> ```

## Steps

1. **Rules.** Read [[AGENTS]] (labels, privacy, batch rules). Write only to `sources/chats/`, `sources/chats/raw/`, `agent/outputs/`, [[agent/index]], [[agent/log]]. Never delete, rename or edit anything else.
2. **Identity.** Get the title, URL and chat ID. ChatGPT: `https://chatgpt.com/c/<id>`. Claude: `https://claude.ai/chat/<id>`. If unknown, write `unknown`; never invent one.
3. **Duplicates.** Search all of `sources/chats/` for the same `chat_id`, then `url`. If found, update that note: add new prompts, append dated additions under `## More`. Never make a second note or delete text.
4. **Transcript.** `sources/chats/<app>/raw/<Title> — <first 8 chars of id>.md` (`<app>` = `chatgpt` for ChatGPT/Codex, `claude` for Claude/Claude Code), frontmatter `type: transcript`, `source` (`chatgpt`, `codex`, `claude` or `claude-code`), `chat_id`, `url`, `saved`. Every turn in order under `## User` / `## Assistant`, verbatim. If part of the chat isn't available to you, say so at the top; don't reconstruct it.
   **Attachments:** keep photos, screenshots, generated images, downloads, PDFs, spreadsheets, ZIPs and raw export JSON in the original chat/export archive outside the vault. Do not copy them by default. Use the original-chat link for details; retain a particular file only when the owner explicitly requests it.
5. **Chat note.** Regular chat: `sources/chats/<app>/<Title>.md` (`kind: chat`). Project chat: `sources/chats/<app>/projects/<Project>/<Title>.md` (`kind: project`, `cssclasses: [project-chat]`; create the project hub note if missing, see AGENTS.md). Claude Code / Codex: `sources/chats/claude/code/` or `sources/chats/chatgpt/codex/` (`kind: code`, `cssclasses: [code-session]`). Use [[system/templates/Chat capture]]. Set `source`, `chat_id`, `url`, `transcript` (link to the raw file), `about`, `main_insight`, `saved`, `status: distilled`. Body in this order. First, right under the title: `> [!link] [Open in <App>](<url>) · [[<transcript>|Full transcript]]`. Then:
   - `## About`: **Started as** / **Turned into** (or "same").
   - `## Main insight`: 1–2 sentences.
   - `## My highlights`: leave empty with its hidden hint; it's the owner's. Never write in it, and keep it untouched on updates.
   - `## Prompts and answers`: one `### N. <short label>` per owner prompt, the prompt verbatim as a `>` quote (over ~120 words: first lines + "… (full prompt in transcript)"), then the condensed answer: a de-bloated version of the reply that keeps **all** substance (every option, approach, tool, list item, step, recommendation, number, decision and caveat; tables when things are compared) and drops filler (greetings, "I'll check…", tool narration, repetition, hedging, source lists). Follow-ups that only tweaked a file get one line on what changed. Skip "thanks/ok/continue" turns and note how many.
   - `## More`: `### Other insights`; a `> [!warning]- Unverified` callout for factual claims without a cited source; `### Next actions` (explicit only); `### Original chat` link.
   Very long chats (50+ prompts or 150,000+ characters): use **compact mode** from AGENTS.md (`depth: compact`): End result, Key insights from the whole chat, Turning points.
   Write "the chat suggested X", not "X is true".
6. **Link.** Set `topics` to `agent/topics/` maps and add the chat to them; add open questions to [[agent/questions/Open questions]]; update `agent/wiki/` if a pattern repeats (see AGENTS.md step 5).
7. **Candidates.** How-tos → `agent/outputs/howto-candidates/` (template `How-to.md`, `tested: false`). Reusable prompts the owner wrote → `agent/outputs/prompt-candidates/` (template `Prompt.md`). Ideas → `agent/outputs/idea-candidates/`, questions → `agent/outputs/question-candidates/`. Never write into `howto/`, `prompts/`, `ideas/` or `questions/`.
   **Claude Code or Codex session?** Use [[system/templates/Code session]] instead (goal, outcome, decisions, fixes, prompts that worked, where) and a slim transcript (your messages and the AI's final replies only). Rules: AGENTS.md, "Code sessions".
   **Commit.** Before writing, and again at the end, run `bash system/scripts/vgit.sh snapshot <tool> "save chat <Title>"` (see AGENTS.md, Version history).
   **Keeper?** If the chat reached a clear final answer (a best pick, a tip that worked, a prompt worth trusting, a decision), draft it in `agent/outputs/keeper-candidates/` (template Keeper, chat linked) and say so in the report. Never write into `keepers/` unless the owner says keep.
8. **Rebuild.** Run `python3 system/scripts/build_index.py`, `python3 system/scripts/build_questions.py` and `python3 system/scripts/build_trails.py`.
   **Project?** If the chat clearly belongs to an active project in `projects/`, say so in the report; set its `projects` property only with the owner's OK.
9. **Log.** Append `## [YYYY-MM-DD] save | <Title> (<your tool name>)` to [[agent/log]]; add the chat to [[agent/index]] under "Sources ingested".
10. **Report** in one or two lines: what was saved, where, how many candidates wait for review.

[[AGENTS]] · [[Home]]
