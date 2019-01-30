# -*-coding:utf-8-*-
from animal import  Animal


class Mouse(Animal):
    def __init__(self, name):
        super(Mouse, self).__init__(name)