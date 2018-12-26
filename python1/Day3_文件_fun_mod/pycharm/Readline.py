# -*-coding:utf-8-*-
a = open('test.txt')
print(a.readline(2))    # 1字节
print(a.readline())     # 当前指针到行末
print(a.readlines(1))   # 1行
print(a.readlines())    # 当前指针到末行
a.close()
