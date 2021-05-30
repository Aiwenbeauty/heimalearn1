# 循环
#while循环

i = 0
while i<=5:
    print('i= %d,这是第%d次循环'%(i,i+1))
    i+=1


i =1
sum = 0
while i<=100:
    sum=sum+i
    i+=1
print('1~100的和为：%d'%sum)

i =1
sum =0
while i<=100:
    if i%2==0:
        sum=sum+i
    i+=1

print('1到100的偶数和为：%d'%sum)

# while嵌套循环

col = 1
while col<=5:
    print ('* '* col)
    col+=1


i = 1
while i<=5:

    j=1
    while j<=i:
        print("$ ",end='') # 不换行
        j+=1
    print('\n')
    i+=1


# 九九乘法表
i = 1
while i<=9:

    j=1
    while j<=i:
        print("%d * %d = %d\t"%(j,i,j*i),end='') #\t制表符，协助在垂直方向对齐
        j+=1
    print('\n')
    i+=1
