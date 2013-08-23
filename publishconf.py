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
OUTPUT_RETENTION = ['.git', '.gitignore', 'CNAME']
DELETE_OUTPUT_DIRECTORY = True
GOOGLE_ANALYTICS = u'UA-43454971-1'
