#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
import initiate
import lib


class notebookFrame(ttk.Frame):
    """Notebook, contains notbook and tabs related
    to the notebook"""
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        
        lable = tkinter.Label(self, text = "Notebook")
        lable.pack(anchor="ne", pady=5, side="left")
        

class menuFrame(ttk.Frame):
    """Contains everything related to the
    menu and toolbar"""
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.initUI()
        
    def initUI(self):
        
        self.menubar = tkinter.Menu(self)
        self.fileMenu = tkinter.Menu(self, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        
        toolbar = tkinter.Frame(self, bd=1, relief='raised')

        exitButton = tkinter.Button(toolbar, text='Exit', relief='flat',
            command=self.quit)

        exitButton.pack(side='left', padx=2, pady=2)
        
        toolbar.pack(side='top', fill='x')
        
    def setMenu(self):
         return self.menubar
       
    def onExit(self):
        self.quit()


class treeviewFrame(ttk.Frame):
    """Contains the treeview and related scrollbar"""
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        
        lable = tkinter.Label(self, text = "TreeWiew")
        lable.pack(anchor="ne", pady=5, side="left")


class mainGuiFrame(ttk.Frame):
    """Connects all different parts of the gui"""
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.master.title(lib.WINDOW_TITLE)
        self.master.geometry('{w}x{h}'.format(w=initiate.defVars['width'],
                                            h=initiate.defVars['height']))

        s1 = ttk.Style()
        s1.configure('f1.TFrame', background='blue')                                    
        s2 = ttk.Style()
        s2.configure('f2.TFrame', background='green')
        s3 = ttk.Style()
        s3.configure('f3.TFrame', background='yellow')
        s4 = ttk.Style()
        s4.configure('f4.TFrame', background='red')
        
        self.frame1 = menuFrame(self, style='f1.TFrame')
        self.frame1.pack(fil='x')
        
        self.frame2 = treeviewFrame(self, style='f2.TFrame')
        self.frame2.pack(side='left', fill='y')                         #Side will be changable in Gui, Config or arguments
        
        self.frame3 = notebookFrame(self, style='f3.TFrame')
        self.frame3.pack(fill='both', expand=True)
        
        self.master.config(menu=self.frame1.setMenu())
        
        self.pack(expand=True, fill='both')

         
def main():
	pass

if __name__ == '__main__':
	main()

