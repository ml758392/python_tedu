# -*-coding:utf-8-*-
import re


str3 = "sunck is a good man! sunck is nice man! sunck is a handsome man"
d = re.finditer(r'(sunck)', str3)
while True:
    try:
        l = next(d)
        print(d)
    except StopIteration as e:
        break
