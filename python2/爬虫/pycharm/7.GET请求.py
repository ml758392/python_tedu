# -*-coding:utf-8-*-
import urllib.request
import json

url = 'http://127.0.0.1/'
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')
print(data)

jsondata = json.loads(data)
print(jsondata["name"])