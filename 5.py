# 判断语句

"""if语句判断格式
  if 要判断的条件：
    条件成立时，执行的语句
  """
age = input('请输入你的年龄')
name = input('请输入你的名字')
password = input('请输入你的密码')
age = int(age)

print('-----------if开始-----------')

if age>=18 and password=='12345':
    print('%s,你已经成年,\n欢迎登陆爱学习管理系统'%name)

print('-----------if结束-----------')



0
