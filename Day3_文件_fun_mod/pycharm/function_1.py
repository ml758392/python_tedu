# -*-coding:utf-8-*-
def foo():
    print('hello world')


foo()
print(foo)  # 直接输出函数名，查找函数对象
print(foo())#默认返回None
#######################################


def foo():
    res = 3 + 4
    return res  # return返回 res


print(foo())
print(foo() * 2)
