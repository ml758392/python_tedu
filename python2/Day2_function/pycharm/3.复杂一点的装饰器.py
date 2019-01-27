# -*-coding:utf-8-*-
def bread(f):
    def inner(*args, **kwargs):
        print('start')
        f()
        for x, y in kwargs.items():
            print('%s--%s' % (x, y))
        print('end')
    return inner


@bread
def say_hello():
    print('hello')


dict1 = {'name': 'yy', 'age': 18}
say_hello(**dict1)
