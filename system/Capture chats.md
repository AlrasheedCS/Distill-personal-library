# Capture chats

Ways to bring a chat in. **Only chats you approve are added.** Quickest, by situation:

| Situation | Do this |
|---|---|
| Claude chat, linked to this Mac | Say **"save this chat"** in it |
| An older Claude chat | In a linked chat: **"save my chat about X"** |
| ChatGPT chat | **Share → Copy link**, then share it to **To sort** on your iPhone, or paste it into a linked Claude chat or Codex |
| Claude Code or Codex session | Say **"save this session"** |
| On the Mac, any page, post or share link | **Web Clipper → "To sort — capture"** (one click; select text first to keep it) |
| Many chats at once | Export, then let an AI make a tick list (below) |

## 1. "Save this to my vault" (Claude)

In a Claude chat in the desktop app, linked to this Mac, say **save this to my vault** or **save my chat about X**. The *save-chat-to-vault* skill writes the transcript and the note to `sources/chats/claude/`, and drafts how-tos and prompts for review.

## 2. Codex (ChatGPT side)

Open this folder in Codex and ask it to save a chat following [[system/prompts/Save this chat]]. Codex can't see your ordinary ChatGPT chats: give it a ChatGPT **share link** or an export.

## 3. Exports (best for the backlog)

1. Request the export. ChatGPT: Settings → Data controls → Export data. Claude: Settings → Privacy → Export data.
2. Unzip it outside the vault, somewhere the AI can reach, and ask it to import.
3. It writes a tick-box list to `agent/outputs/import-candidates-<date>.md`. Tick what you want.
4. Only ticked chats are imported, in batches. Re-running never creates duplicates.
5. Import notes and text transcripts only. Photos, screenshots, PDFs, spreadsheets, ZIPs and raw export JSON stay in the original chat/export archive outside the vault. Copy a particular file only when you explicitly request it; use the original-chat link for details.

Steps: [[system/Migration checklist]].

## 4. Web Clipper (a quick link, older method)

> [!note] Usually not needed now: sharing a chat's link to [[inbox/to sort|To sort]] does the same from the iPhone.

Set up once: install the [Obsidian Web Clipper](https://obsidian.md/clipper), then in its settings → **Import** `system/clipper/chatgpt-pointer-clipper.json`. It saves ChatGPT chat links to `sources/chats/chatgpt/`. (For Claude, "save this to my vault" does better.)

Each time: open the chat → click the Clipper → check the title and link → save. This saves a link only. The full text and summary come with the next export or save, into the same note.

> [!warning]- Clipper limits
> It doesn't check for duplicates: search the chat's link in Omnisearch first. Avoid clipping a home page, project page or temporary chat. Pinned and project fields are a snapshot you set by hand.

## Without any tool

> [!note]- Paste-in method
> Paste the prompt from [[system/prompts/Archive this chat]] into the chat itself. Create a note in `sources/chats/chatgpt/` or `sources/chats/claude/`, insert the [[system/templates/Chat capture|Chat capture]] template, paste the result, and add the chat's link. This adds a message to the chat.

[[ChatGPT home]] · [[Claude home]] · [[Home]]
