# 字符串常见操作

# find,检测try是否包含在mystr中，如果是，返回开始的索引值，否则返回-1
mystr = 'we need to try our best to get try our the job'

a = mystr.find('try',0,len(mystr))
print(a)

# rfind,从右边开始查找,仍然返回第一个字母的索引
b = mystr.rfind('try')
print(b)

# index,也是检查字符串是否包含在其中，不同之处是如果不包含，会报异常
b = mystr.index('our',0,25)
print(b)
# c = mystr.index('ijn')
# print(c)

b = mystr.rindex('our')
print(b)
# count,计算try,从0，到len(mystr),在muystr中出现的次数
d = mystr.count('try',0,len(mystr))
print(d)

# replace,把str1替换成str2,如果count指定，则替换次数不超过count
# mystr.replace(str1,str2,mystr.count(str1))
say = 'hello world hahaha'
e = say.replace('ha','he',2)
print(e)

# split,以str为分隔符，切片mystr,如果maxsplit有指定，则仅分隔maxsplit个子字符串,后面不变
mystr = 'we need to try our best to get the job'
f = mystr.split(' ',2)
print(f)
f =mystr.split(' ')
print(f)

# captialize,把字符串第一个字符大写
g = mystr.capitalize()
print(g)

# title,把字符串每个单词的首字母大写
h = mystr.title()
print(h)

# startswith,检查字符串是否以obj开头，是返回true,否则返回false
a = mystr.startswith("we")
b = mystr.startswith('haha')
print(a)
print(b)

# endswith,检查字符串是否以obj结束
a = mystr.endswith('job')
b = mystr.endswith('haha')

print(a)
print(b)

# lower,把mystr中所有大写字母变成小写
mystr = 'As you Can see'
a = mystr.lower()
print(a)

# upper,把 mystr中的小写字母变成大写字母
b = mystr.upper()
print(b)

# ljust,返回原字符串，左对齐,并用空格填充至width
a = mystr.ljust(50)
print(a)

#rjust,右对齐
b = mystr.rjust(50)
print(b)

# center, 居中
c = mystr.center(50)
print(c)

# lstrip,删除左边空白字符
d = b.lstrip()
print(d)

# rstrip,删除末尾空白字符
# strip,删除两端空白字符


# partition,把mystr以str分割成三部分
a = mystr.partition('you')
print(a)
# rpartition是从右边开始找

# splitlines,按照行分隔，返回有一个包含每一行作为元素的列表
mystr = 'wangmeng\nfighting\ndonot\nafraid'
print(mystr)
a = mystr.splitlines()
print(a)

# isalpha,判断字符串里所有元素是否都为字母，如果是返回true,注意空格也不是字母
a = mystr.isalpha()
print(a)

# isdigit,判断字符串是否都为数字
mystr = '12345'
a = mystr.isdigit()
print(a)

# isalnum,判断是否都为数字或字母
mystr = '123abc'
a = mystr.isalnum()
print(a)

# isspace,判断是否只包含空格
mystr = '   '
b = mystr.isspace()
print(b)

# join,在每个字符后面插入str
li = ["my",'name','is','wang','meng']
str1 = " "
str2 = '--'
a = str1.join(li)
b = str2.join(li)
print(a)
print(b)

# split,
testStr = 'haha nihao a \t heihei \t woshi nide \t hao \n pengyou'
print(testStr)
a = testStr.split()
print(a)
