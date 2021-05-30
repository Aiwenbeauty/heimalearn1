# if嵌套

balance = input('请输入公交卡余额')
balance = float(balance)

# site = input('空位数')
# site = int(site)

if balance>=2:
    print('你可以上车')
    site = input('空位数')
    site = int(site)
    if site>0:
        print('你可以就坐')
    else:
        print('没有位置')
else:
    print('余额不足，你不能上车')
