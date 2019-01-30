# -*-coding:utf-8-*-
class Person(object):
    def __init__(self, num):
        self.num = num

    # 运算赋重载
    def __add__(self, other):
        return Person(self.num+other.num)

    def __str__(self):
        return 'num =' + str(self.num)


per1 = Person(1)
per2 = Person(2)

# 对象相会执行 __add__ 方法,返回一个对象，print对象 __str__方法
print(per1 + per2)