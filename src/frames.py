from PIL import Image

import movies

def getFrameImage(movie, position):
  moviePath = movies.getMoviePath(movie)

  imageFilePath = moviePath + str(currentPosition).zfill(4) + ".png"

  if not os.path.exists(imageFilePath):
    return None

  image = Image.open(imageFilePath)
  
  return image.convert(mode='1', dither=Image.FLOYDSTEINBERG)
