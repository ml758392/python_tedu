# -*-coding:utf-8-*-
import shutil

shutil.copyfile('/etc/hosts', '/mnt/copyfile')

# 无元数据
# src dst 只能是文件

# [root@lenovo 5_张志刚]# ll /etc/hosts
# -rw-r--r--. 1 root root 195 12月 15 17:05 /etc/hosts
# [root@lenovo 5_张志刚]# ll /mnt/copyfile
# -rw-r--r-- 1 root root 195 12月 25 09:21 /mnt/copyfile
