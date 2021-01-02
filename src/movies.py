#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Movies Module
#
# List movies
#

import os

import constants

def listMovies():
  if (not os.path.exists(constants.MOVIES_FOLDER_PATH)):
    print("Movies folder does not exist")
    return []

  filesAndFolders = os.listdir(constants.MOVIES_FOLDER_PATH)
  return [ name for name in filesAndFolders if os.path.isdir(os.path.join(constants.MOVIES_FOLDER_PATH, name)) ]

def hasMovies():
  movies = listMovies()
  return len(movies) > 0

def checkMovieExists(movie):
  movies = listMovies()
  return movie in movies

def getMoviePath(movie):
  return os.path.join(constants.MOVIES_FOLDER_PATH, movie)