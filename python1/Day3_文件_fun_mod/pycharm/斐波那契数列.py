# -*-coding:utf-8-*-

# 打印十个斐波那契数
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2]+fibs[-1])
else:
    print(fibs)

######################
a = 0
b = 1
print(a, b, end=" ")
for i in range(8):
    c = a+b
    print(c, end=" ")
    a = b
    b = c

#########################
print()
def fibs(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibs(n-1) + fibs(n-2)    # 要用return全剧变量 不用else

print(fibs(4))