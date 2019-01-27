# -*-coding:utf-8-*-
from __future__ import print_function
import time
import functools


def benckmark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res
    return wrapper


@benckmark
def add(a, b):
    """12344"""
    return a + b


print(add(1, 2))
print(add.__name__)
print(add.__doc__)



