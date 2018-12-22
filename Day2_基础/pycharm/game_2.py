# -*-coding:utf-8-*-
import random
all_choice = ['剪刀', '石头', '布']
win = [['剪刀', '布'], ['石头', '剪刀'], ['布', '石头']]


num_player = 2
num_computer = 2
while num_player > 0 and num_computer > 0:
    computer = random.choice(all_choice)
    prompt = '''
    (0)剪刀
    (1)石头
    (2)布
    请出拳(0/1/2):'''
    player = int(input(prompt))
    player = all_choice[player]

    print("You choice:"+player)
    print("You choice:"+computer)
    if player == computer:
        print("平局")             # 先写平局的,代码执行效率高
    elif [player, computer] in win:
        print("You win!")
        num_player -= 1
    else:
        print("You lose")
        num_computer -= 1
else:
    if num_player == 0:
        print("你赢了")
    else:
        print("电脑赢了")
