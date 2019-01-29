# -*-coding:utf-8-*-
class Father(object):
    def __init__(self, money):
        self.money = money

    def work(self):
        print(self.money)

    def func(self):
        print('father')