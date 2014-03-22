#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

import tkinter
import gui
import dbHandlers

def main():
    root = tkinter.Tk()
    gui.mainGuiFrame(master=root).mainloop()
	
if __name__ == '__main__':
	main()

