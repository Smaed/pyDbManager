#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
from dbFile import dbFile

name = 'Sqlite 3'

class database_handler_sqlite(dbFile):

    def __init__(self, path):
        dbFile.__init__(self, path)
        self.path = path
        self.db_type = 'sqlite'
        
    def connect(self):
        self.con = sqlite.connect(self.path)
        self.cur = self.con.cursor()

    def exec_sql(self):
        pass
        
    def update_tables(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()

