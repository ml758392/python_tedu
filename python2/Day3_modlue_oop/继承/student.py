# -*-coding:utf-8-*-
from person import Person


class Student(Person):
    def __init__(self, name, age, grade):
        super(Student, self).__init__(name, age)
        self.grade = grade

    def test(self):
        print('%s考了 %d' % (self.name, self.grade))
        super().run()


