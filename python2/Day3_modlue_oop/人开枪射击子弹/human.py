# -*-coding:utf-8-*-
from gun import Gun
import random


class Person:
    def __init__(self, count):
        self.gun = Gun(count)

    def fire(self):
        self.gun.shoot()
        print('%d环' % random.randint(0, 10))


