import turtle
#turtle.tracer(1, 1)
w=turtle.Screen()
w.bgcolor("light green")
turtle=turtle.Turtle()
turtle.color("peru")
turtle.width(7)
colors=["peru","ivory","dark orange","coral","cyan","hot pink","gold","yellow","red","pink","green","blue","light green"]

# def f1():
#     for i in range(7):
#         turtle.pensize(5)
#         turtle.pencolor('light blue')
#         turtle.color(colors[i%19])
#         turtle.begin_fill()
#         turtle.left(330)
#         turtle.forward(55)
#         turtle.begin_fill()
#         turtle.rt(110)
#         turtle.circle(33)
#         turtle.end_fill()
#         turtle.rt(11)
#         turtle.backward(33)
#         turtle.end_fill()
#f1()

def move(x,y):
    turtle.up()
    turtle.setposition(0,0)
    turtle.setheading(90)
    turtle.rt(90)
    turtle.fd(x)
    turtle.lt(90)
    turtle.fd(y)
    turtle.pendown()

def mov(x,y):
    turtle.up()
    turtle.setposition(0,0)
    turtle.setheading(90)
    turtle.lt(90)
    turtle.fd(x)
    turtle.rt(90)
    turtle.fd(y)
    turtle.pendown()

# def A(size):
#     #turtle.rt(-74)
#     turtle.forward(size)
#     turtle.rt(150)
#     turtle.fd(size-10)
#     turtle.backward(size/2)
#     turtle.rt(104)
#     turtle.fd(size/4)

def B(size):
    turtle.lt(90)
    turtle.forward(60)
    turtle.rt(90)
    for i in range(18):
        turtle.rt(9)
        turtle.fd(3)
    for i in range(18):
        turtle.rt(13)
        turtle.backward(5)
B(200)

w.exitonclick()