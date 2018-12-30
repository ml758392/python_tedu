# -*-coding:utf-8-*-
x = 0
def func():
    global x
    x += 1
    print(x)
    func()

func()