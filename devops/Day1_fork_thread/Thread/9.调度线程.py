# -*-coding:utf-8-*-
import threading
import time


# 线程条件变量
cond = threading.Condition()


def thread1():
    for i in range(10):
        if i % 2 ==0:
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.wait()
            cond.notify()


def thread2():
    for i in range(10):
        if i % 2 != 0:
            print(threading.current_thread().name, i)
            time.sleep(1)
            cond.notify()
            cond.wait()


if __name__ == '__main__':
    threading.Thread(target=thread1).start()
    threading.Thread(target=thread2).start()
