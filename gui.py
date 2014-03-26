#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
import initiate
import lib
import db_connect

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

        self.menubar = tkinter.Menu(self)
        
        self.fileMenu = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.newMenu = tkinter.Menu(self.fileMenu, tearoff=0)
        self.fileMenu.add_cascade(label="New", menu=self.newMenu)
        
        self.openMenu = tkinter.Menu(self.fileMenu, tearoff=0)
        self.fileMenu.add_cascade(label="Open", menu=self.openMenu)

        self.fileMenu.add_command(label="Exit", command=self.master.onExit)
        
        exitButton = ttk.Button(self, style   =  'toolbar.TButton', 
                                         text    =  'Exit', 
                                         command =  self.master.onExit)

        exitButton.pack(side='left', padx=2, pady=2)
        
        self._populateMenu()
        
        
    def _populateMenu(self):                        #Will be extended to include options on how a db will open (filebox,loginbox)
        for db_type in db_connect.db_types:
            self.newMenu.add_command(label=db_type, 
                                    command=lambda db_type=db_type: self.master.onNew(db_type))
        for db_type in db_connect.db_types:
            self.openMenu.add_command(label=db_type, 
                                    command=lambda db_type=db_type: self.master.onOpen(db_type))
            
        
    def setMenu(self):
        return self.menubar


class treeviewFrame(ttk.Frame):
    """Contains the treeview and related scrollbar"""
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        
        self.tree = ttk.Treeview(self)
        self.tree.pack(fill='y', expand=True)


class mainGuiFrame(ttk.Frame):
    """Connects all different parts of the gui"""
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.master.title(lib.WINDOW_TITLE)
        self.master.geometry('{w}x{h}'.format(w=initiate.defVars['width'],
                                            h=initiate.defVars['height']))

        s1 = ttk.Style()
        s1.configure('toolbar.TFrame', relief='flat', bd=1)
        s1.configure('toolbar.TButton', relief='flat')
        s1.configure('f2.TFrame', background='green')
        s1.configure('f3.TFrame', background='yellow')
        s1.configure('f4.TFrame', background='red')
        
        self.frame1 = menuFrame(self, style='toolbar.TFrame')
        self.frame1.pack(fill='x', side=initiate.defVars['toolBar'])     #Side will be changable in Gui, Config or arguments
        
        self.frame2 = treeviewFrame(self, style='f2.TFrame')
        self.frame2.pack(fill='y', side=initiate.defVars['treeSide'])  #Side will be changable in Gui, Config or arguments
        
        self.frame3 = notebookFrame(self, style='f3.TFrame')
        self.frame3.pack(fill='both', expand=True)
        
        self.master.config(menu=self.frame1.setMenu())
        
        self.pack(expand=True, fill='both')
        
               
    def onExit(self):
        self.quit()
        
    def onOpen(self, db_type):
        print('Open: ' + db_type)
        
    def onNew(self, db_type):
        print('New: ' + db_type)
         
         
def main():
    pass

if __name__ == '__main__':
    main()

