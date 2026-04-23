#!/usr/bin/env python3
"""nescribe — minimal static site generator

Content:   content/*.md  (Markdown with YAML frontmatter)
Templates: site/*.html   (Jinja2), site/style.css, site/config.yaml
Output:    build/
"""

import shutil
import xml.etree.ElementTree as etree
from pathlib import Path

import yaml
import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from jinja2 import Environment, FileSystemLoader

CONTENT_DIR = Path("content")
SITE_DIR    = Path("site")
IMAGES_DIR  = Path("images")
BUILD_DIR   = Path("build")


class ImageCaptionTreeprocessor(Treeprocessor):
    """Wrap paragraphs containing a lone image in <figure>, promoting alt text to <figcaption>."""

    def run(self, root):
        for parent in list(root.iter()):
            for child in list(parent):
                if (child.tag == "p"
                        and len(child) == 1
                        and child[0].tag == "img"
                        and not (child.text or "").strip()
                        and not (child[0].tail or "").strip()):
                    img = child[0]
                    figure = etree.Element("figure")
                    figure.append(img)
                    alt = img.get("alt")
                    if alt:
                        caption = etree.SubElement(figure, "figcaption")
                        caption.text = alt
                    idx = list(parent).index(child)
                    parent.remove(child)
                    parent.insert(idx, figure)


class ImageCaptionExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(ImageCaptionTreeprocessor(md), "image_caption", 5)


_md = markdown.Markdown(extensions=["fenced_code", "smarty", "tables", ImageCaptionExtension()])


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML frontmatter from body. Returns (meta, body)."""
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}, text
    return yaml.safe_load(parts[1]) or {}, parts[2]


def render_md(text: str) -> str:
    _md.reset()
    return _md.convert(text)


def parse_article(path: Path) -> dict:
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    body = body.strip()
    return {
        "title":   meta.get("title", path.stem.replace("-", " ").title()),
        "date":    meta.get("date"),
        "tags":    meta.get("tags") or [],
        "slug":    path.stem,
        "content": render_md(body),
        "excerpt": render_md(body.split("\n\n")[0]),
        "url":     f"articles/{path.stem}.html",
    }


def build():
    config = {}
    config_path = SITE_DIR / "config.yaml"
    if config_path.exists():
        config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}

    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir()
    (BUILD_DIR / "articles").mkdir()

    for asset in SITE_DIR.rglob("*"):
        if asset.is_file() and asset.suffix not in ('.html', '.yaml'):
            dest = BUILD_DIR / asset.relative_to(SITE_DIR)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(asset, dest)

    if IMAGES_DIR.exists():
        shutil.copytree(IMAGES_DIR, BUILD_DIR / "images")

    env = Environment(loader=FileSystemLoader(str(SITE_DIR)), autoescape=True)

    articles = [parse_article(p) for p in CONTENT_DIR.glob("*.md")]
    articles.sort(key=lambda a: (a["date"] is not None, a["date"]), reverse=True)

    base_ctx = dict(site=config, articles=articles)

    index_tmpl = env.get_template("index.html")
    (BUILD_DIR / "index.html").write_text(
        index_tmpl.render(**base_ctx, recent=articles[:10], root="."),
        encoding="utf-8",
    )

    article_tmpl = env.get_template("article.html")
    for article in articles:
        (BUILD_DIR / "articles" / f"{article['slug']}.html").write_text(
            article_tmpl.render(**base_ctx, article=article, root=".."),
            encoding="utf-8",
        )

    print(f"Built {len(articles)} article(s) → {BUILD_DIR}/")


if __name__ == "__main__":
    build()
