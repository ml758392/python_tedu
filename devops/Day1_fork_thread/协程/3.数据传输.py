# -*-coding:utf-8-*-


def run():
    # 空变量，存储的作用data 始终为空
    data = ''
    r = yield data
    print(1, r, data)
    r = yield data
    print(2, r, data)
    r = yield data
    print(3, r, data)
    r = yield data


m = run()
# 启动m
print(m.send(None))
print(m.send('a'))
print(m.send('b'))
print(m.send('c'))

