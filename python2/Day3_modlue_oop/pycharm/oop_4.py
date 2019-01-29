# -*-coding:utf-8-*-
class BearToy:
    def __init__(self, name, size, color):
        self.name = name  # 绑定属性self上，整个类中都可以引用
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s,hello everyone...' % self.name)


class NewBearToy(BearToy):  # 新类是BearToy的子类
    def __init__(self, name, size, color, date):
        """ 父子类有同名方法，子类对象执行子类方法 """

        # BearToy.__init__(self, name, size, date)
        super(NewBearToy, self).__init__(name, size, color)

    def run(self):
        print("我能跑了!")


if __name__ == '__main__':

    # 创建实例
    big = NewBearToy('倒霉熊', 'Large', 'Brown', '2018-10-22')

    big.sing()
    big.run()
