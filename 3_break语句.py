running=True
while running:
    s=input('写一些东西：')
    if s=="quit":
        break
    print("文本长度为：",len(s))#len(s)，取出s的文本长度
print('Done')
