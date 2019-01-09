# -*-coding:utf-8-*-
class Vendor:
    def __init__(self, em, ph):
        self.email = em
        self.phone = ph


class BearToy:
    def __init__(self, name, size, color, em, ph):
        """实例化时，自动调用"""
        self.name = name  # 绑定属性self上，整个类中都可以引用
        self.size = size
        self.color = color
        self.vendor = Vendor(em, ph)

    def sing(self):
        print('I am %s,hello everyone...' % self.name)


if __name__ == '__main__':

    # 创建实例
    big = BearToy('熊大', 'Large', 'Brown', 'admin@tedu.cn', '4001001234')  # 将会调用 __init__ 方法，big传递到self
    second = BearToy('熊二', 'Middle', 'Brown', 'admin@tedu.cn', '4001001234')

    print(big.vendor.phone)

