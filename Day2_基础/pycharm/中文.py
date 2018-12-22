# -*- coding:utf-8 -*-
print("中文环境")
print(5+5)

'''
三引号表示注释 
'''
print(0b1111)
print("九九乘法表")
for a in range(1, 10):
    for b in range(1, a+1):
        print("{1}x{0}={2}".format(a, b, a*b), end=" ")
    print("")
