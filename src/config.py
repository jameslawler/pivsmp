import os

configDirectory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config/')
currentPositionPath = configDirectory + 'settings.cfg'

def getCurrentPosition():
  if not os.path.exists(currentPositionPath):
    return 1

  currentPositionFile = open(currentPositionPath)

  for line in currentPositionFile:
    return int(line)

  return 1

def saveCurrentPosition(currentPosition):
  log = open(currentPositionPath, 'w')
  log.write(str(currentPosition))
  log.close()
