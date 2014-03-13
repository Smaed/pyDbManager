#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import gui

def main():
	window = gui.main_gui()
	window.show_all()
	Gtk.main()
	
if __name__ == '__main__':
	main()

