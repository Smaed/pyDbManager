#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
import initiate

class NotebookFrame(ttk.Frame):
    '''Notebook, contains notbook and frames related
    to the notebook'''
    
    def __init__(self, master):
        self.master = master
        super().__init__(master)


class MenuFrame(ttk.Frame):
    '''Contains everything related to the
    menu and toolbar'''
    
    def __init__(self, master):
        self.master = master
        super().__init__(master)


class TreeviewFrame(ttk.Frame):
    '''Contains the treeview and related scrollbar'''
    
    def __init__(self, master):
        self.master = master
        super().__init__(master)


class MainGuiFrame(ttk.Frame):
    '''Connects all different parts of the gui'''
    
    def __init__(self, master):
        self.master = master
        self.master.geometry('{w}x{h}'.format(w=initiate.defVars['width'],
                                            h=initiate.defVars['height']))
        super().__init__(master)
            
            
def main():
	pass

if __name__ == '__main__':
	main()

