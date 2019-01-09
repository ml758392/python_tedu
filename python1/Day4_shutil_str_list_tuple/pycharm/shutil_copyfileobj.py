# -*-coding:utf-8-*-
import shutil

with open('/etc/hosts', 'rb') as a:
    with open('/mnt/copyfileobj', 'wb') as b:
        shutil.copyfileobj(a, b)


# 无元数据

# [root@lenovo 5_张志刚]# ll /etc/hosts
# -rw-r--r--. 1 root root 195 12月 15 17:05 /etc/hosts
# [root@lenovo 5_张志刚]# ll /mnt/copyfileobj
# -rw-r--r-- 1 root root 195 12月 25 09:23 /mnt/copyfileobj
