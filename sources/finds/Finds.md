---
type: guide
summary: "Finds: posts, threads, repos and pages from your feed (mostly X) kept for your projects and setups."
---

# Finds

Things you bookmarked from your feed, mostly X: one small note each, with the post as captured, **My take** (yours) and a short AI line on why it matters. A find joins a project through its `projects` property and then shows up on that project's note. Captured through [[inbox/to sort|To sort]]; filed at the sort. Not chats, not searches.

```base
filters:
  and:
  - file.inFolder("sources/finds")
  - type == "find"
properties:
  file.name:
    displayName: Find
  about:
    displayName: About
views:
- type: table
  name: All finds
  order:
  - file.name
  - about
  - projects
  - priority
  - saved
  sort:
  - property: saved
    direction: DESC
```

[[Home]]
