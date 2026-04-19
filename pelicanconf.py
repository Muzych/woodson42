from __future__ import annotations

from pathlib import Path


AUTHOR = "woodson42"
SITENAME = "woodson42"
SITEURL = ""
PATH = "content"
TIMEZONE = "Asia/Shanghai"
DEFAULT_LANG = "en"

THEME = str(Path(__file__).parent / "theme")
OUTPUT_PATH = "output/"

DIRECT_TEMPLATES = ["index"]
ARTICLE_PATHS = []
PAGE_PATHS = []

STATIC_PATHS = ["extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

DEFAULT_PAGINATION = 0

INDEX_SAVE_AS = "index.html"
ARCHIVES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAGS_SAVE_AS = ""

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True
