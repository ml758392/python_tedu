# -*-coding:utf-8-*-
# /usr/bin/env python
import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n')
obj.stdin.write('print 2 \n')
obj.stdin.write('print 3 \n')
obj.stdin.write('print 4 \n')
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print cmd_out
print cmd_error