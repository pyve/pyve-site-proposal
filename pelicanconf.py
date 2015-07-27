#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fundación Python Venezuela'
SITENAME = 'Python Venezuela'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Caracas'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('@pyconve', 'http://twitter.com/pyconve'),
          ('#pyve','https://twitter.com/search?q=%23pyve'),
	  ('irc','http://webchat.freenode.net/?channels=python-ve&uio=MTE9ODIdf'),
	  ('linkedin','http://www.linkedin.com/groups/Python-Venezuela-4613465'),
	  ('google+','https://plus.google.com/101468780661156563423'),
	  ('lista de correos','http://goo.gl/ug9by'),
	  ('github','https://github.com/pyve'),
	  ('telegram', 'https://telegram.me/joinchat/046ea0cf01b34af4ea68c255517e0806'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'Just-Read'
