---
type: chat
kind: code
cssclasses:
- code-session
depth: full
source: claude-code
chat_id: unknown
about: 'A small script that renames recipe photos by date taken'
main_insight: 'Read the EXIF date first and fall back to the file date, or half the photos get the wrong name.'
url: ''
transcript: ''
saved: '2025-01-20'
chatgpt_project: ''
repo: 'example/photo-renamer'
outcome: worked
coding_vault: ''
pinned: false
status: kept
review: ''
priority: ''
topics: []
projects: []
why_saved: 'The EXIF fallback is reusable'
example: true
---

# Rename photos by date (example)

> [!warning] Fictional example. Not a real session.

## About

**Goal:** rename a folder of photos to `YYYY-MM-DD-n.jpg`.
**Outcome:** worked, after one fix.

## What I asked

### 1.
> Write a script that renames every photo in this folder by the date it was taken.

Wrote `rename.py`; dry-run mode by default.

## Decisions

- Dry run by default; `--apply` to rename. Rejected: renaming in place straight away.

## What broke and the fix

- Screenshots have no EXIF date, so they crashed the script. Fix: fall back to the file's modified date.

## Where

- **Repo / folder:** `example/photo-renamer`
- **Files touched:** `rename.py`
