#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk, Gdk
import db_connect, initiate, lib, menu, lang


class main_gui(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title=lib.WINDOW_TITLE)
		self.db = db_connect.connection_handler()
		self.set_vars = initiate.set_values()

		self.set_default_size(self.set_vars.var['width'], self.set_vars.var['height'])
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_border_width(10)
		self.connect('destroy', Gtk.main_quit)
		
		try:
			self.set_icon_from_file(lib.TITLE_ICON)
		except:
			pass
		
		action_group = Gtk.ActionGroup("my_actions")
		
		self.add_file_menu_actions(action_group)
			
		uimanager = self.create_ui_manager()
		uimanager.insert_action_group(action_group)
		
		menubar = uimanager.get_widget("/MenuBar")
		
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		box.pack_start(menubar, False, False, 0)
		
		toolbar = uimanager.get_widget("/ToolBar")
		box.pack_start(toolbar, False, False, 0)
		
		self.add(box)

	def add_file_menu_actions(self, action_group):
		action_filemenu = Gtk.Action("openMenu", lang.OPEN, None, None)
		action_group.add_action(action_filemenu)

		action_filenewmenu = Gtk.Action("open", None, None, Gtk.STOCK_OPEN)
		action_group.add_action(action_filenewmenu)

		action_filequit = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
		action_filequit.connect("activate", self.on_menu_file_quit)
		action_group.add_action(action_filequit)
		
		action_new = Gtk.Action("SQLite", lang.MENU_OPEN_SQLITE, "Create a new file", Gtk.STOCK_OPEN)
		action_new.connect("activate", self.on_menu_file_new_generic)
		action_group.add_action_with_accel(action_new, None)
		
		action_group.add_actions([ 
			("MySQL", None, lang.MENU_OPEN_MYSQL, None, "Create new foo",
             self.on_menu_file_new_generic),
            ("MSSQL", None, lang.MENU_OPEN_MSSQL, None, "Create new goo",
             self.on_menu_file_new_generic),
        ])
		
	def create_ui_manager(self):
		uimanager = Gtk.UIManager()
		
        # Throws exception if something went wrong
		uimanager.add_ui_from_string(menu.UI_INFO)

        # Add the accelerator group to the toplevel window
		accelgroup = uimanager.get_accel_group()
		self.add_accel_group(accelgroup)	
		return uimanager
		
	def on_menu_file_quit(self, widget):
		Gtk.main_quit()
	
	def create_widgets(self):
		pass

	def on_menu_file_new_generic(self, widget):
		print("A File|New menu item was selected.")

def main():
	pass

if __name__ == '__main__':
	main()

