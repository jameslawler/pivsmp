#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Display Module
#
# Dynamically loads a WaveShare e-paper display
#

import importlib

import config

SUPPORTED_DISPLAYS = [
  "epd1in02",
  "epd1in54_V2",
  "epd1in54",
  "epd1in54b_V2",
  "epd1in54b",
  "epd1in54c",
  "epd2in7",
  "epd2in7b",
  "epd2in9",
  "epd2in9b_V2",
  "epd2in9bc",
  "epd2in9d",
  "epd2in13_V2",
  "epd2in13",
  "epd2in13b_V2",
  "epd2in13bc",
  "epd2in13d",
  "epd4in2",
  "epd4in2bc",
  "epd5in65f",
  "epd5in83",
  "epd5in83bc",
  "epd7in5_HD",
  "epd7in5_V2",
  "epd7in5",
  "epd7in5b_HD",
  "epd7in5b_V3",
  "epd7in5bc_V2",
  "epd7in5bc"
]

display = config.getDisplayConfig()
displayModule = importlib.import_module("waveshare_epd." + display)

epd = displayModule.EPD()

def init():
  epd.init()

def clear():
  epd.clear()

def sleep():
  epd.sleep()

def getWidth():
  return epd.width

def getHeight():
  return epd.height

def showImage(image):
  buffer = epd.getbuffer(image)
  epd.display(buffer)

def shutdown():
  clear()
  sleep()
  displayModule.epdconfig.module_exit()