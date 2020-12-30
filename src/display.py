#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Display Module
#
# Dynamically loads a WaveShare e-paper display
#

import importlib

DEFAULT_DISPLAY = "epd7in5_V2"

displayModule = importlib.import_module("waveshare_epd." + DEFAULT_DISPLAY)

def changeDisplay(display):
  global displayModule
  displayModule = importlib.import_module("waveshare_epd." + display)