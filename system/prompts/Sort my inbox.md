---
type: guide
summary: "The weekly sort of inbox/to sort.md: propose a place for each capture, the owner ticks, then file and mark done."
---

# Sort my inbox

Run this only when the owner asks ("sort my inbox"). Never sort on your own. Rules: [[AGENTS]] (section "To sort").

1. **Read** the unticked lines (`- [ ]`) under `## New captures` in [[inbox/to sort]]. Leave everything above that heading alone: it's the owner's own material.
2. **Work out each line's kind,** from the type word if there is one (chat, search, find, prompt, question, vault idea), otherwise from the link: `chatgpt.com/share` or `claude.ai` = chat, `x.com` or a web page = find, plain text = the owner's thought, prompt or question. Open what you can reach to judge it; private `chatgpt.com/c/` links can't be read, so ask for a share link.
3. **Propose a tick list** in the chat (and in `agent/outputs/sort-YYYY-MM-DD.md`), one row per capture: the item, where it would go, and why.
   | Kind | Suggested place |
   |---|---|
   | Chat | Save it with [[system/prompts/Save this chat]] (capturing it counts as approval to save that chat) |
   | Search result | A note in `sources/searches/` |
   | Find from X or the web | A note in `sources/finds/` (template [[system/templates/Find]]): the captured text word for word, the owner's own words into **My take**, `projects` set if the capture names one (`→ Project name`) or it clearly fits, and the idea added to that project's `[!ai]` Ideas box |
   | Prompt | A draft in `agent/outputs/prompt-candidates/` |
   | Question | [[agent/questions/Open questions]] under its topic, or a question candidate |
   | Vault idea | A next action in [[projects/Improve this vault]] (with the owner's OK; it's their note) |
   | The owner's own thought | **"yours"**: stays put. Never route anything to your notes vault |
   | A clear final answer (best pick, proven tip, trusted prompt, decision) | Also suggest **"keeper?"**: a draft in `agent/outputs/keeper-candidates/`; it goes to `keepers/` only if the owner says keep |
   When nothing fits, suggest **"new note: <name>"** or **"new project: <name>"**. Mark unclear items **"?"** and ask.
4. **Wait for ticks.** Apply only ticked rows. For each: create or append at the destination, then tick its line in To sort and add ` → [[<destination>]]`.
5. **Archive (only with a yes):** move ticked lines into `inbox/archive/YYYY-Www.md`, keeping the order. Never delete a capture.
   **Reading captures:** one capture may hold several posts; split them. Text before or after a link belongs to that link by position; when it's unclear whose post a text is, say so in the find. Lines starting `me:` are the owner's own thoughts. Captures that aren't `- [ ]` lines stay as they are: record where each went in an `> [!ai] Filed` box under them.
6. **Rebuild and log:** run the rebuild scripts if notes were added, then append `## [YYYY-MM-DD] sort | N captures (<tool>)` to [[agent/log]].
