# 猜拳游戏

import random
player = input('请输入:剪刀（0），石头（1），布（2）')
player = int(player)
if player<0 or player>2 or type(player)!=int:
    print('您的输入不符合要求，请按要求输入')
else:
    computer = random.randint(0,2)#返回0，2之间的任一整数，包括0，2
    if ((player==1) and (computer==0)) or ((player==0) and (computer==2)) or ((player==2) and (computer==1)):
        print('你出%d，电脑出%d。你赢了'%(player,computer))
    elif player==computer:
        print('你出%d，电脑出%d。平局'%(player,computer))
    else:
        print('你出%d，电脑出%d。你输了'%(player,computer))
