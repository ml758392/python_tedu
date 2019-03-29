# -*-coding:utf-8-*-
import sys

print(sys.stdin)
n = 0
for line in sys.stdin:
    n = n+1
    print(n, line, end="")
