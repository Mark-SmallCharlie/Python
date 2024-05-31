import turtle
c = ["red","blue","yellow","green","purple"]
s = input ("螺旋图的外形(边数,2-6):")
s = int(s)
turtle.speed(15)
for i in range(800):
    turtle.pencolor(c[i&s])
    turtle.forward(i)
    turtle.left(360/s+1)
                
