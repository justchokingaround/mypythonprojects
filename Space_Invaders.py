import turtle
import os

# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15


# move the player left and right
def move_left():
    x = player.xcor()
    if x < -270:        #doesn't cross the borders
        x = -270
    x -= playerspeed
    player.setx(x)


def move_right():
    x = player.xcor()
    if x > 270:
        x = 270
    x += playerspeed
    player.setx(x)

# move the player up and down
def move_up():
    y = player.ycor()
    if y > 270:
        y = 270
    y += playerspeed
    player.sety(y)


def move_down():
    y = player.ycor()
    if y < -270:
        y = -270
    y -= playerspeed
    player.sety(y)

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

# create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.listen()
turtle.onkey(move_right, "Right")
turtle.listen()
turtle.onkey(move_up, "Up")
turtle.listen()
turtle.onkey(move_down, "Down")





delay = raw_input("Press enter to finish.")
