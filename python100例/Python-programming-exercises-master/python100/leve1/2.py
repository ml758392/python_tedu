# -*-coding:utf-8-*-
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


prompt= 'input number：'
x = int(input(prompt))
print(fact(x))
