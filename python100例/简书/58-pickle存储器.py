# -*-coding:utf-8-*-
import pickle

"""以前的文件写入，只能写入字符串，如果希望把任意数据对象（数字，列表等）
写入文件，取出来的时候数据类型补编，就能用pickle了"""

shop_list = ["eggs", "apple", "peach"]
with open('58-pickle存储器.txt', 'wb') as fobj:
    pickle.dump(shop_list, fobj)

with open('58-pickle存储器.txt', 'rb') as fobj:
    mylist = pickle.load(fobj)

print(mylist)
