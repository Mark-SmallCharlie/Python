from math import sqrt
a=float(input("第1条边的长度:"))
b=float(input("第2条边的长度:"))
c=float(input("第3条边的长度:"))
    if a+b>c and b+c>a and a+c>b:
        p=(a+b+c)/2
        s=math.sprt(P*(p-a)*(p-b)*(p-c))
        return s
    slse:

        return -1
    
