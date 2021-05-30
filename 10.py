# 循环
# for循环---遍历

"""
for循环格式
for 临时变量 in 列表或字符串：
    满足循环条件时执行的代码
else：
    不满足循环条件时执行的代码
"""

name = 'wangmeng'
for a in name:
    print('----------------')
    print(a)

name =''
for a in name:
    print(a)
else:
    print('没有数据')

# break 退出循环执行后续代码，结束整个循环
name = 'wangmeng'
for a in name:
    print('----------------')
    if a == 'm':
        break
    print(a)

# continue 不执行循环中的这一次，回到条件判读语句。结束这一次循环，继续执行下一次循环。
name = 'wangmeng'
for a in name:
    print('----------------')
    if a == 'm':
        continue
    print(a)
# break continue只能在循环中使用，只对最近一层循环起作用
