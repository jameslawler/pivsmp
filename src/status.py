import config
import display

print("Display: " + config.getDisplayConfig() + "(" + display.getWidth() + "x" + display.getHeight() + ")")
print("-----------------------------")
print("Movie: " + config.getMovieConfig())
print("Position: " + config.getPositionConfig())
print("Delay: " + config.getDelayConfig() + " seconds")
print("-----------------------------")
