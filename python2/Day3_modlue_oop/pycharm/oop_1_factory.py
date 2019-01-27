# -*-coding:utf-8-*-
class BearToy:
    def __init__(self, name, size, color):
        """实例化时，自动调用"""
        self.name = name  # 绑定属性self上，整个类中都可以引用
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s,hello everyone...' % self.name)


if __name__ == '__main__':

    # 创建实例
    big = BearToy('熊大', 'Large', 'Brown')  # 将会调用 __init__ 方法，big传递到self
    second = BearToy('熊二', 'Middle', 'Brown')
    print(dir(big))
    print(big.size)
    print(big.color)
    big.sing()
    second.sing()

