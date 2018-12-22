#-*-coding:utf-8-*-
import  random
print("和电脑一决胜负吧！")
print("1.石头\n2.剪刀\n3.布")

dic = {1:'石头',2:'剪刀',3:'布'}
player = int(input("请输入相应的数字出拳："))
computer = random.randint(1,3)

win =  [[1,2],[2,3],[3,1]]
lose = [[1,3],[2,1],[3,2]]

print("你的出拳为："+dic[player])
print("电脑出拳为："+dic[computer])
if [player,computer] in win:
    print("你赢了")
elif [player,computer] in lose:
    print("你输了")
else:
    print("平局")
