# -*-coding:utf-8-*-
import threading
import time

def oo():
    event = threading.Event()
    def run():
        for i in range(5):
            # 阻塞， 等待时间的触发
            event.wait()
            # 重置
            event.clear()
            print('sunck is a good man')
    threading.Thread(target=run).start()
    return event


event =oo()

for i in range(5):
    time.sleep(2)
    event.set()