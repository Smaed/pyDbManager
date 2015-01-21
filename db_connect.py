#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

db_types = {}

"""
Most of the code here is either temporary or very much unfinnished.
The plan is to read in all files from ./dbHandlers/database_handler_[a-z]+.py
and do the the imports in a loop. Generating a list of avilable databases 
useable (both module and hanlder present). The GUI will use that info to present
the available options.
"""

#Test if sqlite3 module is present
#try: 
#	import dbHandlers.database_handler_sqlite
#	db_types[dbHandlers.database_handler_sqlite.name] = dbHandlers.database_handler_sqlite
	
#except ImportError:
	#Going to show message to user later
#	print('no sqlite')
		
#Test if MySQL module is present

db_handlers = __import__('dbHandlers', fromlist = ['database_handler_mysql'])
print(db_handlers.database_handler_mysql.name)
print(dir(db_handlers))

db_types[db_handlers.name] = db_handlers
print(db_types['mysql'])

class DbConnect(object):
	
	_databases = []
	
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

