# -*-coding:utf-8-*-
from random import choice
num = int(input("请输入密码的位数:"))
string = "123456absimport!#@%"
password = ""
for i in range(num):
    password = password + choice(string)
else:
    print(password)
