# -*-coding:utf-8-*-
"""
注意：以后千万不要将对象属性与类属性重名，因为对象属性会屏蔽类属性，
但是当删除对象属后，在使用又能使用类属性了
"""


class Person(object):
    # 这里的属性实际上属于类属性（用类名来调用）
    name = 'person'

    def __init__(self, name):
        self.name = name


print(Person.name)  # 类属性

yy = Person('yy')
print(yy.name)  # 对象属性 优先级高于类属性

print('*'*50)
print(Person.name)

print('*'*50)
yy.name = 'yyy'  # 对象属性改变 对其对象无效
del yy.name       # 删除对象属性，之后使用了类属性
print(yy.name)



