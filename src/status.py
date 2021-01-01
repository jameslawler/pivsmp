import config
import display

print("Display: " + config.getDisplayConfig() + "(" + str(display.getWidth()) + "x" + str(display.getHeight()) + ")")
print("-----------------------------")
print("Movie: " + config.getMovieConfig())
print("Position: " + config.getPositionConfig())
print("Delay: " + config.getDelayConfig() + " seconds")
print("-----------------------------")
