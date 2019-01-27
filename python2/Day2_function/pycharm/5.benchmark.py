# -*-coding:utf-8-*-
from __future__ import print_function
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res
    return wrapper


@benchmark
def add(a, b):
    time.sleep(1)
    return a + b


print(add(1, 2))

# 续
# 使用装饰器之后函数属性的变化


def mul(a, b):
    """ 123445"""
    return a + b


@benchmark
def addd(a, b):         # __doc__ 和 __name__ 属性是装饰器中
    """54321"""         # 嵌套函数的信息
    return a * b


print(mul.__name__)
print(mul.__doc__)
print('*'*50)
print(addd.__name__)
print(addd.__doc__)
