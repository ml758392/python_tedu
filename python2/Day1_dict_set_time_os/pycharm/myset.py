# -*-coding:utf-8-*-
with open("passwd1") as obj1:
    aset = set(obj1)

with open("passwd2") as obj2:
    bset = set(obj2)

with open('difference',"w") as obj:
    obj.writelines(bset - aset)
