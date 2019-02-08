# -*-coding:utf-8-*-
import paramiko


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
    host = '192.168.142.51'
    password = 'Taren1'
    cmd = 'id root'
    rcmd(host, password=password, cmd=cmd)
