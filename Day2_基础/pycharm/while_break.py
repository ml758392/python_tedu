#-*-coding:utf-8-*-
##输出1～100之间的整数
#当数字在大于30时退出
num = 1
while num<=100:
    print(num,end=" ")
    num += 1
    if num>30:
        break

##break 退出循环