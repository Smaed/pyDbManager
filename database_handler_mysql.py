#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

class database_handler_sqlite(object):
	
	def __init__(self, path):
		self.path = path
		self.type = 'mysql'
		
	def database_handler_connect(self):
		self.con = sqlite.connect(self.path)
		self.cur = con.cursor()
		
	def database_handler_exec_sql(self):
		pass
	
	def database_handler_update_tables():
		pass
	
def main():
	pass

if __name__ == '__main__':
	main()

