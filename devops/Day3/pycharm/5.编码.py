# -*-coding:utf-8-*-
import webbrowser
from urllib import request


url = 'http://www.baidu.com/s?wd=你好'
encode_url = request.quote(url)
print(encode_url)

request.quote('你好')
url = 'http//www.baidu.com/s?wd=' + request.quote('你好')
webbrowser.open_new_tab(url)