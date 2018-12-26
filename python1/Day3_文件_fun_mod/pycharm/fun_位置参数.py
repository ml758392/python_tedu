# -*-coding:utf-8-*-
import sys


def copy_files():
    with open(sys.argv[1], "rb") as a:
        while True:
            data = a.read(4096)
            if not data:
                break
    with open(sys.argv[2], "wb") as b:
        b.write(data)


copy_files()
