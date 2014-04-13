#!/usr/bin/env python
# -*- coding: utf-8 -*-

db_types = {}

"""
Most of the code here is either temporary or very much unfinnished.
The plan is to read in all files from ./dbHandlers/database_handler_[a-z]+.py
and do the the imports in a loop. Generating a list of avilable databases 
useable (both module and hanlder present). The GUI will use that info to present
the available options.
"""

#Test if sqlite3 module is present
try: 
	from dbHandlers import database_handler_sqlite
	db_types[database_handler_sqlite.name] = database_handler_sqlite
	
except ImportError:
	#Going to show message to user later
	print('no sqlite')
		
#Test if MySQL module is present
try:
	from dbHandlers import database_handler_mysql
	db_types[database_handler_mysql.name] = database_handler_mysql
	
except ImportError:
	#Going to show message to user later
	print ('no mySQL')

#Test if MsSQL module is pressent
try:
	from dbHandlers import database_handler_mssql
	db_types[database_handler_mssql.name] = database_handler_mssql
	
except ImportError:
	#Going to show message to user later
	print('no ms sql')

print(db_types['Sqlite 3'])

class DbConnect(object):
	
	def __init__(self):
		self.connected_db = []
	
	def addDb(self, db_type):
		
		if db_type.options['login']:
			pass
			
		else:
			pass
	
	def removeDB(self):
		pass

def main():
	
	return 0

if __name__ == '__main__':
	main()

