# -*-coding:utf-8-*-
import threading
import time
import subprocess

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        rc = subprocess.call('ping -c2 %s &> /dev/null' % self.host)
        if rc == 0:
            print('\033[32;1m%s:up\033[0m' % self.host)
        else:
            print('\033[31;1m%s:down\033[0m' % self.host)


def main():
    threads = []
    ips = ['192.168.142.%s' % i for i in range(1, 255)]
    start = time.time()
    for ip in ips:
        t = threading.Thread(target=Ping(ip))
        t.start()
        threads.append(t)
    for i in threads:
        i.join()
    end = time.time()
    print(end - start)
        

if __name__ == '__main__':
    main()

