# -*- coding:utf-8 -*-

import sqlite3

def Create_DB(file, table):
	c_db = sqlite3.connect(file)
	cursor = c_db.cursor()
	cursor.execute(\
		'CREATE TABLE %s (username varchar(20) UNIQUE,password BLOB)'%table)

if __name__ == '__main__':
	Create_DB('test_01.db', "user_table")