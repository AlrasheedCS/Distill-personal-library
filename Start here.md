# Start here

Five steps, once. Then read [[system/How this vault works]] for the full picture.

Want to see it filled in first? Open the demo vault: `demo/Distill-demo.zip` (see [[demo/README|the demo guide]]).

## 1. Open the vault

In Obsidian: **Open folder as vault** → the folder you downloaded. To use it on your iPhone too, put the folder in `iCloud Drive › Obsidian` (then in Finder, right-click it → **Keep Downloaded** so files never go cloud-only).

## 2. Turn on the plugins

**Settings → Community plugins → Turn on community plugins**, then **Browse** and install: Notebook Navigator, Omnisearch, Quiet Outline, Hover Editor, Link Peek, Style Settings and QuickAdd (Readwise Official only if you use Readwise). Their settings are already in the vault. The Things theme and the `distill` snippet are already on. What each does: [[system/Features]].

## 3. Set up capture on your iPhone

In Obsidian on iPhone, point the **share sheet** and **Quick Capture** at the bookmarked note [[inbox/to sort|To sort]] (two share locations: link and text). Templates are in `system/templates/capture/`. Say **"sort my inbox"** to an AI now and then to file what you captured.
**On the Mac:** install the [Obsidian Web Clipper](https://obsidian.md/clipper) in your browser and import `system/clipper/to-sort-clipper.json` (Clipper settings → Import). One click on any page, post or ChatGPT share link adds a line to To sort; select text first to include it. For a quick thought, assign a hotkey to Notebook Navigator's "Open shortcut 2" (To sort) in Settings → Hotkeys and type at the bottom.

## 4. Connect your AIs

- **Claude** (desktop app, or the phone app in a chat linked to this Mac): connect this vault folder (and the folder holding its version history, if you use `vgit.sh`), then say **"save this chat"**. Starter prompts: [[system/Handoff]].
- **Codex:** open this folder as its workspace. It reads [[AGENTS]] automatically.
- **ChatGPT** can't reach the vault: share a chat's link to To sort, or paste it into a linked Claude chat.

## 5. Bring in your chats

Request the exports (ChatGPT: Settings → Data controls → Export data · Claude: Settings → Privacy → Export data), then ask an AI to import them. You'll get a tick-box list first, and only ticked chats are added. Checklist: [[system/Migration checklist]]. Photos, screenshots, downloads and raw export files stay outside the vault by default; the notes link back to the original chats. Ask explicitly to retain a particular attachment.

> [!note]- About the example notes
> The notes in `system/template examples/` (and the starter prompts in `prompts/`) are fictional examples. The examples are hidden from your views; delete any of them whenever you like.

[[Home|Back to Home]]
