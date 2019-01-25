# -*-coding:utf-8-*-
from alchemy import Departments, Session

session = Session()

hr = Departments(dep_id=1, dep_name='人事部')
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
devops = Departments(dep_id=4, dep_name='DEVOPS')
finance = Departments(dep_id=5, dep_name='财务部')
deps = [ops, dev, devops, finance]
session.add(hr)
session.add_all(deps)
session.commit()
session.close()


# dep_dev =Departments(dep_name='yy')   # 创建实例时，并不会真正在表中添加记录
# print(dep_dev.dep_name)
# print(str(dep_dev.dep_id))
