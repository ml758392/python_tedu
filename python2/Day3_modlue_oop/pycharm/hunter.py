# -*-coding:utf-8-*-
import random


class Hunter(object):
    def __init__(self, bullet_number):
        self.bullet_number = bullet_number

    def shoot(self):
        print('%s\nBong!' % ('#'*50))
        print(' %d 环!' % random.randint(0, 10))
        self.bullet_number -= 1
        print('剩余子弹数 %d' % self.bullet_number)


def main():
    hunter = Hunter(7)
    prompt = """现在你已经成为一名猎人！
        输入‘1’开枪
        输入其他离开
        输入你的选择:
        """
    while True:
        if hunter.bullet_number == 0:
            print('离开射击场!')
            break
        choice = input(prompt)
        if int(choice) == 1:
            hunter.shoot()
        else:
            print('离开射击场!')
            break


if __name__ == '__main__':
    main()
