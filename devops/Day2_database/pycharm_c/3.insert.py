# -*-coding:utf-8-*-
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='Taren1',
    db='yy',
)

cursor = conn.cursor()
insert1 = 'insert into  yy(name,age) values(%s, %s)'
data1 = ('pp', 20)
cursor.execute(insert1, data1)
conn.commit()

query1 = 'select * from yy'
cursor.execute(query1)
cursor.scroll(3, mode='absolute')
result = cursor.fetchall()
print(result)
cursor.close()
conn.close()