# -*- coding :utf-8 -*-

import sqlite3

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
	filename = ''
	cursor = ''
	pw_db = ''
	def __init__(self, filename):
		# super(SqlHandler, self).__init__()
		self.pw_db = sqlite3.connect(filename)

# 查找
	def query(self,username):
		self.cursor = self.pw_db.cursor()
		self.cursor.execute('SELECT * FROM user_table WHERE username = ?', \
			(username,))
		temp = self.cursor.fetchall() 
		return temp

# 插入	
	def insert(self,username,password):
		self.cursor = self.pw_db.cursor()
		self.cursor.execute(\
			'INSERT INTO user_table (username,password) VALUES (?,?) ',\
			(username,password))
		self.cursor.close()
		self.pw_db.commit()

# 删除
	def delete(self,username):
		self.cursor = self.pw_db.cursor()
		self.cursor.execute(\
			'DELETE FROM user_table WHERE username = ?',\
			(username,))

# 关闭文件
	def close(self):
		self.pw_db.close()

		
# if __name__ == '__main__':
# 	test = 	SqlHandler('user_data.db')
# 	test.insert('caicai','123456')
# 	print(test.query('caicai'))
# 	test.close()


#额  记录一下错误没关系吧
##python在用sqlite3时一定要及得提交事务在即
	# cursor.close()
	# coon.commit()
	# coon.close()	