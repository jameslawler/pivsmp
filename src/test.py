#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Test Module
#
# Draws a test pattern on the display
#

import sys
from PIL import Image,ImageDraw

import display

def displayTestMessage():
  epd = display.displayModule.EPD()
  epd.init()

  Himage = Image.new('1', (epd.width, epd.height), 255)
  draw = ImageDraw.Draw(Himage)
  draw.line((20, 50, 70, 100), fill = 0)
  draw.line((70, 50, 20, 100), fill = 0)
  draw.rectangle((20, 50, 70, 100), outline = 0)
  draw.line((165, 50, 165, 100), fill = 0)
  draw.line((140, 75, 190, 75), fill = 0)
  draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
  draw.rectangle((80, 50, 130, 100), fill = 0)
  draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
  epd.display(epd.getbuffer(Himage))
  epd.sleep()

# Main function
# First argument is the e-paper display to use
# Default is epd7in5_V2

args = sys.argv

if len(args) > 1:
  display.changeDisplay(display)

displayTestMessage()