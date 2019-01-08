# -*-coding:utf-8-*-
import os
import random
import time
from multiprocessing import Pool


def run(n):
    start = time.time()
    print("子进程%d启动----%s" % (n, os.getpid()))
    time.sleep(random.randint(1,3))
    end = time.time()
    print("子进程%d结束---%s,sleep%3fs" % (n, os.getpid(), end - start))


if __name__ == '__main__':
    print('父进程启动')
    pp = Pool(3)         # 创建进程池，默认和核心数一致个子进程数量
    for i in range(3):
        # 创建进程，放入进程池统一管理
        pp.apply_async(run, args=(i,))
    # 在调用join之前必须先调用close，调用close之后就不能再个在继续添加新的进程了
    pp.close()
    pp.join()
    print("父进程结束")
