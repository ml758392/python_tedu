# -*-coding:utf-8-*-
import subprocess


def execute_cmd(cmd):
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    p.wait()
    if p.returncode == 0:
        print(p.stdout.read().decode())
    else:
        print(p.stdout.read().decode())


if __name__ == '__main__':
    execute_cmd("whoami")


