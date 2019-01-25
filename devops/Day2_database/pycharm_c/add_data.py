# -*-coding:utf-8-*-
from  sqlalchemy1 import Student, Session

session = Session()

xiaoming = Student(
    ID=1,
    name='xiaoming',
    age=17
)

xiaohong = Student(
    ID=2,
    name='xiaohong',
    age=17
)

lilei = Student(name='lilei', age=19)

session.add(xiaoming)
session.add_all((xiaohong, lilei))
session.commit()
session.close()