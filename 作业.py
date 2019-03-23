# -*- coding: utf-8 -*-

#倒序输出
list=[1,2,3,4,5,6,7,8,9]
print(list[::-1])

#替换字符串
a=input('输入字符串')
b=input('输入要查找的字符')
if b in a:
    print("找到字符串")
    c=input('输入你要替换的字符串')
    print('替换后的结果：\n',a.replace(b,c))
else:
    print('没有找到')


