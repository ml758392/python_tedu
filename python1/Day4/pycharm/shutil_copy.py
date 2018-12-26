# -*-coding:utf-8-*-
import shutil

shutil.copy('/etc/hosts','/mnt/')

# shutil.copy  无元数据
# src 为文件 dst可以是目录

# [root@lenovo 5_张志刚]# ll /mnt/hosts
# -rw-r--r-- 1 root root 195 12月 25 09:28 /mnt/hosts
# [root@lenovo 5_张志刚]# ll /etc/hosts
# -rw-r--r--. 1 root root 195 12月 15 17:05 /etc/hosts
