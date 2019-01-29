# -*-coding:utf-8-*-
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myself(self):
        print("I'm %s , %s years old " % (self.name, self.age))

    """当对象时释放是执行 __del
        1.程序退出
        2.手动释放
        3.函数
    """
    def __del__(self):
        print('对象 %s 已经释放' % self)


person1 = Person('yy', 18)
person1.myself()

del person1     # 1.手动释放对象执行 __del__函数


def person():
    person2 = Person('pp', 20)
    person2.myself()


person()        # 2.函数执行完毕，对象自动释放


# 3.程序退出，执行__del__函数
person3 = Person('bob', 30)
person3.myself()