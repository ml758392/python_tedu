# -*-coding:utf-8-*-
from multiprocessing import Process   # 跨平台的多进程库
from time import sleep
import os


def run1(num):
    while True:
        print("子进程%d \n pid is %s" % (num, os.getpid()))
        print("ppid is %s" % os.getppid())
        sleep(1)


def run2():
    while True:
        print("process_2 is running")
        sleep(1)


if __name__ == '__main__':
    print("父进程执行,pid是 %s" %(os.getpid()))
    p = Process(target=run1, args=(1,))
    p.start()

    run2()
