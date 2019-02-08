# -*-coding:utf-8-*-
import paramiko
import sys
import getpass
import os
import threading


def rcmd(host, username='root', password=None, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read().decode()
    err = stderr.read().decode()
    if out:
        print('[%s] OUT:\n%s' % (host, out))
    if err:
        print('[%s] EROOR:\n%s' % (host, err))
    ssh.close()


if __name__ == '__main__':
    ipfile = sys.argv[1]
    if not os.path.isfile(ipfile):
        print('no such file')
        eixt(2)
    cmd = sys.argv[2]
    password = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            host = line.strip()
            threading.Thread(target=rcmd, args=(host, 'root', password, cmd)).start()
            # cmd(host, password=password, cmd=cmd)
