# -*-coding:utf-8-*-
import time

print('#' * 20, end='')
n = 0

while True:
    print('\r%s@%s' % ('#' * n, '#' * (19 - n)), end='')    #\r 覆盖原来的字符
    n += 1
    if n== 20:
        n = 0
    time.sleep(0.4)