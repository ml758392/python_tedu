# -*-coding:utf-8-*-
from person import Person


class Worker(Person):
    def __init__(self, name, age, money):
        super(Worker, self).__init__(name, age, money)

    def work(self):
        # 继承父类中的私有属性
        # print(self.__money)
        print(A._Person__money)  # 私有属性的名仍为父类的名


A = Worker('bob', 30, 10000)
A.work()
A.get_mon()     # 使用方法获取父类的私有属性


