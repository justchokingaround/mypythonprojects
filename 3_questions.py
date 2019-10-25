print("Hello young fellow, would you like to play a game?")
play_a_game=input('Please answer with Yes or No ')

if play_a_game == 'Do something cool':
    magic = input("What's the magic word ? ")
    if magic != "please":
        print("Nope, that's not the right magic word")
    if magic == "please":
        print("Alright.")
        import turtle
        import math
        import colorsys

        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Something cool")

        phi = 180 * (3 - math.sqrt(5))

        t = turtle.Pen()
        t.speed(0)


        def square(t, size):
            for tmp in range(0, 4):
                t.forward(size)
                t.right(90)


        num = 200

        for x in reversed(range(0, num)):
            t.fillcolor(colorsys.hsv_to_rgb(x / num, 1.0, 1.0))
            t.begin_fill()
            t.circle(5 + x, None, 11)
            square(t, 5 + x)
            t.end_fill()
            t.right(phi)
            t.right(.8)

        turtle.mainloop()

if play_a_game != 'Yes':
    print("Alrighty then, come back when you will feel like playing...")

elif play_a_game:
    score = 0
    print('Okay, cool')
    username = input('What username would you like to use? ')
    print("Alright listen here", username,',')
    print("I have a list of questions I want to ask you")
    print("There are 3 questions")
    print("If you get all of the answers right, you'll get a surprise")
    start = input("Alright, press enter when you are ready ")

    if start == '':
        print("Let's start the quiz!!")

    print("Your first question :")
    fquestion = input("What is 2+2 ? ")
    if fquestion == '4':
        print("Wrong, you are bloody dumb, go home and fuck yourself")

    if fquestion == 'dick':
        print('Weaouw, you found an easter egg, you should be proud of yourself')
        import turtle

        wn = turtle.Screen()
        wn.bgcolor("blue")
        wn.title("Your motherfucking easter egg")
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        my_turtle.setposition(-100, 250)
        my_turtle.pendown()
        my_turtle.speed(0)
        my_turtle.color("red")
        my_turtle.pensize(5)


        # drawing the dick
        def rectangle(length, width, angle):
            for i in range(2):
                my_turtle.forward(width)
                my_turtle.right(angle)
                my_turtle.forward(length)
                my_turtle.right(angle)


        length = 400
        width = 150
        angle = 90

        rectangle(length, width, angle)

        # drawing the left ball

        my_turtle.right(angle)
        my_turtle.fd(length)
        my_turtle.right(angle)
        my_turtle.left(180)
        my_turtle.fd(width / 2)

        for i in range(4):
            my_turtle.rt(angle)
            my_turtle.fd(width)

        # drawing the right ball

        for i in range(4):
            my_turtle.fd(width)
            my_turtle.rt(angle)

        # drawing the tip

        my_turtle.left(90)
        my_turtle.penup()
        my_turtle.fd(length - length / 10)
        my_turtle.pendown()
        my_turtle.fd(length / 10)
        my_turtle.rt(180)
        my_turtle.penup()
        my_turtle.fd(2 * (length / 10))
        my_turtle.pendown()
        my_turtle.lt(90)
        my_turtle.fd(width / 2)
        my_turtle.rt(180)
        my_turtle.fd(width)
        my_turtle.penup()
        my_turtle.setposition(1000, 1000)

    if fquestion != '4':
            print("Well done, you got the first question right")
            score = 1

    print("Your second question is a multiple choice question :")
    print("Only one of the three sentences is the right one,")
    print("To answer type the number of the sentence and hit enter.")
    print("1. A human")
    print("2. An idiot")
    print("3. Something useless")
    squestion = input("Which of the sentences above best describes me ? ")
    if squestion != '3':
        print("Nope, you got it wrong")
    if squestion == '3':
        print("Well done, I must say you are a very smart man")
        score = score+1

    print("Your third question and final question :")
    tquestion = input("Who is the most beautiful person you have ever seen ? ")
    if tquestion != 'Ivan':
        print("No, the most beautiful person you have ever seen is me, you dumbfuck")
    if tquestion == 'Ivan':
        print("Damn you are good at this quizz")
        print("And you are really modest too")
        score = score+1

    print("Your score is", score)
    if score ==1:
        print("You got 1 answer right, maybe you can be better next time")
        print("Faggot")

    if score ==2:
        print("Sad, you were one point away brother")
        print("Maybe better luck next time")

    if score ==3:
        print("Well done, you got all of the answers right")
        print("Here is your surprise")
        for i in range(20):
            print("Fuck you", username)
        print("Now go get a life.")

        import turtle

    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.color("blue")
    my_turtle.pensize(3)
    wn = turtle.Screen()
    wn.bgcolor("red")
    wn.title("Your motherfucking surprise")

    my_turtle.penup()
    my_turtle.setposition(0, 0)
    my_turtle.pendown()



    def rectangle(length, width, angle):
        for i in range(2):
             my_turtle.forward(width)
             my_turtle.right(angle)
             my_turtle.forward(length)
             my_turtle.right(angle)

    length = 50
    width = 35
    angle = 90

    for i in range(20):
        rectangle(length, width, angle)
        length += 10
        width += 10

    my_turtle.penup()
    my_turtle.setposition(0, 0)
    my_turtle.pendown()

    length = -50
    width = -35

    for i in range(20):
        rectangle(length, width, angle)
        length -= 10
        width -= 10


    def rectangle2(length, width, angle):
        for i in range(2):
             my_turtle.forward(width)
             my_turtle.left(angle)
             my_turtle.forward(length)
             my_turtle.left(angle)



    my_turtle.penup()
    my_turtle.setposition(0, 0)
    my_turtle.pendown()

    length = 50
    width = 35
    angle = 90

    for i in range(20):
        rectangle2(length, width, angle)
        length += 10
        width += 10

    my_turtle.penup()
    my_turtle.setposition(0, 0)
    my_turtle.pendown()

    length = -50
    width = -35

    for i in range(20):
        rectangle2(length, width, angle)
        length -= 10
        width -= 10


    my_turtle.shape("square")
    my_turtle.penup()
    my_turtle.speed(0)
    my_turtle.setposition(0, 0)


    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("green")
    pen.penup()
    pen.setposition(-300, -25)
    pen.pendown()
    pen.pensize(5)

    distance = 50
    angle = 90

    # drawing the letter F
    pen.lt(90)
    pen.fd(distance)
    pen.rt(angle)
    pen.fd(distance / 2)
    pen.rt(2 * angle)
    pen.fd(distance / 2)
    pen.lt(90)
    pen.fd(distance / 3)
    pen.lt(90)
    pen.fd(distance / 4)

    # drawing the letter U

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

    # drawing the letter C

    pen.penup()
    pen.setposition(-200, -25)
    pen.pendown()
    pen.fd(distance)
    pen.rt(angle)
    pen.fd(25)
    pen.rt(2 * angle)
    pen.fd(distance / 2)
    pen.lt(angle)
    pen.fd(distance)
    pen.left(angle)
    pen.fd(distance / 2)

    # drawing the letter K

    pen.penup()
    pen.setposition(-150, -25)
    pen.pendown()
    pen.lt(90)
    pen.fd(distance)
    pen.rt(180)
    pen.fd(distance / 2)
    pen.lt(135)
    pen.fd(35)
    pen.rt(180)
    pen.fd(35)
    pen.lt(angle)
    pen.fd(35)

    # drawing the letter Y

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

    # drawing the letter O

    pen.penup()
    pen.setposition(25, -25)
    pen.pendown()
    pen.lt(angle / 2)


    def rectangle(length, width, angle):
        for i in range(2):
            pen.fd(length)
            pen.rt(angle)
            pen.fd(width)
            pen.rt(angle)


    length = 50
    width = 25

    rectangle(length, width, angle)

    # drawing the letter U

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

    # drawing exclamation mark

    pen.penup()
    pen.setposition(175, -15)
    pen.pendown()
    pen.fd(40)
    pen.penup()
    pen.setposition(175, -25)
    pen.pendown()
    pen.shape("circle")
    pen.shapesize(0.25)