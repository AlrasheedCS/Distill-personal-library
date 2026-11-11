#!/usr/bin/env python3
"""Distill health check. Read-only: reports problems, changes nothing.
Run from anywhere:  python3 "system/scripts/check_vault.py"
Checks: broken wikilinks, frontmatter that won't parse, chat notes missing
required properties or their transcript, Base/JSON files that won't parse,
and AI pages (agent/wiki, agent/topics) whose bullet lines lack a label."""
import os, re, sys, json, glob
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
try:
    import yaml
except ImportError:
    yaml = None
problems = []
def rel(p): return os.path.relpath(p, ROOT)
md = [p for p in glob.glob("**/*.md", recursive=True) if not p.startswith((".obsidian", "system/archive/", "agent/backups/", "sources/readwise/"))]
names = {os.path.basename(p)[:-3] for p in md}
paths = {p[:-3] for p in md} | {p for p in glob.glob("**/*", recursive=True)}
def fm(text):
    if not text.startswith("---"): return {}
    end = text.find("\n---", 3)
    if end < 0: return None
    if not yaml: return {}
    try: return yaml.safe_load(text[3:end]) or {}
    except Exception: return None
REQUIRED = ["type","kind","source","chat_id","about","main_insight","url","transcript","saved","status"]
LABEL = re.compile(r"^\s*[-*] (\[(source|inferred|mine|verified)\]|\[\[|\*\*|`)")
for p in md:
    if p == "agent/log.md": continue
    t = open(p, encoding="utf-8").read()
    meta = fm(t)
    if meta is None: problems.append(f"frontmatter won't parse: {p}"); meta = {}
    if "/raw/" not in p:
        for m in re.finditer(r"\[\[([^\]|#]+)", t):
            target = m.group(1).strip().rstrip("\\")
            if "<" in target or target.startswith("PASTE"): continue
            if target not in paths and target not in names and target + ".md" not in paths:
                problems.append(f"broken link in {p}: [[{target}]]")
    if meta.get("type") == "chat" and not meta.get("example"):
        miss = [k for k in REQUIRED if k not in meta]
        if miss: problems.append(f"chat missing {', '.join(miss)}: {p}")
        tr = str(meta.get("transcript", ""))
        m = re.search(r"\[\[(.+?)\]\]", tr)
        if m and m.group(1) + ".md" not in paths: problems.append(f"transcript not found for {p}")
    if p.startswith(("agent/wiki/", "agent/topics/")) and "About this folder" not in p and not p.endswith("Topics.md"):
        sec = ""
        for i, line in enumerate(t.split("\n"), 1):
            if line.startswith("## "): sec = line
            if sec.startswith(("## Chats", "## Where each point comes from", "## Unverified")): continue
            if re.match(r"^\s*- (?!\[[ x]\])", line) and not LABEL.match(line):
                problems.append(f"unlabelled line {p}:{i}: {line.strip()[:60]}")
for b in glob.glob("system/bases/*.base"):
    if yaml:
        try: yaml.safe_load(open(b, encoding="utf-8"))
        except Exception as e: problems.append(f"base won't parse: {b} ({e.__class__.__name__})")
for j in glob.glob(".obsidian/*.json") + glob.glob("system/clipper/*.json"):
    try: json.load(open(j, encoding="utf-8"))
    except Exception: problems.append(f"json won't parse: {j}")
print(f"Checked {len(md)} notes.")
print("No problems found." if not problems else f"{len(problems)} problem(s):")
for x in problems: print(" -", x)
sys.exit(1 if problems else 0)
