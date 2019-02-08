# -*-coding:utf-8-*-
# /usr/bin/env python
import paramiko
import os
import sys
import threading


def remote_comm(host, password, comm):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='root', password=password)
    stdin, stdout, stderr = ssh.exec_command(comm)
    out = stdout.read().decode()
    err = stderr.read().decode()
    if out:
        print("[%s:out]: %s" % (host, out))
    if err:
        print("[%s:Error]: %s" % (host, err))
    ssh.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Uage: %s ipfile password 'comm'" % sys.argv[0])
        sys.exit(1)
    ipfile = sys.argv[1]
    if not os.path.isfile(ipfile):
        print("No such file:%s" % ipfile)
    password = sys.argv[2]
    comm = sys.argv[3]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=remote_comm, args=(ip, password, comm))
            t.start()










