# -*-coding:utf-8-*-


def product(c):
    c.send(None)
    for i in range(5):
        print('生产者产生数据%d' % i)
        r = c.send(str(i))
        print('消费者消费了数据%s' % r)
        print()
    c.close()


def customer():
    data = ''
    while True:
        n = yield data
        print('我消费了%s' % n)
        data = n


c = customer()
product(c)

