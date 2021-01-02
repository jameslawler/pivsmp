#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Constants Module
#
# Program wide constants
#

import os
from os.path import expanduser

HOME = expanduser("~")
CONFIG_FOLDER_PATH = os.path.join(HOME, ".pivsmp/config")
MOVIES_FOLDER_PATH = os.path.join(HOME, ".pivsmp/movies")
