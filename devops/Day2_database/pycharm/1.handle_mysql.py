# -*-coding:utf-8-*-
import pymysql


# 设置连接数据库的参数
con = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    db='nsd1806',
    passwd='Taren1',
    charset='utf8'
)

cursor = con.cursor()  # 创建游标，可以理解为指向某一位置的数据库指针
insert1 = 'insert into departments values(%s, %s)'
hr = (1, 'HR')
deps = [(2, '运维部'), (3, '开发部'), (4, '财务部')]
cursor.execute(insert1, hr)         # 插入单条记录
cursor.executemany(insert1, deps)   # 插入多行记录
con.commit()    # 增删改都要确认
cursor.close()  # 关闭游标
con.close()     # 关闭连接
