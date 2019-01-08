# -*-coding:utf-8-*-
from multiprocessing import Process
from time import sleep

num = 100


def run():
    print("子进程开始")
    global num
    print("子进程结束 %d" % (num + 1))


if __name__ == '__main__':
    print("父进程开始")
    p = Process(target=run)
    print(type(p))
    p.start()
    print("父进程结束 %d" % num)
# 在父子进程中发生变化的变量不能共享
