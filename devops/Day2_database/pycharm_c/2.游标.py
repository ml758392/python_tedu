# -*-coding:utf-8-*-
import pymysql


conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    port=3306,
    passwd='Taren1',
    db='yy',
    charset='utf8'
)

cursor = conn.cursor()
query1 = 'select * from yy'
cursor.execute(query1)
cursor.scroll(1, mode='absolute')
result = cursor.fetchone()
print(result)


cursor.close()
conn.close()