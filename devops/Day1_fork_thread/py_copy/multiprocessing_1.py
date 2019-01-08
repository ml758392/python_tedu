# -*-coding:utf-8-*-
from multiprocessing import Process   # 跨平台的多进程库
from time import sleep


def run1(num):
    while True:
        print("process_%d is running" % num)
        sleep(1)


def run2():
    while True:
        print("process_2 is running")
        sleep(1)


if __name__ == '__main__':
    print("父进程执行")
    p = Process(target=run1, args=(7,))
    p.start()

    run2()
