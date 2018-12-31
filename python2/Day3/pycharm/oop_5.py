# -*-coding:utf-8-*-
class A:
    def foo(self):
        print('你好！')


class B:
    def bar(self):
        print('How are you?')
    def pstar(self):
        print('@'*20)


class C(A, B):
    def pstar(self):
        print('*'*20)


if __name__ == '__main__':
    c = C()     # 子类的实例继承了所有父类的方法
    c.foo()     # 如果多个父类有同名的方法，查找顺序是从上向下，从左到右
    c.bar()     # 也就是先查子类，再查父类，父类按定义顺序从左到右查找
    c.pstar()   # 子类和父类有同名的方法先查子类
