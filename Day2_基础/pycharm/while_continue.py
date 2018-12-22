#-*-coding:utf-8-*-
##输出1～20之间所有的偶数
##要就跳过所有奇数

num = 0
while num<=20:
    num += 1
    if num%2 == 1:
        continue
    print(num,end=" ")

