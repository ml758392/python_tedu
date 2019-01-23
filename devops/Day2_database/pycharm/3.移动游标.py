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
cursor.scroll(1, mode='absolute')   # 绝对移动
result = cursor.fetchone()
print(result)

cursor.scroll(2, mode='relative')   # 默认就是相对移动
result = cursor.fetchone()
print(result)

cursor.close()
con.close()
