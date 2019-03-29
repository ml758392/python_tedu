# -*-coding:utf-8-*-
import subprocess

child1 = subprocess.Popen('sleep 60', shell=True, stdout=subprocess.PIPE)
child2 = subprocess.Popen('sleep 60', shell=True, stdout=subprocess.PIPE)
print(child1.poll())
print(child2.poll())

child2.kill()
print(child2.poll())

# child.send.signal()
child1.terminate()

