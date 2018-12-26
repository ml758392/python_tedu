#-*-coding:utf-8-*-
#!/usr/bin/env python3
user = input("username:")
pwd = input("password:")
if user == "yy":
    if pwd == "123456":
        print("Login successful")
    else:
        print("Password inorrect")
else:
    print("login inorrect")
