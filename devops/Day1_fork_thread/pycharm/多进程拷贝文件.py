# -*-coding:utf-8-*-
import os
import time
from multiprocessing import Pool


def copyfile(sfile, dfile):
    with open(sfile, 'rb') as s:
        with open(dfile, 'wb') as d:
            d.write(s.read())


def main(n):
    start = time.time()
    pp = Pool(n)
    spath = '/root/桌面/5_张志刚/devops/Day1_fork_thread/pycharm'
    dpath = '/root/桌面/5_张志刚/devops/Day1_fork_thread/py_copy'
    for filename in os.listdir(spath):
        pp.apply_async(copyfile, args=(os.path.join(spath, filename), os.path.join(dpath, filename)))

    pp.close()
    pp.join()
    end = time.time()
    print('总耗时 %0.5f' % (end - start))


if __name__ == '__main__':
    main(2)











