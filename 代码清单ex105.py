import turtle
turtle.pensize(1)
turtle.speed(15)
c=["black","red","green","yellow","orange","blue"]
for i in range(50,200,100):
    turtle.pencolor(c[int(i/10)%6])
    turtle.circle(i)
    turtle.penuo()
    turtle.forward(-10)
    turtle.pendown()
    turtle.right(900)
