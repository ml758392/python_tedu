# -*-coding:utf-8-*-
from bullet import BulletBox


class Gun:
    def __init__(self, count):
        self.bulletbox = BulletBox(count)

    def shoot(self):
        print('Bong')
        self.bulletbox.count -= 1
        print('子弹剩余%d' % self.bulletbox.count)