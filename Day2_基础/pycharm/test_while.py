#-*-coding:utf-8-*-
#1.打印1～20
num = 1
while num<=20:
    print(num,end=" ")
    num += 1

#换行
print("")
#2.打印1～20的奇数
num = 1
while  num<=20:
    if num%2 != 0:
        print(num,end=" ")
    num += 1