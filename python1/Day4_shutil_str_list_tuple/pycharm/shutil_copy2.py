# -*-coding:utf-8-*-
import shutil

shutil.copy2('/etc/hosts', '/mnt/copy2')

# 保留元数据

# [root@lenovo 5_张志刚]# ll /etc/hosts
# -rw-r--r--. 1 root root 195 12月 15 17:05 /etc/hosts
# [root@lenovo 5_张志刚]# ll /mnt/copy2
# -rw-r--r--. 1 root root 195 12月 15 17:05 /mnt/copy2
