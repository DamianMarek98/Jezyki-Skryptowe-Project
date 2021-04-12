import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk

class Main:
    def __init__(self):
        gladeFile = "test.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)
        window = self.builder.get_object("GtkWindow")
        window.connect("delete-event", gtk.main_quit)
        window.show()
