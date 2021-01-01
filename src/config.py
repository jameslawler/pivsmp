import os
import configparser

DEFAULT_DISPLAY = "epd7in5_V2"
DEFAULT_MOVIE = None
DEFAULT_DELAY = "120"
DEFAULT_POSITION = "1"

def loadConfig():
  configDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/')
  configFilePath = configDirectory + 'pivsmp.ini'

  if (os.path.exists(configFilePath)):
    config = configparser.ConfigParser()
    config.read(configFilePath)
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

  with open(configFilePath, 'w') as configFile:
    config.write(configFile)

def setPositionConfig(position):
  config = loadConfig()

  if (not config):
    print("No config found. Exiting...")
    exit(1)
  
  config['pivsmp']['position'] = position

  with open(configFilePath, 'w') as configFile:
    config.write(configFile)
