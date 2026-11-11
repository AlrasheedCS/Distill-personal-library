---
type: prompt
saved: '2025-01-01'
status: kept
review: ''
priority: ''
purpose: 'Find and rank the best papers on a question'
variables: ['question', 'field']
source_chats: []
topics: []
example: false
---

# Find research papers on a question

> [!info] Starter prompt shipped with Distill. Edit it, rename it or delete it.

## When to use it

Find and rank the best papers on a question.

## Prompt

```text
Find research papers that answer: {question} (field: {field}).
For each of the 5–10 strongest papers give: title, authors, year, venue, link or DOI, the main finding in one line, method and sample size, and one limit.
Prefer systematic reviews and meta-analyses, then large studies. Say where studies disagree.
Do not invent papers: if you can't verify a paper exists, leave it out and say so.
```

## Variables

- `{question}`
- `{field}`

## Notes and variations

%% What worked, what you changed, which AI did it best. %%
