# -*-coding:utf-8-*-
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    passwd='Taren1',
    db='pymysql'
)

cursor = db.cursor()
insert1 = 'insert into yy(name, age) values(%s,%s)'
data1 = ('yy', 1)
datalist1 = [('bob', 2), ('jack', 3)]
data2 = (1,'pp')

try:
    cursor.execute(insert1, data1)
    cursor.executemany(insert1, datalist)
    db.commit()
except:
    db.rollback()

try:
    cursor.execute(insert1, data2)
    db.commit()
except:
    db.rollback()

cursor.close()
db.close()
