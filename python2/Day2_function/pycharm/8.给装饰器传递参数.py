# -*-coding:utf-8-*-
# 若装饰器本身也有参数，则需要再嵌套一层函数


def time(length=1):
    def bread(func):
        def wrapper(*args, **kwargs):
            for i in range(length):
                func(*args, **kwargs)
        return wrapper
    return bread


@time(5)
def sandwich(name):
    print(name)


sandwich('hello world')