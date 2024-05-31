a=float(input("第1条边的长度:"))
b=float(input("第2条边的长度:"))
c=float(input("第3条边的长度:"))
if a+b>c and b+c>a and a+c>b:
    print("三角形的三边边长:",a,b,c)
else:
    print("ERROR,Can have 三角形!")
