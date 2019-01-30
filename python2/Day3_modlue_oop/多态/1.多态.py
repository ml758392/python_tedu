# -*-coding:utf-8-*-
"""
多态： 一种事物的多种形态

最终目标：人可以为任何一种动物

"""

from cat import Cat
from person import Person


tom = Cat('Tom')
yy = Person('yy', 18)
yy.feed(tom)
