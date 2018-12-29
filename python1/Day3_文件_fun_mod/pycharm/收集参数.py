# -*-coding:utf-8-*-

def func(*args):
     print("hello 大家好,我在自我介绍以下：")
     print(type(args))
     for item in args:
         print(item)

func("liuying", 18, "北京大通州区", "wangxiaojing", "single")