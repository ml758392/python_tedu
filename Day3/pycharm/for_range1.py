# -*-coding:utf-8-*-

# 打印1～20之间的奇数

# case1
for i in range(1, 21):
    if i%2 == 1:
        print(i, end=" ")
else:
    print()


# case2
for i in range(1, 21, 2):
    print(i, end=" ")
