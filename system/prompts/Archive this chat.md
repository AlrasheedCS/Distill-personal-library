# Archive this chat

For chats no AI can save directly. Paste the block into the conversation itself (this adds a message to it), then paste the answer into a [[system/templates/Chat capture|Chat capture]] note. AIs with access to the vault should follow [[system/prompts/Save this chat]] instead.

```text
Summarize this conversation for my notes, in Markdown, in exactly this order:

## About
**Started as:** what the chat was first about
**Turned into:** what it ended up being about (or "same")

## Main insight
The single most useful takeaway, 1–2 sentences.

## Prompts and answers
For each of my prompts, in order (skip "thanks/ok/continue" and say how many you skipped):
### N. <3–6 word label>
> my prompt, word for word (if over ~120 words, the first lines then "…")
then your answer, condensed: keep every option, approach, list item, step, recommendation, number and caveat (tables for comparisons); drop greetings, narration, repetition and hedging.

## More
### Other insights
> [!warning]- Unverified
> - factual claims you made without a cited source
### Next actions
Only actions I explicitly stated. Otherwise omit.

Text only: do not embed images or copy attachments. Keep those in the original chat/archive; include the original-chat link when known.

Use only this conversation. Don't invent links, decisions or sources. No YAML.
```

[[system/Capture chats]] · [[Home]]
