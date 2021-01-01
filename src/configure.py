import questionary

import config
import display
import movies

if (not movies.hasMovies()):
  print("No movies found. Please add to the movies directory (" + movies.MOVIES_PATH + ")")
  exit(1)

defaultMovie = config.getMovieConfig()
if (not movies.checkMovieExists(defaultMovie)):
  defaultMovie = None

answers = questionary.form(
  display = questionary.select("Which e-paper display do you have?", choices=display.SUPPORTED_DISPLAYS, default=display.DEFAULT_DISPLAY),
  movie = questionary.select("Which movie do you want to show?", choices=movies.listMovies(), default=defaultMovie),
  position = questionary.text("Which frame number to show next?"),
  delay = questionary.select("How many seconds to wait between frames?", choices=["60", "120", "180", "240", "300"], default="120"),
  confirm = questionary.confirm("Are you sure you want to update the config?")
).ask()

if (answers["confirm"]):
  config.setConfig(answers["display"], answers["movie"], answers["position"], answers["delay"])
  print("Config updated. Use the `pivsmp restart` feature to start using the new config.")
else:
  print("Changes not saved.")