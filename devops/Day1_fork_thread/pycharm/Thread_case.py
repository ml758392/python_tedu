# -*-coding:utf-8-*-
import threading
import time
nums = [4, 2]


def loop(nloop, nsec):   # 定义函数，打印运行的起始时间
    print('start loop %d,at %s' % (nloop, time.ctime()))
    time.sleep(nsec)
    print("loop %d done at %s" % (nloop, time.ctime()))


def main():
    print('starting at:%s' % time.ctime())
    threads = []
    for i in range(2):      # 创建两个线程，放入列表
        t = threading.Thread(target=loop, args=(0, nums[i]))
        print(type(t))
        threads.append(t)

    for i in range(2):
        threads[i].start()  # 同时运行两个线程

    for i in range(2):
        threads[i].join()   # 主程序挂起，直到所有线程结束
    print('all Done at %s' % time.ctime())


if __name__ == '__main__':
    main()
