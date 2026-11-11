#!/usr/bin/env python3
"""Rebuild agent/status.md: small live-ish counts shown on Home (captures waiting in To sort, drafts waiting).
Read-only on everything except agent/status.md. Run from the vault root (build_index.py runs it too)."""
import re, glob, datetime
t = open("inbox/to sort.md", encoding="utf-8").read()
new = t.split("## New captures", 1)[1] if "## New captures" in t else ""
# only what came after the last "[!ai] Filed" box
parts = re.split(r"^> \[!ai\] Filed[^\n]*\n(?:>[^\n]*\n?)*", new, flags=re.M)
tail = parts[-1]
lines = [l for l in tail.split("\n") if l.strip()]
boxes = sum(1 for l in lines if re.match(r"\s*- \[ \]", l))
urls = sum(len(re.findall(r"https?://", l)) for l in lines if not re.match(r"\s*- \[[ x]\]", l))
paras = len([p for p in re.split(r"\n\s*\n", tail) if p.strip()])
waiting = boxes + urls if (boxes + urls) else paras
drafts = len([f for f in glob.glob("agent/outputs/*-candidates/*.md")])
now = datetime.date.today().isoformat()
out = f"""---
type: status
maintained_by: script
---

# Status

Rebuilt by `system/scripts/status` whenever an AI runs the rebuild scripts (not live). Last rebuilt {now}.

## To sort

📥 **[[inbox/to sort|To sort]]**: {"nothing waiting" if not lines else f"about {waiting} capture{'s' if waiting != 1 else ''} waiting"} · say "sort my inbox" to file them

## Drafts

🗂 {drafts} AI drafts waiting for you (how-tos, prompts, ideas, questions): see *Waiting for you* below
"""
out = out.replace("`system/scripts/status`", "`system/scripts/build_status.py`")
open("agent/status.md", "w", encoding="utf-8").write(out)
print(f"Status rebuilt: {waiting if lines else 0} captures waiting, {drafts} drafts.")
