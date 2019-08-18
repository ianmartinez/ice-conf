import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from icedesktop import *

class Handler:
	def onDestroy(self, *args):
		Gtk.main_quit()
		
	def change_image(self, button):
		set_wallpaper(button.get_filename(), True, True)
        
	def change_color(self, button):
		return
			
	def toggle_centered(self, button):
		return
	
	def toggle_scaled(self, button):
		return
		
	def toggle_use_image(self, button):
		return

builder = Gtk.Builder()
builder.add_from_file("ui.glade")
builder.connect_signals(Handler())

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()
