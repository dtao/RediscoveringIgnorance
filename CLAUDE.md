# Rediscovering Ignorance — guidance for Claude

This is a personal website and writing project. Articles are written in Markdown with YAML frontmatter and built into a static site by `nescribe.py`.

## Writing articles

When drafting or editing articles, use the existing pieces in `content/` as the style reference — read them before writing. Key traits to preserve:

- **Tone**: Thoughtful, measured, first-person. Intellectually confident but not overclaiming. Hedges ("to me", "I tend to believe") are intentional, not weakness. Comfortable saying "I don't know" while still staking out a position.
- **Structure**: No subheadings. Medium-length paragraphs. Opens with a strong declarative or framing idea; closes with a callback or resonant final sentence.
- **Prose**: Em dashes (---) for asides. Concrete examples anchor abstract arguments. Direct address of the reader ("you", "we") is natural and common. Avoid academic jargon.
- **Length**: Match the complexity of the argument — no padding, no truncation. Philosophy/opinion pieces typically run 500–1200 words.

### Signature moves to preserve

**Narrative-first openings.** Posts almost always begin with a specific scene, personal observation, or short story — not an abstract thesis. The idea emerges from the concrete, not the other way around.

**Extended analogy as the primary argumentative engine.** Nearly every major piece is built around a central analogy or metaphor (a 100-mile chainsaw, a house with many rooms, two men on a beach). The analogy is introduced early, developed throughout, and often returned to at the close. When drafting, identify or invent an analogy before writing the argument.

**Counterintuitive premises.** The blog often stakes out a position that cuts against received wisdom: "Your brain is a liability," "Pride is a weakness," "Modesty is a luxury," "Free will is not an illusion." The title frequently IS the argument. Don't soften or hedge the premise in the opening — earn it through the piece.

**Cross-domain bridging.** Moves freely between software/technology concepts and human relationships, philosophy, and everyday life. Applying a concept from one domain to illuminate another is a signature move, not a quirk to avoid.

**Self-implication.** The author regularly admits he has been guilty of the very thing he's criticizing, or acknowledges his own uncertainty mid-argument. This is a deliberate rhetorical and moral stance — preserve it.

**The "to clarify" move.** Longer pieces often include a paragraph that proactively addresses a likely misreading ("I should clarify: I am not saying X, I am saying Y"). Use this when a central claim risks being misconstrued.

**Challenging common wisdom.** A recurring pattern is to take a piece of received wisdom or a common saying, complicate it, and reframe it more precisely. The reframe is the point of the piece.

When given an outline or rough notes, you don't need to follow the sequence exactly. Look for opportunities to streamline structure and improve flow, but preserve the author's core ideas and voice.

## Book reports from transcripts

Book reports are a distinct kind of article: a record of knowledge I've consumed that has shaped my thinking, as opposed to my own ideas. The raw source material often lives in `transcripts/` — conversations I've had with other LLMs in which I talk through a book from memory. To turn one into an article:

- Treat the transcript as source material, not a script. My half carries the substance; the other LLM is usually just prompting me forward. Pull the book summary and my reflections from what I actually said.
- Skip anything that isn't really about the book (e.g. the other model's book recommendations, unrelated tangents).
- Write a single unified piece in my voice — a summary of what the book argues, woven together with my reflections on it. Follow every rule in "Writing articles" above (narrative opening, central analogy, self-implication, "to clarify" move, no subheadings, em dashes). The book's own central metaphor often makes a natural analogy for the piece.
- If I expressed genuine interest in particular follow-up books during the conversation, a short closing note like "Other books I'm considering reading after this one are…" is welcome. Only include books I actually responded positively to; skip the ones I brushed off.
- Use the book-report frontmatter (see below) so the site renders it as a book report rather than a regular article.

## Site structure

- `content/*.md` — article source files (Markdown + YAML frontmatter)
- `transcripts/*.md` — raw conversation transcripts, often the source material for book reports
- `site/` — Jinja2 templates, CSS, config
- `images/` — inline article images, copied to `build/images/` at build time
- `build/` — generated output (not committed)
- `nescribe.py` — static site generator; run with `python nescribe.py`

## Frontmatter

```yaml
---
title: Article Title
date: YYYY-MM-DD
tags: [tag1, tag2]
---
```

Tags used so far: `philosophy`, `ethics`, `identity`

### Content kinds

`kind` is an optional frontmatter field that separates content types (things I've consumed vs. my own ideas). Currently the only value in use is `book-report`, which also takes a nested `book` object:

```yaml
---
title: The Master and His Emissary
date: 2026-04-23
tags: [philosophy]
kind: book-report
book:
  title: The Master and His Emissary
  author: Iain McGilchrist
---
```

The article `title` and `book.title` can differ — the article title is free to be its own declarative framing, while `book.title` and `book.author` are the canonical metadata for the book being discussed.
