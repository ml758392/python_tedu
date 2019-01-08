# -*-coding:utf-8-*-
#  两个线程同时工作，一个存钱，一个取钱
import threading

# 锁对象
lock = threading.Lock()

num = 100


def run(n):
    global num
    for i in range(10000000):
        # 加锁
        # 确保了这段代码只能有一个线程从头到尾的完整执行
        # 阻止多先线程的并发执行，包含锁的某段代码世纪上只能以单线程模式执行，所以效率大大的降低了

        lock.acquire()
        try:
            num = num + n
            num = num - n
            # 修改完一定要释放锁
        finally:
            lock.release()

        # with lock:    自动解锁
        #     num = num + n
        #     num = num - n


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('num=', num)

    # num 的值发生了不可预知的改变
