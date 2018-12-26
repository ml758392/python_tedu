# -*-coding:utf-8-*-
#!/usr/bin/env python3
import os


def get_fname():
    name = input("输入文件的完整路径:")
    if os.path.exists(name):
        print("%s已经存在" % name)
        get_fname()
    return name

def get_content():
    content = []
    print("输入数据，输入end退出")
    while True:
        data = input('>')
        if data == "end":
            break
        content.append(data)
    return content

def wfile(fname,content):
    content = ['%s\n' % line for line in content]
    with open(fname, "w") as f:
        f.writelines(content)


if __name__ == "__main__":
    fname = get_fname()
    content = get_content()
    wfile(fname, content)

