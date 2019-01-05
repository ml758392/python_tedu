# -*-coding:utf-8-*-
import os
print("hello world")

pid = os.fork()
if pid:
    print('父进程.......')
else:
    print('子进程.......')
print('你好')