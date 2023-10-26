import turtle

square = turtle.Turtle()
square.color('white')
sc = turtle.Screen()
sc.bgcolor('black')
square.begin_fill()
square.fillcolor('red')
for i in range(4):
    square.forward(100)
    square.left(90)

square.end_fill()
square.hideturtle()
