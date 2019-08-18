# Handles getting/setting wallpapers

from icecore import *

# Gets the path of the current wallpaper
def get_wallpaper():
	return ""
	
def set_wallpaper(image_path, is_centered, is_scaled):
	print("New wallpaper: " + image_path) 
	return icewmbg(["--image=" + image_path, 
	"--center=" + str(int(is_centered)), 
	"--scaled=" + str(int(is_scaled))])
	
def set_background_color(background_color):
	return

set_wallpaper("/home/pi/Downloads/test2.jpg", True, True)
print("Changed wallpaper")
