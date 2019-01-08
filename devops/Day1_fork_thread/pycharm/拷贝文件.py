# -*-coding:utf-8-*-
import os
import time


def copyfile(sfile, dfile):
    with open(sfile, 'rb') as s:
        with open(dfile, 'wb') as d:
            d.write(s.read())


spath = '/root/桌面/5_张志刚/devops/Day1_fork_thread/pycharm'
dpath = '/root/桌面/5_张志刚/devops/Day1_fork_thread/py_copy'

start = time.time()
for filename in os.listdir(spath):
    copyfile(os.path.join(spath, filename),
             os.path.join(dpath, filename))
end = time.time()
print('总耗时 %0.5f' % (end - start))
