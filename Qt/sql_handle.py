# -*- coding :utf-8 -*-
import sqlite3
import os, sys
sys.path.append("..")
from pcfg import codec

# import creat_db


class User(object):
    """user's infomation"""
    def __init__(self, username, password):
        # super(User, self).__init__()
        self.username = username
        self.password = password
# 设置用户名
    def set_username(self,username):
        self.username = username
# 获取用户名
    def get_username(self):
        return username
# 设置密码
    def set_password(self,password):
        self.password = password
# 获取密码
    def get_password(self):
        return password


class SqlHandle(object):
    """一个处理数据库的类"""
    filename = 'user_data.db'	#请设置默认数据库名
    table_name = ''
    cursor = ''
    pw_db = ''
    key = ''
    def __init__(self, table_name = '', key = ''):
        # super(SqlHandler, self).__init__()
        self.pw_db = sqlite3.connect(self.filename)
        self.table_name = table_name
        self.key = key
        self.pcfg = codec.PcfgEncode(self.key)

# 创建表
    def create_tb(self, registname):
        self.table_name = registname 
        self.cursor = self.pw_db.cursor()
        self.cursor.execute(\
            'CREATE TABLE if not exists %s (username varchar(20), password BLOB, remarks varchar(120))'%self.table_name)
        self.cursor.close()

# 查找
    def query(self, username):
        self.cursor = self.pw_db.cursor()
        self.table_name = username
        # 检查当前表是否存在
        try:
        	self.cursor.execute('SELECT * FROM %s WHERE username = ?' %self.table_name, \
            	 (username,))
        	temp = self.cursor.fetchall() 
        	# print(temp)
        	de_temp = [(name,self.pcfg.pcfg_decode(x.split(b'  ')),remark) for (name,x,remark) in temp]

        except sqlite3.OperationalError as ope:
        	print("have no sqlite!")
        	de_temp = []
        	self.cursor.close()
        	self.pw_db.commit()

        return de_temp

# 插入	
    def insert(self, username, password, remarks):
        self.cursor = self.pw_db.cursor() 
        print("in the insert ,the password is " + password)
        en_password_list = self.pcfg.pcfg_encode(password)
        print(en_password_list)
        if not en_password_list:
        	print("can not encode ,please change the key")
        	return
        # 这里使用特殊的做法：把数据流用'  '作为分隔符，合并到一个二进制串中

        encode_password = b'  '.join(en_password_list)
        self.cursor.execute(\
            'INSERT INTO %s (username, password, remarks) VALUES (?, ?, ?) ' %self.table_name,\
            (username, encode_password, remarks))
        self.cursor.close()
        self.pw_db.commit()

# 删除
    def delete(self, username):
        self.cursor = self.pw_db.cursor()
        try:
        	self.cursor.execute(\
            	'DELETE FROM %s WHERE username = ?' %self.table_name,\
            	(username,))
        except sqlite3.OperationalError as ope:
        	print("the username %s is not existed!"%username)

        self.cursor.close()
        self.pw_db.commit()

# 关闭文件
    def close(self):
        self.pw_db.close()
        

if __name__ == '__main__':
	test = 	SqlHandle('user_data.db')
	test.insert('caicai','123456')
	print(test.query('caicai'))
	test.close()
#额  记录一下错误没关系吧
##python在用sqlite3时一定要及得提交事务在即
    # cursor.close()
    # coon.commit()
    # coon.close()	