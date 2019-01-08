# -*-coding:utf-8-*-
import threading
import time


def run(num):
    print('子线程%s开始' % (threading.current_thread().name))

    # 实现线程的功能
    time.sleep(2)
    print('打印')
    time.sleep(2)
    print('子线程%s结束' % (threading.current_thread().name))
    print(num)


if __name__ == '__main__':
    # 任何进程默认就会启动一个线程，称作为主线程，主线程可以启动新的子线程
    # current_thread(): 返回当先线程的实例
    print('主线程%s启动' % (threading.current_thread().name))

    # 创建子线程                     线程的名称
    t = threading.Thread(target=run, name='runThread', args=(1,))
    t.start()
    t.join()
    print('主线程%s结束' % (threading.current_thread().name))
