#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

AUTHOR = u'goorockey'
SITENAME = u"Goorockey's Life"
SITEURL = 'http://www.goorockey.com'
#SITEURL = 'http://127.0.0.1:8000'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

PATH = 'content'
THEME = 'themes/pelican-elegant'
PAGE_DIR = 'pages'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'
LOCALE = (u'zh_CN.utf8')

USE_FOLDER_AS_CATEGORY = True
REVERSE_CATEGORY_ORDER = True

SUMMARY_MAX_LENGTH = 50

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
#TAG_URL = 'tags/{slug}.html'
#TAG_SAVE_AS = TAG_URL
#TAGS_SAVE_AS = 'tags/index.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = u'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
            ('Dian', 'http://www.dian.org.cn'),
            ('SeedClass', 'http://www.seedclass.com'),
            ('ThankCreate', 'http://www.thankcreate.com'),
        )

PLUGIN_PATH = ['plugins/',]
PLUGINS = (
            'gist',
            'sitemap',
            'gzip_cache',
            'extract_toc',
            'tipue_search',
            'summary',
            'neighbors',
          )

# Social widget
SOCIAL = (
            ('Github', 'http://github.com/goorockey'),
            ('RSS', 'http://feed.goorockey.com'),
         )

DEFAULT_PAGINATION = 6


SITEMAP = {
        "format": "xml",
        "priorities": {
            "articles": 0.7,
            "indexes": 0.5,
            "pages": 0.3,
            },
        "changefreqs": {
            "articles": "monthly",
            "indexes": "daily",
            "pages": "monthly",
            }
        }

STATIC_PATHS = [
        "uploads",
        "extra/robots.txt",
        "extra/CNAME",
        "extra/favicon.ico",
        ]
EXTRA_PATH_METADATA = {
        'extra/robots.txt': {'path': 'robots.txt'},
        'extra/CNAME': {'path': 'CNAME'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
        }

DISQUS_SITENAME = "goorockeyslife"
GOOGLE_ANALYTICS = 'UA-28958629-1'
GITHUB_URL = 'http://github.com/goorockey'


SITE_LICENSE = u"本博客遵循CC协议2.5，即署名-非商业使用-相同方式共享。所有未明确注明转载来源的文章均为本博客原创文章，对于原创文章的转载请注明作者并保持原文链接，否则保留追究法律责任的权利。"

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
