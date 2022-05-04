# # CTI-110
# CTI-110
# P4LAB2b - Turtle Graphic
# Todd Henderson
# 9 May 2022

import turtle
my_turtle = turtle.Turtle()
drawing_area = turtle.Screen()
drawing_area.bgcolor("gray")
drawing_area.setup (width=750, height=530, startx=0, starty=0)
# start first inital "T"
t = turtle
t.shape("turtle")
t.setworldcoordinates(-1, -200, 20, 10)
drawing_area = t.Screen()
t.pensize(5)
t.color("orange","yellow")
t.forward(7)
t.penup()
t.back(3.5)
t.right(90)
t.pendown()
t.forward(80)
t.penup()
t.end_fill()
# Start second initial "H"
h = turtle
h.shape("turtle")
drawing_area = h.Screen()
h.pensize(10)
h.color("blue","red")
h.forward(15)
h.pendown()
h.forward(90)
h.penup()
h.left(180)
h.forward(40)
h.right(90)
h.pendown()
h.forward(4)
h.penup()
h.left(90)
h.pendown()
h.forward(40)
h.right(180)
h.forward(90)


turtle.mainloop()