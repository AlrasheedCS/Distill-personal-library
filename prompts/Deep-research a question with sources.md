---
type: prompt
saved: '2025-01-01'
status: kept
review: ''
priority: ''
purpose: 'A cited answer you can check'
variables: ['question']
source_chats: []
topics: []
example: false
---

# Deep-research a question with sources

> [!info] Starter prompt shipped with Distill. Edit it, rename it or delete it.

## When to use it

A cited answer you can check.

## Prompt

```text
Research this question: {question}
1. Give the short answer first, then the reasoning.
2. Cite a source for every factual claim, with a link. Prefer primary sources.
3. Separate what's well established, what's debated, and what's unknown.
4. List the 3 best sources to read next.
If sources conflict, show both sides instead of picking one silently.
```

## Variables

- `{question}`

## Notes and variations

%% What worked, what you changed, which AI did it best. %%
