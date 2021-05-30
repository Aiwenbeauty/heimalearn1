# 字典常见操作2

# 1. len()测量字典中键值对的个数
info = {'name':'班长','id':100,'sex':'f','address':'复旦大学'}
print(len(info))

# 2. keys返回一个包含字典所有键key的列表
a = info.keys()
print(a)

# 3. values返回一个包含字典所有值value的列表
b = info.values()
print(b)

# 4. items返回一个包含所有（键，值）元组的列表
c = info.items()
print(c)

# 5. has_key，dict.has_key(key)如果key在字典中，返回True,否则返回False
d = dict.has_key()
# print(d)
#
