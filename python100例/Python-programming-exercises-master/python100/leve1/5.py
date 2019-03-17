"""
定义一个至少包含两种方法的类：
getString：从控制台输入中获取字符串
printString：以大写形式打印字符串。
还请包括简单的测试函数来测试类方法。

提示：
使用__init__方法构造一些​​参数
"""


class IuputOutString(object):
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input('input:')

    def printString(self):
        print(self.s.upper())


A = IuputOutString()
A.getString()
A.printString()
