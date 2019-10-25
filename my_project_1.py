import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.setposition(-300, -25)
pen.pendown()
pen.pensize(3)

distance = 50
angle = 90

#drawing the letter F
pen.lt(90)
pen.fd(distance)
pen.rt(angle)
pen.fd(distance/2)
pen.rt(2*angle)
pen.fd(distance/2)
pen.lt(90)
pen.fd(distance/3)
pen.lt(90)
pen.fd(distance/4)

#drawing the letter U

pen.penup()
pen.setposition(-250, -25)
pen.pendown()
pen.lt(90)
pen.fd(50)
pen.rt(180)
pen.fd(distance)
pen.lt(angle)
pen.fd(25)
pen.lt(angle)
pen.fd(distance)

#drawing the letter C

pen.penup()
pen.setposition(-200, -25)
pen.pendown()
pen.fd(distance)
pen.rt(angle)
pen.fd(25)
pen.rt(2*angle)
pen.fd(distance/2)
pen.lt(angle)
pen.fd(distance)
pen.left(angle)
pen.fd(distance/2)

#drawing the letter K

pen.penup()
pen.setposition(-150, -25)
pen.pendown()
pen.lt(90)
pen.fd(distance)
pen.rt(180)
pen.fd(distance/2)
pen.lt(135)
pen.fd(35)
pen.rt(180)
pen.fd(35)
pen.lt(angle)
pen.fd(35)

#drawing the letter Y

pen.penup()
pen.setposition(-25, -25)
pen.pendown()
pen.lt(135)
pen.fd(25)
pen.lt(45)
pen.fd(35)
pen.rt(180)
pen.fd(35)
pen.lt(90)
pen.fd(35)

#drawing the letter O

pen.penup()
pen.setposition(25, -25)
pen.pendown()
pen.lt(angle/2)
def rectangle(length, width, angle):
    for i in range(2):
         pen.fd(length)
         pen.rt(angle)
         pen.fd(width)
         pen.rt(angle)

length = 50
width = 25

rectangle(length, width, angle)

#drawing the letter U

pen.penup()
pen.setposition(75, -25)
pen.pendown()
pen.fd(50)
pen.rt(180)
pen.fd(distance)
pen.lt(angle)
pen.fd(25)
pen.lt(angle)
pen.fd(distance)

#drawing exclamation mark

pen.penup()
pen.setposition(175, -15)
pen.pendown()
pen.fd(40)
pen.penup()
pen.setposition(175, -25)
pen.pendown()
pen.shape("circle")
pen.shapesize(0.25)
