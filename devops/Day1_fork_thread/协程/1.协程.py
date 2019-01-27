# -*-coding:utf-8-*-
"""
子程序（子函数）：
    在所有语言中都是层级调用，比如A调用B，在B执行的过程中又可以调用C,
    C执行完毕返回，B执行完毕返回，最后是A执行完毕，
    是通过栈实现的，一个线程就是一个执行一个子程序，子程序调用总是一个入口，
    一次返回，调用的顺序是明确的


def A():
    print('A---start')
    B()
    print('A---end')


def B():
    print('B---start')
    C()
    print('B---end')


def C():
    print('C---start')
    print('C---end')

A()
#################################################################


协程：
    看上去也是子程序，但是执行过程中，内部可中断，然后转而执行别的子程序
    不是函数调用，有点类似CPU中断。
    达到以上的这个结果
    但是A中是没有B的调用
    看起来A，B执行过程有点向线程，但是协程的特点在于是一个线程执行

    与线程相比，协程的执行效率较高，因为只有一个线程，也不存在同时写变量
    的冲突，在协程中共享资源不加锁


python对协程的支持是通过generator实现的


"""


# 协程的最简单风格，控制函数的阶段执行，节约线程或者进程的切换
# 返回值是一个生成器


def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30


# m = run()
# print(next(m))
# print(next(m))
# print(next(m))

for i in run():
    print(i)









