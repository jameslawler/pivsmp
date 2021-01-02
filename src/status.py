#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Status Module
#
# Displays program status with config and e-paper values
#

import config
import display

print("Display: " + config.getDisplayConfig() + " (" + str(display.getWidth()) + "x" + str(display.getHeight()) + ")")
print("-----------------------------")
print("Movie: " + (config.getMovieConfig() or "<None Selected>"))
print("Position: " + config.getPositionConfig())
print("Delay: " + config.getDelayConfig() + " seconds")
print("-----------------------------")
