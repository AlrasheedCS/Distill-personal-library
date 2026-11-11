#!/usr/bin/env python3
"""Zips the whole vault (except backups, plugin code and indexes) into agent/backups/.
Run before any batch change:  python3 system/scripts/backup.py <short-label>"""
import os, sys, zipfile, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
label = (sys.argv[1] if len(sys.argv) > 1 else "backup").replace("/", "-")
os.makedirs("agent/backups", exist_ok=True)
out = f"agent/backups/{datetime.datetime.now():%Y-%m-%d-%H%M}-{label}.zip"
skip = ("agent/backups", ".obsidian/plugins", ".smart-env", ".trash")
n = 0
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for d, _, files in os.walk("."):
        dd = d[2:] if d.startswith("./") else d
        if dd.startswith(skip): continue
        for f in files:
            p = os.path.join(dd, f) if dd not in (".", "") else f
            z.write(p); n += 1
print(f"Backed up {n} files to {out} ({os.path.getsize(out)//1024} KB)")
