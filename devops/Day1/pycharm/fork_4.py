# -*-coding:utf-8-*-
import os
for i in range(3):
    pid = os.fork()
    if not pid:
        print('hello world')
        exit()
print('Done')