# -*-coding:utf-8-*-
class Person(object):
    def __init__(self, age):
        # 属性直接对外暴露
        self.__age = age


    '''
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            age = 0
        self.__age = age
        print(self.__age)
    '''

    @property
    def age(self):
        return self.__age

    @age.setter  # 属性去掉下划线  .setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age


per = Person(-1)

# 属性直接对外暴露
# 不安全，没有数据的过滤
# print(per.name)
print(per.age)

per.age = 100   # 相当与调用set_age
print(per.age)  # 相当于调用get_age


# property: 可以让你对首限制访问的属性使用点语法
