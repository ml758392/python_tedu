#-*-coding:utf-8-*-
##剪刀石头布

import  random
print("你可以根据以下提供出拳：")
print("石头\n剪刀\n布")
print("和电脑一决胜负把！")

all_choice = ["剪刀","石头","布"]
computer   = random.choice(all_choice)
player     = input("你的出拳为：")

win  = [['石头','剪刀'],['布','石头'],['剪刀','布']]
lose = [['石头','布'],['布','剪刀'],['剪刀','石头']]
if [player,computer] in win:
    print("电脑出拳：",computer)
    print("你赢了!")
elif [player,computer] in lose:
    print("电脑出拳：",computer)
    print("你输了！")
else:
    print("平局")
