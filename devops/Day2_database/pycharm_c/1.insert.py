# -*-coding:utf-8-*-
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='Taren1',
    db='yy'
)

cursor = conn.cursor()
insert = 'insert into yy(name,age) values(%s, %s)'
line1 = ('yy', 18)
line2_3 = (('bob', 30), ('li', 20))

cursor.execute(insert, line1)
cursor.executemany(insert, line2_3)
conn.commit()
cursor.close()
conn.close()
