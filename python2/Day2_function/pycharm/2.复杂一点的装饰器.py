# -*-coding:utf-8-*-
def say(age):
    print('yy is %s age old' % age)


def fun(arg):
    def inner(age):
        if age > 0:
            arg(age)
        else:
            print('ValueError')
    return inner


say = fun(say)

say(-3)
say(10)


