# -*-coding:utf-8-*-
import os
import time

pid = os.fork()
if pid:
    print('parent....')
    time.sleep(60)
else:
    print('child....')
    time.sleep(15)