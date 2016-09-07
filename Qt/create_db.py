# -*- coding:utf-8 -*-

import sqlite3

def Create_TB(file, table):
	c_db = sqlite3.connect(file)
	cursor = c_db.cursor()
	cursor.execute(\
		'CREATE TABLE if not exists %s (username varchar(20), password BLOB, remarks varchar(120))'%table)
	# 用户名，密码，备注

