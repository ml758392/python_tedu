# -*-coding:utf-8-*-
import pymysql

con = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='Taren1',
    db='nsd1806',
    charset='utf8'
)

cursor = con.cursor()
query1 = 'select * from departments order by dep_id'
cursor.execute(query1)
result = cursor.fetchone()
print(result)
print('-'*50)

result = cursor.fetchmany(2)
print(result)
print('-'*50)

result = cursor.fetchall()
print(result)

cursor.close()
con.close()
