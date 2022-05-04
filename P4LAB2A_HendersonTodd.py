# # CTI-110
# CTI-110
# P4LAB2A - Turtle Graphic
# Todd Henderson
# 9 May 2022

import turtle

my_turtle = turtle.Turtle()
# create two turtles
squ = turtle
# drawing a square with turtle
squ.shape("turtle")
drawing_area = squ.Screen()
squ.pensize(10)
squ.color("red","blue")
squ.begin_fill()
for i in range(4):
	squ.forward(200)
	squ.left(90)
squ.end_fill()
# drawing a triable with turtle
tri = turtle
tri.shape("turtle")
drawing_area = tri.Screen()
tri.pensize(10)
tri.color("orange","yellow")
tri.begin_fill()
for i in range(3):
	tri.forward(100)
	tri.left(120)
tri.end_fill()
my_turtle.write(my_turtle.position(), font=("Arial", 16, "normal"))
turtle.mainloop()