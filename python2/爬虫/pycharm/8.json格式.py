# -*-coding:utf-8-*-
import json

#  将json字符串转换成python字符串
jsonstr = '{"name":"yy","age":18,"grade":100}'
jsondata = json.loads(jsonstr)
print(jsondata)
print(type(jsondata))

print('*'*50)
# 将python字典转换成json字符串
dict = dict(name="yy", age=18, grade=100)
jsonstr = json.dumps(dict)
print(jsonstr)
print(type(jsonstr))

