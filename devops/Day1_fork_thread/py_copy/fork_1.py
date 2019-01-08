# -*-coding:utf-8-*-
import os

print("父进程开始 %s" % os.getpid())
p = os.fork()
if p == 0:
    print("子进程开始 %s" % os.getpid())
    print("父进程 %s" % os.getppid())
    exit()
print("ooxx")
