import config
import display

print("Display: " + config.getDisplayConfig() + " (" + str(display.getWidth()) + "x" + str(display.getHeight()) + ")")
print("-----------------------------")
print("Movie: " + (config.getMovieConfig() or "<None Selected>"))
print("Position: " + config.getPositionConfig())
print("Delay: " + config.getDelayConfig() + " seconds")
print("-----------------------------")
