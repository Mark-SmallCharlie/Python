#创建抽奖名单
名单=[]
while True:
    name=input("姓名:")
    if name.strip()=="":#检测输入内容是否为空
        break
    else:
        名单.append(name)
print("名单采集完毕,名单如下:")
print(名单)    
