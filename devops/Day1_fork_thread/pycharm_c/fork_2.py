import os
print('hello world')

pid = os.fork()

if pid:				# 返回两个值父进程 返回值为子进程的PID
    print('父进程......')
else:
    print('子进程......')
    exit()
print('你好')


