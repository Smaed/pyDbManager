#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

import gui
import tkinter
import dbHandlers

def main():
    root = tkinter.Tk()
    gui.mainGuiFrame(master=root).mainloop()
	
if __name__ == '__main__':
	main()

