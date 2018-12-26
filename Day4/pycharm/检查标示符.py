# -*-coding:utf-8-*-
import string,keyword

start = string.ascii_letters+"_"
after = string.digits+start


def check():
    fag = input("输入标识符:")
    if keyword.iskeyword(fag):
        print("不能使用关键字作为标示符！")
    else:
        for i, j in enumerate(fag):
            if i == 0 and j not in start:
                print("第1个字符不合法")
            elif i != 0 and j not in after:
                    print("第%d个字符不合法" % (i+1))
    return fag





if __name__ == "__main__":
    check()
