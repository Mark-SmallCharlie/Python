import random
#创建抽奖名单
名单 = []
while True:
    name = input("姓名:")
    if name.strip()=="":
        break
    else:
        名单.append(name)
print("名单采集完毕，名单如下:")
print(名单)
#开始抽奖,20%为一等奖,30%为二等奖,40%为三等奖
n=len(名单)
print("参与抽奖人数:",n)
#三等奖
x=int("n*0.4) input("chijian")
    print("--------------------------")
    print("三等奖是:",x,"人")
i = 0
while i<x:
    j = random.randint(0,len(名单)-1)
    print(名单[j])
    del 名单[j]
    i = i+1
