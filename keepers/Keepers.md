---
type: guide
summary: "Your best-of shelf: final findings after searching and asking, across every area. Only you change or delete anything here."
---

# Keepers

The cream of what you found: the final answer after the searching, chatting and comparing. A best pick, a tip that works, a prompt you trust, a verdict you reached. **Only you edit, move or delete anything here.** AIs may propose keepers (drafts in `agent/outputs/keeper-candidates/`) and add one only when you say "keep this". Every change is in the version history.

Areas: Food · Cities and travel · Writing · Coding · AI tools · Health and fitness · Shopping · Money · Home · Learning · Other. One note per keeper; set its `area`. New keeper: template [[system/templates/Keeper]].

```base
filters:
  and:
  - file.inFolder("keepers")
  - type == "keeper"
  - example != true
properties:
  file.name:
    displayName: Keeper
  verdict:
    displayName: The finding
  area:
    displayName: Area
  kind:
    displayName: Kind
views:
- type: table
  name: By area
  groupBy:
    property: area
    direction: ASC
  order:
  - file.name
  - verdict
  - kind
  - confirmed
- type: table
  name: Due for a recheck
  filters:
    and:
    - recheck != ""
    - recheck <= today()
  order:
  - file.name
  - verdict
  - recheck
```

> [!tip]- What makes a keeper
> - **Final, not raw:** the conclusion you'd act on, with the one or two sources that got you there (chats, finds, searches).
> - **Kinds:** `pick` (the best X), `tip`, `prompt`, `how-to`, `verdict` (a decision and why), `list` (your shortlist).
> - **Things that change** (restaurants, prices, tools): set `recheck` to a date; it appears under *Due for a recheck*.
> - Proposed by an AI and waiting for you: *Waiting for you* on [[Home]].

[[Home]]
