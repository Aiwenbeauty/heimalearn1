# 数据源类型转换

a = '100'
print(type(a))
b = int(a)
print(type(b))
c = float(a)
print(type(c))
d =str(c)
print(type(d))
e = complex(a)
print(type(e))

f = '王'
f1 = ord(f) # 只能转换一个字符
print(f1)

g = hex(b)  # 只能把整数转换为字符串，字符串是十六进制的数
print(g)
print(type(g))

h = oct(b) # 转换为八进制
print(h)
