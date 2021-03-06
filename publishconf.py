#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = u'http://oncrashreboot.com'
OUTPUT_RETENTION = ['.git', '.gitignore', 'CNAME', 'README.md', 'robots.txt']
DELETE_OUTPUT_DIRECTORY = True
GOOGLE_ANALYTICS = u'UA-43454971-1'
DISQUS_SITENAME = u'oncrashreboot'
STAT_COUNTER_PROJECT = 9376577
STAT_COUNTER_SECURITY = u'8d87792a'

