import argparse

def getArgs():
  parser = argparse.ArgumentParser(description='SlowMovie Settings')
  parser.add_argument('-d', '--delay', default=300,
    help="Delay between screen updates, in seconds")
  parser.add_argument('-s', '--start',
    help="Start at a specific frame (default is read from file)")

  return parser.parse_args()
