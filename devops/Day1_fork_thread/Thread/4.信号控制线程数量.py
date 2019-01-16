# -*-coding:utf-8-*-
import threading
import time

sem = threading.Semaphore(2)    # 控制线程并发执行数量


def run():
    with sem:
        for i in range(4):
            print('%s----%s' % (threading.current_thread().name, i))
            time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()