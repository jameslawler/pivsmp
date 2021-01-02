#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# Config Module
#
# Get and Write configuration settings to file
#

import os
import configparser

import constants

DEFAULT_DISPLAY = "epd7in5_V2"
DEFAULT_MOVIE = None
DEFAULT_DELAY = "120"
DEFAULT_POSITION = "1"

CONFIG_FILE_PATH = os.path.join(constants.CONFIG_FOLDER_PATH, 'pivsmp.ini')

def loadConfig():
  if (os.path.exists(CONFIG_FILE_PATH)):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE_PATH)
    return config
  else:
    return None

def getDisplayConfig():
  config = loadConfig()
  if (config):
    return config['pivsmp']['display'] or DEFAULT_DISPLAY
  else:
    return DEFAULT_DISPLAY

def getMovieConfig():
  config = loadConfig()
  if (config):
    return config['pivsmp']['movie'] or DEFAULT_MOVIE
  else:
    return DEFAULT_MOVIE

def getPositionConfig():
  config = loadConfig()
  if (config):
    return config['pivsmp']['position'] or DEFAULT_POSITION
  else:
    return DEFAULT_POSITION

def getDelayConfig():
  config = loadConfig()
  if (config):
    return config['pivsmp']['delay'] or DEFAULT_DELAY
  else:
    return DEFAULT_DELAY

def setConfig(display, movie, position, delay):
  config = loadConfig() or configparser.ConfigParser()

  if (not config.has_section("pivsmp")):
    config.add_section("pivsmp")

  config['pivsmp']['display'] = display
  config['pivsmp']['movie'] = movie
  config['pivsmp']['position'] = position
  config['pivsmp']['delay'] = delay

  with open(CONFIG_FILE_PATH, 'w') as configFile:
    config.write(configFile)

def setPositionConfig(position):
  config = loadConfig()

  if (not config):
    print("No config found. Exiting...")
    exit(1)
  
  config['pivsmp']['position'] = position

  with open(CONFIG_FILE_PATH, 'w') as configFile:
    config.write(configFile)
