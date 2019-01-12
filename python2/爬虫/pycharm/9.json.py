# -*-coding:utf-8-*-
import json
path1 = r'/var/www/html/index.html'
# 读取本地json文件
with open(path1, 'rb') as f:
    data = json.load(f)
print(data)
print(type(data))

 
# 将字典保存位本地json文件
path2 = 'test.json'
dict1 = {'name': 'yy', 'age': 18, 'grade': 100}
with open(path2, 'w') as f:
    json.dump(dict1, f)
