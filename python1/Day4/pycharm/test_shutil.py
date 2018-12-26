# -*-coding:utf-8-*-
import shutil  # 提供对文件的复制和移动操作、

# -------- 复制文件的五种方法

# copyfileobj(fsrc,fdst)接受文件对象
# fsrc需要读权限 fdst需要写权限
shutil.copyfileobj(open('/etc/passwd', 'rb'), open('/mnt/passwd1', 'wb'))

# copyfile(src,dst)只需写入源文件路径和目标文件路径()字符串
# 复制源文件到目标文件
shutil.copyfile('/etc/passwd', '/mnt/passwd2')

# copy(src,dst)复制src到dst
# src必须为文件，dst可以是文件或目录如果dst为目录，将文件复制到目录中
shutil.copy('/etc/shadow', '/mnt')

# copy2(src.dst)
# copy2会尝试复制源文件的元数据(权限，最后修改时间，最后访问时间...)
# 可以从文件复制到目录
shutil.copy2('hello.py','/mnt')

#############################################################

# ---------- 移动文件或者目录

# move(src,dst)将src移动到dst
# src可以是文件或者目录 dst是一个目录
shutil.copyfile('/etc/passwd', '/opt/move.txt')
shutil.move('/opt/move.txt', '/mnt/move.txt')


##############################################################

# ------------复制目录

# copytree(src,dst)递归的复制src目录到dst目录
# dst目录不能是一个已存在的目录
shutil.copytree('/etc/yum.repos.d', '/mnt/repos.d/')

# rmtree(path) 删除目录 不能删除文件
shutil.rmtree('/mnt/repos.d')


##################################################################

# ---------------权限管理

# copymode(src,dst)将src的权限复制给dst
# 只复制权限，不会复制内容
shutil.copymode('/etc/shadow', '/mnt/passwd')

# copystat(src,dst) 复制元数据（权限位，最后访问时间，上次修改时间）
shutil.copystat('/etc/shadow', '/mnt/passwd')


# chown(path,user=None,group=None) 更改给定的路径的所有这用户和/或组
shutil.chown('/mnt/shadow', user='yy', group='yy')
