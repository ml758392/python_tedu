# -*-coding:utf-8-*-
from multiprocessing import Process   # 跨平台的多进程库
from time import sleep


def run(str):
    print('%s 子进程启动' % str)
    sleep(3)
    print('%s 子进程结束' % str)


if __name__ == '__main__':
    print("父进程开始")
    p = Process(target=run, args=("”咔咔的“",))
    p.start()
    p.join()  # 等待子进程结束
    print("父进程结束")
