# -*-coding:utf-8-*-
import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    passwd='Taren1',
    db='pymysql'
)

cursor = db.cursor()
create1 = '''create table yy(
ID int(1) primary key auto_increment,
name varchar(20) not null,
age int(1) not null default 18); 
'''

cursor.execute(create1)
db.commit()
cursor.close()
db.close()
