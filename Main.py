#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

import tkinter
import gui.Gui


def main():
    root = tkinter.Tk()
    gui.Gui.mainGuiFrame(master=root).mainloop()
            
if __name__ == '__main__':
    main()

