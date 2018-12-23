# 打印十个斐波那契数
def fib(num):
    fibs = [0, 1]
    for i in range(num-2):
        fibs.append(fibs[-2]+fibs[-1])
    else:
        print(fibs)


fib(10)
fib(15)
