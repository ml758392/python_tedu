# -*-coding:utf-8-*-
import threading


def run():
    print('sunck is a good man')


t = threading.Timer(5, run)
t.start()
t.join()

print('父线程结束')
