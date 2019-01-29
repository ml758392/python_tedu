# -*-coding:utf-8-*-
class Person(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    def run(self):
        print('running')

    def get_mon(self):
        print(self.__money)

    def set_mon(self, money):
        self.__money = money
        print('set money to %s' % str(self.__money))
