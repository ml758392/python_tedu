# -*-coding:utf-8-*-
class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print('%s is running' % self.name)

    def eat(self):
        print('%s is eating' % self.name)

