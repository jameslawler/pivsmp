#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Movies Module
#
# List movies
#

import os

MOVIES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'movies/')

def listMovies():
  if (not os.path.exists(MOVIES_PATH)):
    return []

  filesAndFolders = os.listdir(MOVIES_PATH)
  return [ name for name in filesAndFolders if os.path.isdir(MOVIES_PATH + name) ]

def hasMovies():
  movies = listMovies()
  return len(movies) > 0

def checkMovieExists(movie):
  movies = listMovies()
  return movie in movies

def getMoviePath(movie):
  return MOVIES_PATH + movie