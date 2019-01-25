# -*-coding:utf-8-*-
import pymysql


db = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Taren1',
    port=3306,
    db='pymysql'
)

cursor = db.cursor()
query1 = 'select * from yy;'
cursor.execute(query1)
cursor.scroll(1, mode='absolute')
result = cursor.fetchone()
print(result)
result = cursor.fetchall()
print(result)
cursor.close()
db.close()
