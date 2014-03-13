#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mssql

name = 'mssql'

class database_handler_mssql(object):
	
	def __init__(self, path):
		self.path = path
		self.db_type = 'mssql'
		
	def database_handler_connect(self):
		self.con = sqlite.connect(self.path)
		self.cur = con.cursor()
		
	def exec_sql(self):
		pass
	
	def update_tables(self):
		pass
	
def main():
	pass

if __name__ == '__main__':
	main()

