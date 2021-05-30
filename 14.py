# 列表的相关操作

# 添加元素：append,extend,insert

# append 添加列表元素之后，列表名还是之前的，只是在之前列表最后一位加了一个元素
# li = ['wangmeng','siguangwen']
# print('-----添加之前列表中的数据-----')
# for name in li:
#     print(name)
#
# temp = input('请输入要添加的姓名：')
# li.append(temp)
#
# print('-----添加之后列表中的数据-----')
# for name in li:
#     print(name)

# extend 可以将一个列表（集合）中的元素逐一添加到列表中
# 注意extend 和 append的区别
a = [1,2]
b = [3,4]
a.extend(b)
print(a)

a = [5,6]
b = [7,8]
a.append(b)
print(a)

# insert,在指定位置插入元素
a = [0,1,2]
a.insert(1,3)  #(位置，元素）
print(a)

# 修改元素
#修改元素，要通过索引来确定修改哪个元素

a = ['xiaozhu','xiaoma','xiaogou']
print('------修改之前的元素------')
for name in a:
    print(name)

a[1] = 'xiaomao'

print('------修改之后的元素------')
for name in a:
    print(name)

# 查找元素：in,not in,index,count
# in / not in
# a = ['xiaozhu','xiaoma','xiaogou']
# findname = input('请输入要查找的姓名：')
#
# if findname in a:
#     print('在列表中找到了相同的名字')
# else:
#     print('没找到')

#index,count在列表中用法相同
a = ['xiaozhu','xiaoma','xiaogou']
b = a.index('xiaozhu',0,2) # 1,2 代表索引范围，区间是左闭右开的
print(b)  # 找到，返回索引
b = a.count('zhuzhu')
print(b)  # 找不到，返回0


# 删除元素：del,pop,remove
# del根据索引进行删除
# pop删除最后一个元素
# remove 根据元素的值进行修改

# del
movieName = ['罗小黑战记','奇巧计程车','一人之下','JOJO的奇妙冒险','鬼灭之刃','星辰变']
print('----------删除之前----------')
for name in movieName:
    print(name)

del movieName[2]
print('----------删除之后----------')
for name in movieName:
    print(name)

# pop
movieName = ['罗小黑战记','奇巧计程车','一人之下','JOJO的奇妙冒险','鬼灭之刃','星辰变']
print('----------删除之前----------')
for name in movieName:
    print(name)

movieName.pop()
print('----------删除之后----------')
for name in movieName:
    print(name)

# remove
movieName = ['罗小黑战记','奇巧计程车','一人之下','JOJO的奇妙冒险','鬼灭之刃','星辰变']
print('----------删除之前----------')
for name in movieName:
    print(name)

movieName.remove('鬼灭之刃')
print('----------删除之后----------')
for name in movieName:
    print(name)


# 排序：sort,reverse
# sort将列表按照特定的顺序进行排列，默认为由小到大,参数reverse=True，可改为由大到小
# reserve的方法，是将列表逆置,和大小无关，只是从后往前读入
print('------------sort正序-------------')
a = [1,5,3,2,5,4,7,6,3,8,0,9]
a.sort()
print(a)
print('------------sort逆序-------------')
a = [1,5,3,2,5,4,7,6,3,8,0,9]
a.sort(reverse=True)
print(a)
print('-------------reverse-----------')
a = [1,5,3,2,5,4,7,6,3,8,0,9]
a.reverse()
print(a)
