# -*-coding:utf-8-*-
"""
重写：可将函数重写定义一遍

__str__()

__repr__()

"""


class Person(object):
    """
    :param
    :parameter
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myself(self):
        print("I'm %s , %s years old " % (self.name, self.age))

    # __str__()在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法
    def __str__(self):
        return 'person'

    # __repr__():给机器用的，再python解释起里面直接敲对象名在回车后调用的方法
    def __repr__(self):
        return 'ppp'


person1 = Person('yy', 18)
print(person1.__dict__)
print(person1.__class__)
print(person1.__doc__)
print(person1.__dir__())
print(person1.__repr__())

print(person1)
