# -*-coding:utf-8-*-
import threading
import os


def run():
    print("子进程 pid=%s,ppid=%s" %(os.getpid(), os.getppid()))


if __name__ == '__main__':
    print("父进程 %s" % os.getpid())
    p = threading.Thread(target=run())
    p.start()
    print("xxoo")