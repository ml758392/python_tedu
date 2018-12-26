# -*-coding:utf-8-*-


def f():
    content = []
    b = 0
    print("输入内容，回车换行，输入end结束。")；
    while True:
        b += 1
        a = input("line%d:" % b)
        if a == "end":
            break
        content.append(a)
    print('+{}+'.format('*'*48))
    for i in content:
        print('+{: ^48}+'.format(i))
    print('+{}+'.format('*'*48))


if __name__ == "__main__":
    f()



