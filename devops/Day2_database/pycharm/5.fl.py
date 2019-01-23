# -*-coding:utf-8-*-
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='Taren1',
    db='nsd1806',
    charset='utf8'
)

cursor = conn.cursor()
update1 = 'update departments set dep_name="HR" where dep_name="人力资源部"'
# data = ('人力资源部', 'HR')
cursor.execute(update1)
conn.commit()
cursor.close()
conn.close()

