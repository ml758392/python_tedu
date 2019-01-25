# -*-coding:utf-8-*-
from SQLalchemy import Departments, Session, Employees

session = Session()

# query1 = session.query(Departments)  # 只是SQL语句
# print(query1)
# for dep in query1:  # 当取数据时，才会真正查询数据库
#     print(dep)      # 打印出部门类的每个实例  __str__
#     print('%s -> %s' % (dep.dep_id, dep.dep_name))


# query2 = session.query(Departments.dep_id, Departments.dep_name)
# print(query2)   # 只是SQL语句
# for dep in query2:  # 查询的结果是元组组成的列表
#     print(dep)
#
# for dep_id, dep_name in query2:
#     print('%s ---> %s' % (dep_id, dep_name))


# query3 = session.query(Departments.dep_name.label('部门'))    # 别名
# print(query3)
# for dep in query3:
#     print(dep, dep.部门)


# query4 = session.query(Departments).order_by(Departments.dep_id)[1:3]
# print(query4)   # 因为取切片了，所以query4不是query语句，而是一个对象
# for dep in query4:
#     print(dep)  # 不包含左边包含右边
#     print(dep.dep_id, dep.dep_name)
#     print()


# query6 = session.query(Departments).filter(Departments.dep_id == 3)
# print(query6)
# for dep in query6:
#     print(dep.dep_id, dep.dep_name)


# query7 = session.query(Departments).filter(Departments.dep_id >= 2)\
#     .filter(Departments.dep_id <= 4)
# print(query7)
# for dep in query7:
#     print(dep.dep_id, dep.dep_name)


# query8 = session.query(Departments)\
#     .filter(Departments.dep_name.in_(['人事部', '财务部']))
# for dep in query8:
#     print(dep.dep_id, dep.dep_name)


# query9 = session.query(Departments)\
#     .filter(~Departments.dep_name.in_(['人事部', '财务部']))\
#     .order_by(Departments.dep_id)
# for dep in query9:
#     print(dep.dep_id, dep.dep_name)


# and or 需要单独导入
# from sqlalchemy import and_, or_
#
# query10 = session.query(Departments).filter(and_(Departments.dep_id >= 2,
#                                                  Departments.dep_id <= 4))
# query11 = session.query(Departments).filter(or_(Departments.dep_id == 2,
#                                                 Departments.dep_id == 4))
#
# for dep in query10:
#     print(dep.dep_id, dep.dep_name)
# print('*'*50)
# for dep in query11:
#     print(dep.dep_id, dep.dep_name)


# query12 = session.query(Departments)
# print(query12)
# print('*'*50)
# print(query12.all())        # all返回全部数据
# print('*'*50)
# print((query12.first()))    # 返回第一条数据
# print('*'*50)
# query13 = session.query(Departments.dep_id, Departments.dep_name)\
#     .filter(Departments.dep_id > 4)
# print(query13.one())        # one必须只有一条记录，否则抛出异常
# print(query13.scalar())     # 只返回one的第一个记录


# 聚合函数
# query14 = session.query(Departments)
# print(query14.count())


# from SQLalchemy import Employees  # 导入表影射类
# zmg = Employees(
#     emp_id=20,
#     emp_name='赵明刚',
#     gender='男',
#     birth_date='1998-10-8',
#     phone='1335595589',
#     email='zmg@163.com',
#     dep_id=2
# )
#
# zjh = Employees(
#     emp_id=25,
#     emp_name='张佳豪',
#     gender='男',
#     birth_date='1996-6-18',
#     phone='1859898698',
#     email='zjh@qq.com',
#     dep_id=5
# )
#
# session.add_all([zmg, zjh])
# session.commit()


# # query括号中先写Employees.emp_name, join的括号就要写Departments
# # query括号中先写Departments.dep_name. join的括号中就要写Employees
# query15 = session.query(Employees.emp_name, Departments.dep_name).join(
#     Departments, Employees.dep_id == Departments.dep_id
# )
# print(query15.all())


#################################################################################
# 修改数据
# q1 = session.query(Departments).filter(Departments.dep_name == '人事部')
# dep = q1.one()
# print(dep)
# dep.dep_name = '人力资源部'
# session.commit()
# session.close()

# 删除数据
# q2 = session.query(Departments).filter(Departments.dep_name == '开发部')
# dep = q2.one()
# print(dep)
# session.delete(dep)
# session.commit()
# session.close()

