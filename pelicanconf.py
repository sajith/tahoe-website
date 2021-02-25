#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Tahoe-LAFS team'
SITENAME = 'Tahoe-LAFS'

# MENUITEMS can't contain relative URLs (see
# https://github.com/getpelican/pelican/issues/2272), so I need to toggle
# SITEURL for previewing stuff locally.
# SITEURL = ''
SITEURL = 'https://sajith.github.io/tahoe-website'

PATH = 'content'

TIMEZONE = 'UTC'

THEME = 'theme/tahoe'

DEFAULT_LANG = 'en'

# Confusing/dangerous when feeds are involved, but kind of necessary to host
# stuff on GitHub pages.
# RELATIVE_URLS = True

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

MENUITEMS = (('News', SITEURL + '/category/news'),
             ('Trac', 'https://tahoe-lafs.org/trac/tahoe-lafs'),
             ('GitHub', 'https://github.com/tahoe-lafs/tahoe-lafs'),
             ('Docs', 'https://tahoe-lafs.readthedocs.org'),)


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
