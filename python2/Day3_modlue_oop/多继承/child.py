# -*-coding:utf-8-*-
from father import  Father
from mother import Mother


class Child(Father, Mother):
    def __init__(self, money, facevalue):
        Father.__init__(self, money)
        Mother.__init__(self, facevalue)

    def study(self):
        print()


yy = Child(1000, 100)
print(yy.money, yy.facevalue)
yy.func()
