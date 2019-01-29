# -*-coding:utf-8-*-
class Person(object):
    def class_name(self):
        print(self.__class__)


person = Person()
person.class_name()     # 类名
