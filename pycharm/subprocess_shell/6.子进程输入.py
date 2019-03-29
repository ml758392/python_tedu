# -*-coding:utf-8-*-
import subprocess

child1 = subprocess.Popen(["cat", "/etc/passwd"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["grep", "0:0"], stdin=child1.stdout, stdout=subprocess.PIPE)
child2_out = child2.communicate()
print(child2_out[0].decode())
