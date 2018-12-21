#-*-coding:utf-8-*-
#!/usr/bin/env python3
username = "yy"
password = 123456
a = input("请输入用户名:")
b = input("情输入密码:")
if a == username and int(b) == password:
    print("登陆成功！")
else:
    print("\n用户名或密码错误！\n登录失败！")
