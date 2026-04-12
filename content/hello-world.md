---
title: Hello, World
date: 2026-04-12
tags: [welcome, meta]
---

This is the first post — a quick test of the static site generator. Add your own articles to the `content/` directory and run `python nescribe.py` to rebuild the site.

## Writing Articles

Each article is a Markdown file in `content/` with a YAML frontmatter block at the top:

```markdown
---
title: My Article Title
date: 2026-04-15
tags: [nature, science]
---

Your content goes here.
```

The generator reads every `.md` file, converts it to HTML using your templates in `site/`, and writes the output to `build/`.

## Customizing the Site

Edit `site/config.yaml` to set the site title and description. The templates in `site/` control all structure and layout — `base.html` defines the shared shell, while `index.html` and `article.html` fill in the content for each page type.
