import ex63
a=float(input("第1条边的长度:"))
b=float(input("第2条边的长度:"))
c=float(input("第3条边的长度:"))
s=ex63.area(a,b,c)
if s>0:
    print("三角形面积=",s)
else:
    print("输入有误，无法构成三角形!")
    
