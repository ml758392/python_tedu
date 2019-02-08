import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # 回答yes
ssh.connect('192.168.142.51', username='root', password='Taren1')
a = ssh.exec_command('id root;id bob')
print(a[1].read().decode())    # 正确输出
print(a[2].read().decode())    # 错误输出
ssh.close()

# 执行命令后的返回值有三项， 分别是输入，输出和错误的类文件对象。执行完命令后名关心的是输出和错误

