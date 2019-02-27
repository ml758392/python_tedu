# -*-coding:utf-8-*-
import requests

param = {'wd': 'python'}
r = requests.get('http://www.baidu.com/s', params=param)
with open('/root/桌面/5_张志刚/devops/Day4/pycharm/python.html', 'wb') as fobj:
    fobj.write(r.content)
