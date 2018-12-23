# -*-coding:utf-8-*-
def foo(num):
    for a in range(1, num+1):
        for b in range(1, a+1):
            print("%dx%d=%d" % (b, a, a*b), end=" ")
        print("")


foo(6)
foo(8)
