#!/usr/bin/env python3
"""Rebuild agent/trails/: links from chat and search notes, by topic and kind, each linked to where it appeared.
Read-only on chat notes. Run from the vault root. Never edit the output by hand."""
import glob, os, re, collections, yaml
OUT = "agent/trails"
SKIP = re.compile(r"^(help|support|docs\.github|accounts|login|auth)\.|chatgpt\.com|claude\.ai|openai\.com/(index|policies)|"
                  r"amazon\.|noon\.com|uniqlo|zara\.com|hm\.com|ikea|linkedin\.com|spotify\.com|circleboom|apps\.apple\.com|"
                  r"play\.google|google\.com/(maps|search)|bing\.com|duckduckgo|example\.com|localhost|readwise-assets|pbs\.twimg|"
                  r"images-|w3\.org|schema\.org|xmlns|fonts\.(googleapis|gstatic)|cdn\.|cloudfront|googleusercontent|gravatar|"
                  r"\.(png|jpe?g|gif|webp|svg|zip|pdf)$")
KINDS = [("Discussions", r"^(reddit\.com|old\.reddit|x\.com|twitter\.com|news\.ycombinator|lobste\.rs|forum\.|community\.)"),
         ("Code and tools", r"^(github\.com|gitlab\.com|huggingface\.co|pypi\.org|npmjs\.com|obsidian\.md/plugins|community\.obsidian)"),
         ("Papers", r"^(arxiv\.org|doi\.org|ssrn|nber\.org|pubmed|ncbi\.nlm|scholar\.google|semanticscholar|jstor|nature\.com|science\.org|biorxiv|medrxiv)"),
         ("Video and audio", r"^(youtube\.com|youtu\.be|vimeo\.com|podcasts\.apple)")]
def kind(dom):
    for k, rx in KINDS:
        if re.match(rx, dom): return k
    return "Reading"
def clean(u): return u.rstrip(".,;:*_`'\"")
# what's already in Readwise
inrw = set()
for f in glob.glob("sources/readwise/**/*.md", recursive=True):
    m = re.search(r"^url: (\S+)", open(f, encoding="utf-8").read()[:800], re.M)
    if m: inrw.add(m.group(1).rstrip("/"))
links = collections.defaultdict(dict)   # topic -> url -> {text, kind, src:set}
for p in sorted(glob.glob("sources/**/*.md", recursive=True)):
    if "/raw/" in p or p.startswith("sources/readwise"): continue
    t = open(p, encoding="utf-8").read()
    if not t.startswith("---"): continue
    fm, body = t.split("---", 2)[1:]
    try: d = yaml.safe_load(fm) or {}
    except Exception: continue
    if d.get("type") not in ("chat", "search", "find") or d.get("example"): continue
    topics = re.findall(r"agent/topics/([^\]|]+)", fm) or ["Other"]
    title = (re.search(r"^# (.+)$", body, re.M) or [None, os.path.basename(p)[:-3]])[1].strip()
    src = f"[[{p[:-3]}|{title}]]"
    seen_here = set()
    for m in re.finditer(r"\[([^\]\n]{2,120})\]\((https?://[^)\s]+)\)|(?<![(\[])(https?://[^\s)\]>\"'|]+)", body):
        text, u = (m.group(1), m.group(2)) if m.group(2) else (None, m.group(3))
        u = clean(u); dom = re.sub(r"^https?://(www\.)?", "", u).split("/")[0].lower()
        path = re.sub(r"^https?://(www\.)?", "", u).lower()
        if SKIP.search(dom) or SKIP.search(path) or u == d.get("url") or u in seen_here: continue
        seen_here.add(u)
        e = links[topics[0]].setdefault(u, {"text": None, "kind": kind(dom), "src": [], "dom": dom})
        if text and not e["text"] and not text.startswith("http"): e["text"] = text.strip()
        if src not in e["src"]: e["src"].append(src)
os.makedirs(f"{OUT}/by topic", exist_ok=True)
rows = []
for topic in sorted(links):
    L = links[topic]; n_rw = sum(1 for u in L if u.rstrip("/") in inrw)
    out = [f"---\ntype: trails\nmaintained_by: script\ntopic: '{topic}'\n---\n",
           f"# Trails: {topic}\n",
           f"{len(L)} links from your chats, by kind; most-cited first. ✓ = already in Readwise. Rebuilt by `system/scripts/build_trails.py`; edits here are overwritten. Back to [[agent/trails/Trails to follow|Trails to follow]].\n"]
    for k in ["Reading", "Papers", "Code and tools", "Discussions", "Video and audio"]:
        items = sorted(((u, e) for u, e in L.items() if e["kind"] == k), key=lambda x: (-len(x[1]["src"]), x[1]["dom"]))
        if not items: continue
        out.append(f"\n## {k} ({len(items)})\n")
        for u, e in items:
            label = (e["text"] or re.sub(r"^https?://(www\.)?", "", u)[:90]).replace("[", "(").replace("]", ")").replace("|", "/")
            mark = " ✓" if u.rstrip("/") in inrw else ""
            out.append(f"- [{label}]({u}){mark} · {e['dom']} · from {', '.join(e['src'][:3])}{' +' + str(len(e['src'])-3) if len(e['src'])>3 else ''}")
    open(f"{OUT}/by topic/{topic}.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
    c = collections.Counter(e["kind"] for e in L.values())
    rows.append(f"| [[{OUT}/by topic/{topic}\\|{topic}]] | {len(L)} | {c['Reading']} | {c['Papers']} | {c['Code and tools']} | {c['Discussions']} | {c['Video and audio']} | {n_rw} |")
total = sum(len(v) for v in links.values())
idx = f"""---
type: trails
maintained_by: script
---

# Trails to follow

Sources your chats, searches and finds pointed to, to follow up and read more on: {total} links, by topic. Each links back to the chat it came from. Help pages, shopping, social profiles and images are left out. ✓ marks ones already saved in Readwise.

> [!tip] To read one later, open it and save it to Readwise Reader; it will sync into `sources/readwise/`. Search inside trails with Omnisearch: `path:agent/trails`.

| Topic | Links | Reading | Papers | Code | Discussions | Video | In Readwise |
|---|---|---|---|---|---|---|---|
""" + "\n".join(rows) + "\n\nRebuilt by `system/scripts/build_trails.py`; edits here are overwritten. Back to [[Home]].\n"
open(f"{OUT}/Trails to follow.md", "w", encoding="utf-8").write(idx)
print(f"Trails rebuilt: {total} links, {len(links)} topics.")
