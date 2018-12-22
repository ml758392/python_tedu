#-*-coding:utf-8-*-

'''
1.系统要求生成100以内的数字
2.最多猜5次，猜对结束程序
3.如果5次全部猜错，则输出正确结果
'''


import random       ##导入随机数模块
num = random.randint(1,100)
counter = 1
while counter <= 5:
    answer = int(input("请输入1～100的数字："))
    if answer>num:
        print("猜大了")
    elif answer<num:
        print("猜小了")
    else:
        print("猜对了")
        break
    counter += 1
else:
    print("随机数为:",num)
