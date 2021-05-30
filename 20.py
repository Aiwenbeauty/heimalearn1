# 遍历 for……in……

# 1. 字符串遍历
a_str = 'hello siguangwen'
for char in a_str:
    print(char,end=' ')

# 2. 列表遍历
a_list = [1,2,3,4,5,6]
for num in a_list:
    print(num,end=' ')

# 3. 元组遍历
a_turple = ('a',1,2,'好的',4,5,3)
for x in a_turple:
    print(x,end=' ')

# 4. 字典遍历
# 4.1 字典遍历key键
dict = {'name':'司广文','sex':'male','hight':'175cm'}
for key in dict.keys():
    print(key)

# 4.2 字典遍历value值
for value in dict.values():
    print(value)

# 4.3 字典遍历item项
for item in dict.items():
    print(item)

# 4.4 遍历字典key-value键值对
for key,value in dict.items():
    print('key=%s,value=%s'%(key,value))

# 5. 带下标索引遍历
chars = ['a','b','c','d','e']
i = 0
for char in chars:
    print(i,char)
    i+=1

# enumerate()
for i,char in enumerate(chars):
    print(i,char)

