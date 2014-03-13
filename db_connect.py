#!/usr/bin/env python
# -*- coding: utf-8 -*-

db_type_list = []

#Test if sqlite3 module is present
try:
	import sqlite3 as sqlite
	from database_handler_sqlite import *
	db_type_list.append('sqlite')
	
except ImportError:
	#Going to show message to user later
	pass
		
#Test if MySQL module is present
try:
	import mysql.connect
	from database_handler_mysql import *
	db_type_list.append('mysql')
	
except ImportError:
	#Going to show message to user later
	pass

#Test if MsSQL module is pressent
try:
	import mssql
	from database_handler_mssql import *
	db_type_list.append('mssql')
	
except ImportError:
	#Going to show message to user later
	pass

class connection_handler(object):
	
	def __init__(self):
		self.db_type_list = db_type_list
		self.connected_db = []
	
	def connect(self, db_type, path):
		if db_type == 'sqlite':
			self.connect_sqlite(path)
		elif db_type == 'mysql':
			self.connect_mysql(path)
		elif db_type == 'mssql':
			self.connect_mssql(path)
			
	def connect_sqlite(self, path):
		self.connected_db.append(database_handler_sqlite(path))
		
	def connect_mysql(self, path):
		self.connected_db.append(database_handler_mysql(path))
		
	def connect_mssql(self, path): 
		self.connected_db.append(database_handler_mssql(path))
	
def main():
	
	return 0

if __name__ == '__main__':
	main()

