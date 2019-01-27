# -*-coding:utf-8-*-
# 使用生成器


def fun1(l):
    for i in range(l):
        if i % 2 == 0:
            yield i


def main():
    for item in fun1(5):
        print(item)


if __name__ == '__main__':
    main()

# def fun1(l):
#     res = []
#     for i in range(l):
#         if i % 2 == 0:
#             res.append(i)
#     return res
#
#
#
# def main(l):
#     for iterm in fun1(l):
#         print(iterm)
#
#
# if __name__ == '__main__':
#     main(5)