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
        
        self.horizontal_canvas = ttk.Scrollbar(self, orient="horizontal")
        self.vertical_canvas = ttk.Scrollbar(self, orient="vertical")
        
        self.horizontal_canvas.pack(side='bottom', fill='x')
        self.vertical_canvas.pack(side='right', fill='y')
        
        self.noteBook = ttk.Notebook(self)
        self.noteBook.pack(side='top', fill='both', expand='yes')
        
        self.data=ttk.Frame(self.noteBook)
        self.data.pack(side='top', fill='both', expand='yes')
        
        self.edit=ttk.Frame(self.noteBook)
        self.edit.pack(side='top', fill='both', expand='yes')
        
        self.sql=ttk.Frame(self.noteBook)
        self.sql.pack(side='top', fill='both', expand='yes')
        
        self.noteBook.add(self.data, text='Data')
        self.noteBook.add(self.edit, text='Edit')
        self.noteBook.add(self.sql, text='SQL')
        
    
    def set_scrollbar(self):
        pass
        
    def update_data(self, *args, **kwargs):
        pass
        
    def update_edit(self, *args, **kwargs):
        pass
    
    def update_sql(self, *args, **kwargs):
        pass


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
        
        self.tree = ttk.Treeview(self, selectmode='browse')
        self.tree.pack(fill='y', expand=True, side='left')
        
        self.vsb = ttk.Scrollbar(self, orient="vertical", command = self.tree.yview)
        self.tree.config(yscrollcommand=self.vsb.set)
        
        self.vsb.pack(side='left', fill='both')
        
        self.initialValues()
    
    def initialValues(self):
        
        for db_type in db_connect.db_types:
            self.tree.insert('', 'end', db_type, text=db_type)
            
    def addDb(self, db_type, database):
        '''Work in progress for adding new entries to the treeview, 
            all new databases will be grouped under their type and all tables groups under the database '''
        
        self.tree.insert(db_type, 'end', database, text='')
        
        for table in database.tables:
            self.tree.insert(database, 'end', table, text=table)    


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
        
                       
    def onOpen(self, db_type):
        print('Open: ' + db_type)
        
    def onNew(self, db_type):
        print('New: ' + db_type)
        
    def onExit(self):
        self.quit()
         
         
def main():
    pass

if __name__ == '__main__':
    main()

