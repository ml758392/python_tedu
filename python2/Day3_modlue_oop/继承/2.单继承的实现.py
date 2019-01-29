# -*-coding:utf-8-*-
from student import Student

xiaoming = Student('xiaoming', 18, 150)
xiaoming.test()

print(dir(Student))
print(Student.__mro__)  # mro继承表
