# -*-coding:utf-8-*-
from urllib import request


url = r'http://127.0.0.1/'
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KH'
                  'TML, like Gecko)\
                    Chrome / 60.0.3112.113 Safari / 537.36'
}

req = request.Request(url, headers=header)
html = request.urlopen(req)
data = html.read()
print(data.decode('utf8'))