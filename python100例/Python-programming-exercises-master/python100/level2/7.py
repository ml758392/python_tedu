"""
题：
编写一个程序，它取2位数，X，Y作为输入，并生成一个二维数组。数组的第i行和第j列中的元素值应为i * j。
注意：i = 0,1 ..，X-1; J = 0,1，¡Y-1。
例
假设为程序提供以下输入：
3,5
然后，程序的输出应该是：
[[0,0,0,0,0]，[0,1,2,3,4]，[0,2,4,6,8]]
"""

x, y = input('input:').split(',')
multilsit = []

for i in range(int(x)+1):
    lis = [i*j for j in range(int(y)+1)]
    multilsit.append(lis)
print(multilsit)