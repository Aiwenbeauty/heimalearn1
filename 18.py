# 字典的常见操作

# 修改元素，通过key键值
info1 = {'name':'班长','id':100,'sex':'f','address':'复旦大学'}
# newId = input('请输入新的学号')
# info['id'] = int(newId)
# print('修改之后的id为%d:'%info['id'])

# 添加元素
# 1.访问不存在元素
info = {'name':'班长','sex':'f','address':'复旦大学'}
# # 当使用 变量名['键'] = 数据，访问一个元素，但是这个元素不存在时，就会新增这个元素
# print(' id为：%d'%info['id'])

# 2.添加新的元素
newId = 100
info['id'] = newId
print('添加之后的id为：%d'%info['id'])

# 删除元素：del,clear()
# 1. del删除指定元素
print('删除前，%s'%info['name'])
# del info['name']
# print('删除后，%s'%info['name'])

# 2. del删除整个字典
print('删除前，%s'%info)
# del info
# print('删除后，%s'%info)

# clear清空整个字典
print('清空前，%s'%info)
info.clear()
print('清空后，%s'%info)

