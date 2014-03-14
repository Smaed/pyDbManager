#!/usr/bin/env python
# -*- coding: utf-8 -*-

db_type_list = []

"""
Most of the code here is either temporary or very much unfinnished.
The plan is to read in all files from ./dbHandlers/database_handler_[a-z]+.py
and do the the imports in a loop. Generating a list of avilable databases 
useable (both module and hanlder present). The GUI will use that info to present
the available options.
"""

#Test if sqlite3 module is present
try: 
	import database_handler_sqlite
	db_type_list.append(database_handler_sqlite.name)
	
except ImportError:
	#Going to show message to user later
	pass
		
#Test if MySQL module is present
try:
	import database_handler_mysql
	db_type_list.append(database_handler_mysql.name)
	
except ImportError:
	#Going to show message to user later
	pass

#Test if MsSQL module is pressent
try:
	import database_handler_mssql
	db_type_list.append(database_handler_mssql.name)
	
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
			
#	def connect_sqlite(self, path):
#		self.connected_db.append(database_handler_sqlite(path))
#		
#	def connect_mysql(self, path):
#		self.connected_db.append(database_handler_mysql(path))
#		
#		self.connected_db.append(database_handler_mssql(path))
	
def main():
	
	return 0

if __name__ == '__main__':
	main()

