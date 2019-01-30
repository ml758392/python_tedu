# -*-coding:utf-8-*-


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed(self, animal):
        print('feed %s' % animal.name)
        animal.eat()

    def work(self):
        pass