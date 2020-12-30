#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Clear Module
#
# Clears the e-paper display
#

import sys
import display

def clearDisplay():
  epd = display.displayModule.EPD()
  epd.init()
  epd.Clear()
  epd.sleep()

# Main function
# First argument is the e-paper display to use
# Default is epd7in5_V2

args = sys.argv

if len(args) > 1:
  display.changeDisplay(display)

clearDisplay()
