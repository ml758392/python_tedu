import subprocess
import threading
import time


def ping(host):
    rc = subprocess.call('ping -c2 %s &> /dev/null' % host, shell=True)
    if rc == 0:
        print('\033[32;1m%s:up\033[0m' % host)
    else:
        print('\033[31;1m%s:down\033[0m' % host)


def main():
    t1 = time.time()
    threads = []
    ips = ['192.168.142.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=ping, args=(ip,))
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
    t2 = time.time()
    print('Done spend %f' % (t2 -t1))


if __name__ == '__main__':
    main()
