# -*-coding:utf-8-*-
class BearToy:
    def __init__(self, name, size, color):
        self.name = name  # 绑定属性self上，整个类中都可以引用
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s,hello everyone...' % self.name)


class NewBearToy(BearToy):  # 新类是BearToy的子类
    def run(self):
        print("我能跑了!")


if __name__ == '__main__':

    # 创建实例
    big = NewBearToy('倒霉熊', 'Large', 'Brown')

    big.sing()
    big.run()
    print(big.name)