# Setup and appearance

## Included

**Things 2.2.4**, by Colin Eckert, is bundled under `.obsidian/themes/Things/`, including its MIT license. The vault selects Things, light mode, a blue accent, readable line length, and an 18 px base text size. No external font installation is required. A small `distill` CSS snippet adds spacing, a wider Home and always-visible fold arrows beside headings. Properties show at the top of each note (fold them with the arrow beside "Properties").

If Things is not active, go to **Settings → Appearance → Themes** and select Things. If necessary, use **Manage**, search Things, and install/update it from the community theme browser. Turn the snippet on/off under **Appearance → CSS snippets**. Change Base color scheme to dark if preferred; Things supports both.

## Core tools, already enabled

| Tool | Purpose |
| --- | --- |
| Bases | Saved-chat views and source library |
| Templates | Reusable note structures, folder `system/templates` |
| Search + Quick Switcher | Full-text search and quick navigation |
| Backlinks + Outgoing links | Follow connected ideas and sources |
| Properties view | Edit metadata consistently |
| Bookmarks | Home, chats, sources, and setup |
| Outline | Navigate longer summaries |
| File recovery | Recover recent local note changes; this is not a backup |

Also enabled: Graph view, Command palette, Slash commands, Random note, Note composer.

## Community plugins

Turn them on once: **Settings → Community plugins → Turn on community plugins.**

| Plugin | Purpose |
| --- | --- |
| Omnisearch | Typo-tolerant search, best match first. Needs Obsidian 1.13.3+ |
| Smart Connections | **Off for now** (slow to load). Installed; turn on in Settings → Community plugins when wanted. Related notes in a sidebar, local index in `.smart-env/` |
| Style Settings | Adjust the Things theme by clicking: Settings → Style Settings |
| Notebook Navigator | Apple Notes–style browser: folders on the left, note previews on the right, pinned and recent notes, iPhone-friendly, right-to-left support. Replaces the file list (ribbon icon or *Notebook Navigator: Open*) |
| Quiet Outline | Better outline for long notes: search headings, remembers what you folded, hover previews |

Add new plugins sparingly: each one can read the whole vault. Ideas for later: [[system/Improve later]].

## Manual step

The [official browser Web Clipper](https://obsidian.md/clipper) is a separate extension. Install it and import the provided JSON as described in [[Capture chats]]. Its browser permissions and vault selection cannot be preconfigured inside a ZIP. The template is stored in `system/clipper/`, not in the core Templates folder.

## Search shortcuts

Open the command palette for **Quick switcher: Open quick switcher**, **Search: Search in all files**, and **Templates: Insert template**. Default platform shortcuts remain available. Try Omnisearch, or search `path:"sources/chats"`, a distinctive phrase, or a conversation URL. The Bases handle property filtering.

## Keep a backup

Back up the whole folder, including hidden `.obsidian` settings and attachments. The vault syncs through iCloud. Avoid editing the same note on two devices at once, which can create conflict copies. Deleted files sit in iCloud's Recently Deleted for 30 days.

[[Home]]

## Who wrote it: [!ai] and [!mine] callouts

`distill.css` styles two callouts: `> [!ai]` (grey, dashed edge, bot icon) for text an AI adds inside your notes, and `> [!mine]` (amber, person icon) for your own comments inside AI-written notes, e.g. under an answer in a chat note. AIs never edit `[!mine]`.

## Notebook Navigator

- **Two vault profiles** (switch with the command "Notebook Navigator: Select vault profile"): **Reading** (default) hides raw transcripts, backups and system internals from the sidebar; **Full** shows everything. Hiding is sidebar-only: search, links and AIs still see every file.
- **Shortcuts** at the top: Home, To sort, ChatGPT home, Claude home, Questions asked, Trails to follow, projects, searches.
- **Property browser:** click `review`, `priority`, `kind` or `source` in the sidebar to list notes by value (e.g. priority → high).
- **Previews** in the file list show each note's `about` (or `main_insight`, `summary`) instead of its first line.
- **Folder notes:** clicking a project folder opens its hub note. Home and the two app homes are pinned; Home is the homepage; calendar off.
- Quiet Outline opens two heading levels deep, so a chat's numbered prompts show as a list.
