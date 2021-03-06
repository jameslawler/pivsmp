#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# PiVSMP Module
#
# Core program with frame loop
#

import time

import display
import config
import frames

display.init()
display.clear()    

while 1:
  movie = config.getMovieConfig()
  position = config.getPositionConfig()
  delay = config.getDelayConfig()

  if (not movie):
    print("No movie configured. Exiting...")
    display.shutdown()
    exit(1)
  
  image = frames.getFrameImage(movie, position)

  if (not image):
    print("Could not load frame")
    display.shutdown()
    exit(1)

  print("Displaying image " + str(position).zfill(4))

  display.showImage(image)
  position = str(int(position) + 1)
  config.setPositionConfig(position)

  # Wait for delay until next frame is shown
  display.sleep()
  time.sleep(float(delay))
  display.init()

display.shutdown()
exit()