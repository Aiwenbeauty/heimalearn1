# if-else

length = input('输入刀子长度')
length = int(length)

if length<=10:
    print('允许上车')
else:
    print('刀子太长了，不能上车')

# elif

a = input('请输入一个数字')
a = int(a)
if 0<=a<=10:
    print('吃火锅')
elif 10<a<=100:
    print('吃烤肉')
else:
    print('吃自助')
