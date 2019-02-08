# -*-coding:utf-8-*-
# !/usr/bin/env python
import sys
import threading
import paramiko
import os


def mput(host, password, src, dst):
    base_name = os.path.basename(src)
    dst_name = os.path.join(dst, base_name)
    scp = paramiko.Transport(host)
    scp.connect(username='root', password=password)
    sftp = paramiko.SFTPClient.from_transport(scp)
    sftp.put(src, dest_name)
    sftp.close()
    scp.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Uage: %s ipfile password localfile remotefile' % sys.argv[0])
        sys.exit(1)
    ipfile = sys.argv[1]
    if not os.path.isfile(ipfile):
        print("No such file:%s" % ipfile)
        sys.exit(2)
    password = sys.argv[2]
    lfile = sys.argv[3]
    rfile = sys.argv[4]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=mput, args=(ip, passwrod, lfile, rfile))
            t.start()




