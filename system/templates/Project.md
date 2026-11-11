---
type: project
saved: '{{date:YYYY-MM-DD}}'
status: active
topics: []
projects: []
example: false
---

# {{title}}

## Outcome

## Next action

- [ ] Define the next concrete step.

## My notes and highlights

%% Yours: notes you took and highlights you kept while researching this project, from chats, Readwise, X or anywhere. Paste, write, or link to them (e.g. [[<note>#<heading>]]). AIs never write in this section. %%

## Ideas

%% One line per idea for this project, each linking the find or chat behind it. AI-proposed ideas sit in an [!ai] box until you accept them: move the ones you keep out of the box. %%

## Finds for this project

%% Any find whose `projects` property links this note shows up here automatically. %%

```base
filters:
  and:
  - file.hasLink(this.file)
  - type == "find"
properties:
  file.name:
    displayName: Find
  about:
    displayName: About
views:
- type: table
  name: Finds for this project
  order:
  - file.name
  - about
  - author
  - saved
  sort:
  - property: saved
    direction: DESC
```

## Chats in this project

%% Any chat whose `projects` property links this note shows up here automatically. %%

```base
filters:
  and:
  - file.hasLink(this.file)
  - type == "chat"
properties:
  file.name:
    displayName: Chat
  about:
    displayName: About
  source:
    displayName: From
views:
- type: table
  name: Chats in this project
  order:
  - file.name
  - about
  - source
  - saved
  sort:
  - property: saved
    direction: DESC
```

## Supporting notes

## Decisions

## Done when
