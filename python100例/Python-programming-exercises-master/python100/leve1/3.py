# -*-coding:utf-8-*-
prompt = 'input number:'
x = int(input(prompt))
d = dict()
for i in range(1, x+1):
    d[i] = i*i
print(d)