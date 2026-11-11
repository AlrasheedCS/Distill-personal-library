#!/usr/bin/env python3
"""Rebuilds system/Index.md: every note with its one-line summary
(`about` for chats, `summary` or first line of text otherwise), grouped by folder.
Safe to re-run; it only rewrites system/Index.md."""
import os, re, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
def meta_and_body(t):
    m = {}
    body = t
    if t.startswith("---"):
        end = t.find("\n---", 3)
        if end > 0:
            for line in t[3:end].split("\n"):
                mm = re.match(r"^(about|summary|type):\s*'?(.*?)'?\s*$", line)
                if mm: m[mm.group(1)] = mm.group(2).replace("''", "'")
            body = t[end+4:]
    return m, body
def first_line(body):
    for l in body.split("\n"):
        l = l.strip()
        if l and not l.startswith(("#", ">", "!", "```", "|", "---", "[[")): return l[:120]
    return ""
groups = {}
for p in sorted(glob.glob("**/*.md", recursive=True)):
    if p.startswith((".obsidian", "system/archive/", "sources/readwise/")) or "/raw/" in p or p == "system/Index.md": continue
    t = open(p, encoding="utf-8").read()
    m, body = meta_and_body(t)
    summ = m.get("about") or m.get("summary") or first_line(body)
    folder = os.path.dirname(p) or "(root)"
    groups.setdefault(folder, []).append((p[:-3], summ, m.get("type", "")))
out = ["---", "type: index", "summary: 'Every note with a one-line summary. Rebuilt by system/scripts/build_index.py; do not edit by hand.'", "---", "", "# Index", "",
       "Every note in the vault with one line on what it is. Transcripts in `raw/` are left out. Rebuilt by `system/scripts/build_index.py`.", ""]
for folder in sorted(groups):
    out += [f"## {folder}", ""]
    for path, summ, typ in groups[folder]:
        out.append(f"- [[{path}|{os.path.basename(path)}]]" + (f" — {summ}" if summ else ""))
    out.append("")
open("system/Index.md", "w", encoding="utf-8").write("\n".join(out))
print(f"Index rebuilt: {sum(len(v) for v in groups.values())} notes.")

# Also refresh the small status counts shown on Home.
import subprocess, sys, os
subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_status.py")])
