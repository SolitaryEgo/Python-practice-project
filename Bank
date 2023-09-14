money = 50000000
name = input("输入姓名：")
flag = True
while flag:
    i = int(input("余额:\t1\n存款:\t2\n取款:\t3\n主菜单:\t4\n"))
    #查询余额
    if i == 1:
        print(f"你好{name},当前余额为{money}")
        continue
    #存款操作
    elif i == 2:
        save = int(input("输入存款数："))
        money += save
        print(f"你好{name},当前余额为{money}")
        continue
    #取款操作
    elif i == 3:
        draw = int(input("输入取款数："))
        money -= draw
        print(f"你好{name},当前余额为{money}")
        continue
    #回到主菜单
    elif i == 4:
        main = i
        print(i)
        continue
    #输入其他直接结束程序
    else:
        flag = False
