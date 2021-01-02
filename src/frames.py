#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Frames Module
#
# Loads a frame from the movie and returns the image to be displayed
#

import os
from PIL import Image

import movies

def getFrameImage(movie, position):
  moviePath = movies.getMoviePath(movie)

  imageFilePath = moviePath + "/" + str(position).zfill(4) + ".png"

  if not os.path.exists(imageFilePath):
    print("File path does not exist: " + imageFilePath)
    return None

  image = Image.open(imageFilePath)
  
  return image.convert(mode='1', dither=Image.FLOYDSTEINBERG)
