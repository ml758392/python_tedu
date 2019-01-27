# -*-coding:utf-8-*-
def gensquares(N):
    for i in range(N):
        yield i ** 2


for item in gensquares(5):
    print(item)


# 不使用生成器函数，达成一致的结果
# def gensquares(N):
#     res = []
#     for i in range(N):
#         res.append(i**2)
#     return res
#
# for item in gensquares(5):
#     print(item)
