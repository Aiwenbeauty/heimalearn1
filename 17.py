# 字典 info
info = {'name':'班长','id':100,'sex':'f','address':'复旦大学'}
"""
1. 字典和列表一样也可以储存多个数据
2. 列表中找到某个元素是通过索引，字典中找到某个元素是通过’名字‘（就是冒号前面那个值）
3. 字典中的每个元素是由两部分组成，键：值。
"""
print(info['name'])
print(info['address'])
# 若访问的键不存在，报错
# 如果不确定字典中是否存在某个键值，可以使用get的方法，还可以设置默认值

age = info.get('age')
print(age)  # None,说明不存在
b = type(age)
print(b)  #NoneType

age = info.get('age',18)
print(age)   # 不存在，返回默认值
