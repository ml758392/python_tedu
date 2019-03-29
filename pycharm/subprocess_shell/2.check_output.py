# -*-coding:utf-8-*-
import subprocess

try:
    output = subprocess.check_output(['df', '-fgg']).decode('utf8')
except subprocess.CalledProcessError as e:
    ourput = e.output
    print(e.returncode)
else:
    lines = output.split('\n')
    for line in lines[1:-1]:
        if line:
            print(line.split()[-2])

# output = subprocess.check_output(['ls', 'pp', '/etc/passwd'], stderr=subprocess.STDOUT)
# print(output.decode())
