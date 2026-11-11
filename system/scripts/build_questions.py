#!/usr/bin/env python3
"""Builds the "Questions asked" notes: every question you asked in your chats
(each prompt heading plus the start of the prompt), grouped by topic, each
linked to the exact spot in its chat note. Rebuilds agent/questions/asked/;
safe to re-run. Run after saving or importing chats."""
import os, re, glob, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
OUT = "agent/questions/asked"
os.makedirs(OUT, exist_ok=True)
by_topic = collections.defaultdict(list)
total = 0
for p in sorted(glob.glob("sources/chats/**/*.md", recursive=True)):
    if "/raw/" in p: continue
    t = open(p, encoding="utf-8").read()
    fm = t.split("\n---", 1)[0] if t.startswith("---") else ""
    if not re.search(r"^type: chat$", fm, re.M) or re.search(r"^example: true", fm, re.M): continue
    topics = re.findall(r"agent/topics/([^\]|]+)", fm) or ["Other"]
    title_m = re.search(r"^# (.+)$", t, re.M)
    title = title_m.group(1).strip() if title_m else os.path.basename(p)[:-3]
    src = (re.search(r"^source: (\S+)", fm, re.M) or [None, ""])[1]
    qs = []
    for m in re.finditer(r"^### (\d+\.\s.+?)\s*\n+> ?(.*)", t, re.M):
        head, first = m.group(1).strip(), m.group(2).strip()
        first = re.sub(r"\s+", " ", first)
        if len(first) > 140: first = first[:137].rstrip() + "…"
        qs.append((head, first))
    if not qs: continue
    total += len(qs)
    by_topic[topics[0]].append((p[:-3], title, src, qs))
APP = {"chatgpt": "ChatGPT", "codex": "Codex", "claude": "Claude", "claude-code": "Claude Code"}
def esc(s): return s.replace("|", "/").replace("[", "(").replace("]", ")")
index = []
for topic in sorted(by_topic, key=lambda k: (-sum(len(c[3]) for c in by_topic[k]), k)):
    chats = by_topic[topic]
    n = sum(len(c[3]) for c in chats)
    L = ["---", "type: questions-asked", "maintained_by: script", f"topic: '{topic}'", "---", "",
         f"# Questions asked: {topic}", "",
         f"{n} questions from {len(chats)} chats. Each links to the exact prompt in its chat note. Rebuilt by `system/scripts/build_questions.py`; edits here are overwritten.", ""]
    for path, title, src, qs in sorted(chats, key=lambda c: c[1].lower()):
        L.append(f"## [[{path}|{esc(title)}]]" + (f" · {APP.get(src, src)}" if src else ""))
        L.append("")
        for head, first in qs:
            label = re.sub(r"^\d+\.\s*", "", head)
            L.append(f"- [[{path}#{head}|{esc(label)}]]" + (f": “{esc(first)}”" if first else ""))
        L.append("")
    L.append("[[agent/questions/Questions asked|All topics]] · [[Home]]")
    open(f"{OUT}/{topic}.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
    index.append((topic, n, len(chats)))
I = ["---", "type: questions-asked", "maintained_by: script", "summary: 'Every question you asked in your chats, by topic, linked to where you asked it.'", "---", "",
     "# Questions asked", "",
     f"Every question you've asked in your chats: **{total} prompts** across {sum(i[2] for i in index)} chats, grouped by topic. Each one links to the exact place in its chat. Use it to find an earlier answer before asking again, or to spot what you keep asking about.", "",
     "> [!tip] Search inside one topic with Cmd+F, or across all with Omnisearch: `path:agent/questions/asked`.", "",
     "| Topic | Questions | Chats |", "| --- | --- | --- |"]
I += [f"| [[{OUT}/{t}\\|{t}]] | {n} | {c} |" for t, n, c in index]
I += ["", "Unresolved questions are a separate list: [[agent/questions/Open questions]].", "", "Rebuilt by `system/scripts/build_questions.py`; edits here are overwritten.", "", "[[Home]]"]
open("agent/questions/Questions asked.md", "w", encoding="utf-8").write("\n".join(I) + "\n")
print(f"Questions asked rebuilt: {total} questions, {len(index)} topics.")
