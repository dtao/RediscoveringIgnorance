# Rediscovering Ignorance — guidance for Claude

This is a personal website and writing project. Articles are written in Markdown with YAML frontmatter and built into a static site by `nescribe.py`.

## Writing articles

When drafting or editing articles, use the existing pieces in `content/` as the style reference — read them before writing. Key traits to preserve:

- **Tone**: Thoughtful, measured, first-person. Intellectually confident but not overclaiming. Hedges ("to me", "I tend to believe") are intentional, not weakness.
- **Structure**: No subheadings. Medium-length paragraphs. Opens with a strong declarative or framing idea; closes with a callback or resonant final sentence.
- **Prose**: Em dashes (---) for asides. Concrete examples anchor abstract arguments. Avoid academic jargon.
- **Length**: Match the complexity of the argument — no padding, no truncation.

When given an outline or rough notes, you don't need to follow the sequence exactly. Look for opportunities to streamline structure and improve flow, but preserve the author's core ideas and voice.

## Site structure

- `content/*.md` — article source files (Markdown + YAML frontmatter)
- `site/` — Jinja2 templates, CSS, config
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
