# -*-coding:utf-8-*-
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:Taren1@localhost/sqlalchemy',
                       encoding='utf8')

Base = declarative_base()
Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = 'student'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    age = Column(Integer, default=19)

    def __str__(self):
        return '名字:%s' % self.name


class Grade(Base):
    __tablename__ = 'grade'
    g_id = Column(Integer, primary_key=True)
    s_id = Column(Integer, ForeignKey('student.ID'))
    grade = Column(Integer, nullable=False)
    time = Column(TIMESTAMP)

    def __str__(self):
        return '成绩:%s' % self.grade


if __name__ == '__main__':
    Base.metadata.create_all(engine)