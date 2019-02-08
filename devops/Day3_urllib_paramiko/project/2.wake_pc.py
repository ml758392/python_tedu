"""
网络唤醒所有的主机
"""
# -*-coding:utf-8-*-
# !/usr/bin/env python
import threading
import os
import sys


def wake_pc(iface, mac):
    os.system('ether-wake -i %s %s' % (iface, mac))


def main():
    if len(sys.argv) != 3:
        print('Uage:%s iface macfile' % sys.argv[0])
        sys.exit(1)
    iface = sys.argv[1]
    mac_file = sys.argv[2]
    with open(mac_file) as fobj:
        for line in fobj:
            mac = line.strip()
            t = threading.Thread(target=wake_pc, args=(iface, mac))
            t.start()


if __name__ == '__main__':
    sys.exit(main())



