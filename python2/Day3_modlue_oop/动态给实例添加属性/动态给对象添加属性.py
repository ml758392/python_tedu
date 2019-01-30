# -*-coding:utf-8-*-


class Person(object):
    # 限制添加实例的属性
    __slots__ = ('name', 'age', 'speak')


per =Person()
# 动态添加属性，这体现了动态语言的特点（灵活）
per.name = 'Tom'

print(per.name)


# 动态添加方法

# def say(self):
#     print('my name is %s' % self.name)
#
# per.speak = say
# per.speak(per)

# 类似与偏函数
from types import MethodType


def say(self):
    print('my name is %s' % self.name)


per.speak = MethodType(say, per)
per.speak()


# 已经限制了属性
# per.weight= 70
# print(per.weight)
