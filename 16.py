# 元组tuple
# 元组与列表类似，不同是元组的元素不能修改，元组使用小括号，列表使用中括号

# 访问元组
tuple = ('hello',100,3.14)
print(tuple[0])
print(tuple[1])
print(tuple[2])

# 修改元素
# python中元组不能修改元素，包括不能删除元素

# 元组内置函数：count,index,与列表中用法相同
a = ('A','你好','pytouch',100,5.20)
b = a.index('pytouch',1,3)    # 查找元素，左闭右开
print(b)  # 返回位置
c = a.count(100)
print(c)  #返回数量
