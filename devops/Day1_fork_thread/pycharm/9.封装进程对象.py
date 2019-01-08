# -*-coding:utf-8-*-
from sunckProcess import SunckProcess

if __name__ == '__main__':
    print('父进程启动')

    # 创建子进程
    p = SunckProcess('test')
    # 自动调用p进程对象的run方法 必须是run
    p.start()
    p.join()
    print('父进程结束')