import subprocess
import os
import time


def ping(host):
    rc = subprocess.call('ping -c2 %s &> /dev/null' % host, shell=True)
    if rc == 0:
        print('\033[32;1m%s:up\033[0m' % host)
    else:
        print('\033[31;1m%s:down\033[0m' % host)


def main():
    t1 = time.time()
    ips = ['192.168.142.%s' % i for i in range(1,255)]
    for ip in ips:
        pid = os.fork()
        if not pid:
            ping(ip)
            exit()		# exit() 子进程不执行下面的代码

    for i in range(1, 255):	# os.waitpid()一次只能处理一个僵尸进程
        os.waitpid(-1,0)
    t2 = time.time()
    print(t2 -t1)


if __name__ == '__main__':
    main()

