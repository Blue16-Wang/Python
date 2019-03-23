number=99
running=True
while running:
    guess=int(input('输入一个数字：'))
    if guess==number:
        print('恭喜你答对了')
        running=False
    elif guess<number:
        print('这个数字要大一些')
    else:
        print("这个数字要小一些")
else:
    print('循环停止')
