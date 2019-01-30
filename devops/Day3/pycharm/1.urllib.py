# -*-coding:utf-8-*-
from urllib import request


html = request.urlopen('http://www.163.com/')

with open('163.html', 'wb') as fobj:
    while True:
        data = html.read(1024)
        if not data:
            break
        fobj.write(data)



