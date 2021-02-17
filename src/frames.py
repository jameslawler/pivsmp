#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Frames Module
#
# Loads a frame from the movie and returns the image to be displayed
#

import os
from PIL import Image
import ffmpeg

import movies
import display

def getFrameFromVideo(movie, position):
  width = display.getWidth()
  height = display.getHeight()
  movieFilePath = movies.getMoviePath(movie) + "/" + "movie.mp4"
  imageFilePath = movies.getMoviePath(movie) + "/" + "frame.bmp"

  time = "%dms"%(float(position)*41.666666)

  try:
    ffmpeg \
    .input(movieFilePath, ss=time) \
    .filter("scale", "iw*sar", "ih") \
    .filter("scale", width, height, force_original_aspect_ratio=1) \
    .filter("pad", width, height, -1, -1) \
    .output(imageFilePath, vframes=1) \
    .overwrite_output() \
    .run(capture_stdout=True, capture_stderr=True)
  except ffmpeg.Error as e:
    print('stdout:', e.stdout.decode('utf8'))
    print('stderr:', e.stderr.decode('utf8'))
    raise e

  return imageFilePath

def getFrameFromImage(movie, position):
  movieFilePath = movies.getMoviePath(movie)

  imageFilePath = movieFilePath + "/" + str(position).zfill(4) + ".png"

  if not os.path.exists(imageFilePath):
    print("File path does not exist: " + imageFilePath)
    return None

  return imageFilePath

def getFrameImage(movie, position):
  movieFilePath = movies.getMoviePath(movie) + "/" + "movie.mp4"

  if not os.path.exists(movieFilePath):
    imageFilePath = getFrameFromImage(movie, position)
  else:
    imageFilePath = getFrameFromVideo(movie, position)

  image = Image.open(imageFilePath)
  
  return image.convert(mode='1', dither=Image.FLOYDSTEINBERG)
