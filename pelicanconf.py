#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Tahoe-LAFS team'
SITENAME = 'Tahoe-LAFS'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

THEME = 'theme/tahoe'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (('News', '/category/news.html'),
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
