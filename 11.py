# 字符串

# 下标、索引

name ='wangmeng'

print(name[0])
print(name[1])
print(name[5])

# 切片
"""
切片语法
[起始：结束：步长]
注意：选取区间是左闭右开，即起始位开始到结束位前一位
"""

name ='wangmeng'

print(name[2:6:1]) #连续取
print(name[2:6])
print(name[2:])  # 取2到最后的字符，包括最后一个字符
print(name[2:-1])  # 取2到最后的字符，去掉最后一个字符
print(name[2:-2])
print(name[:5])  #取0到4
print(name[::2]) #两个里面取一个，间隔为1
