# -*-coding:utf-8-*-
import threading, time, queue, random


def product(id, q):
    while True:
        num  = random.randint(0, 10000)
        q.put(num)
        print('生产者%d生产了%d数据放入了队列' % (id, num))
        time.sleep(3)
    # 任务结束
    q.task_done()


def customer(id, q):
    while True:
        item = q.get()
        if not item:
            break
        print('消费者%d消费了%d数据' % (id, item))
        time.sleep(3)
    # 任务完成
    q.task_done()


if __name__ == '__main__':
    # 消息队列
    q = queue.Queue()

    # 启动生产者
    for i in range(4):
        threading.Thread(target=product, args=(i, q)).start()

    # 启动消费者
    for i in range(3):
        threading.Thread(target=customer, args=(i, q)).start()
