import math
def area(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        p=(a+b+c)/2
        s=math.sprt(P*(p-a)*(p-b)*(p-c))
        return s
    else:

        return -1
