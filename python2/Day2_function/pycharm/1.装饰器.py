# -*-coding:utf-8-*-
def func1():
    print('sunck is a good man')


def func2(arg):
    def inner():
        arg()
        print('*'*50)
    return inner


f =func2(func1)

f()

