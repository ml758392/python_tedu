# -*-coding:utf-8-*-
import urllib.request
import random

url = 'http://www.baidu.com'

UA = [
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) Apple\
    WebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb\
    Kit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
]

agent = random.choice(UA)
req = urllib.request.Request(url)
# 向请求体中添加了user-agent
req.add_header('User-Agent', agent)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

