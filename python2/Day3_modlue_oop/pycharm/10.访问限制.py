# -*-coding:utf-8-*-
# 如果要让内部属性不被外部直接访问，在属性前加两个下划线


class Private:
    def __init__(self, money):
        self.__money = money

    def read(self):
        print('my money is %s' % str(self.__money))

    # 通过内部的方法，取修改私有属性
    # 通过自定义的方法实现对私有属性的赋值与取值

    def add(self, add):
        self.__money += add
        print('赚了 %s,现在有 %s' % (str(add), str(self.__money)))

    def reduce(self, reduce):
        self.__money -= reduce
        print('花了 %s,现在有 %s' % (str(reduce), str(self.__money)))


private = Private(10000)
private.read()
# 不能直接访问__money是因为python解释器把__money变成了
# print(private.__money)    无法访问该属性
private.add(100)
private.read()

print(private.__dict__)
print(private.__dir__())
print(private._Private__money)  # 私有变量  _类名__属性名


# 在python3中 __money__ 属于特殊属性
# 在python3中 _xxx 变量，这样的实例变量外部是可以访问的
# 按照约定的规则，当我们看到这样的变量时，意思是‘虽然我可以被访问’，
# 但是请把我视为私有变量
# 不要直接访问

















