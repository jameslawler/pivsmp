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

display.init()
width = display.getWidth()
height = display.getHeight()

image = Image.new('1', (width, height), 255)
draw = ImageDraw.Draw(image)
draw.line((20, 50, 70, 100), fill = 0)
draw.line((70, 50, 20, 100), fill = 0)
draw.rectangle((20, 50, 70, 100), outline = 0)
draw.line((165, 50, 165, 100), fill = 0)
draw.line((140, 75, 190, 75), fill = 0)
draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
draw.rectangle((80, 50, 130, 100), fill = 0)
draw.chord((200, 50, 250, 100), 0, 360, fill = 0)

display.showImage(image)
display.sleep()
