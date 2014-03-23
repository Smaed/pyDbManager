#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

name = 'Sqlite 3'
options = {'login':False}

class database_handler_sqlite(object):
	
    def __init__(self, path):
		
 #       defValues = {'foreignkeys':0}                       #Set the intital values ex. Pragma foreign
        
        self.path = path
        self.db_type = 'sqlite'
        
    def connect(self):
        self.con = sqlite.connect(self.path)
        self.cur = self.con.cursor()
		
    def exec_sql(self):
        pass
        
    def update_tables():
        pass
	
def main():
	pass

if __name__ == '__main__':
	main()

