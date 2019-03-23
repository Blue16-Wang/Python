number=20
guess=int(input('输入一个数字：'))#input()得到用户输入的内容
if guess==number:
	print('恭喜你答对了')
	print('但是你没有得任何奖项')
elif guess<number:
	print('猜的有点小了哦')
else:
	print("太大了，木有那么大哦")
