# -*-coding:utf-8-*-
import subprocess

# shell=False
a = subprocess.call(['ls', '-l'], stdin=None, stdout=None, shell=False)
print(a)
#
# # shell=True
# a = subprocess.call('ls -l', stdin=None, stdout=None, shell=True)
#
#
# ############################################
# # check_call
# subprocess.check_call(['ls', '-l'])
# # 退出状态非1 抛出异常
# # subprocess.check_call('exit 1', shell=True)
#
#
# ################################################
# # check_output
