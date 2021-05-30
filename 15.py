# 列表的嵌套
# 列表的一个元素是一个列表，就叫列表的嵌套

# 一个学校，3个办公室，8个老师，随机分配

import random

offices =[[],[],[]]

names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为：%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print('%s'%name,end='')
    print('\n')
    print('-' * 20)
