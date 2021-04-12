import random
import time
import turtle


def draw_finish_line():
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.setposition(305, 200)
    finish_line.right(90)
    finish_line.pendown()
    finish_line.forward(250)
    finish_line.hideturtle()


def initiate_racers():
    hare = turtle.Turtle()
    tort = turtle.Turtle()
    hare.shape("arrow")
    tort.shape("turtle")
    tort.color("green")
    hare.color("red")

    tort.penup()
    hare.penup()

    hare.left(90)
    hare.forward(150)
    hare.right(90)

    tort.back(300)
    hare.back(300)

    return hare, tort


draw_finish_line()

hare, tort = initiate_racers()


def move_hare():
    event = random.randrange(1, 11)
    if 1 <= event <= 5:
        return round(3 * 60 / 7)
    if 5 < event <= 7:
        return round(-6 * 60 / 7)
    return round(1 * 60 / 7)


def move_tort():
    event = random.randrange(1, 11)
    if 1 <= event <= 2:
        return 0
    if 2 < event <= 4:
        return round(9 * 60 / 7)
    if event == 5:
        return round(-12 * 60 / 7)
    if 5 < event <= 8:
        return round(1 * 60 / 7)
    return round(-2 * 60 / 7)


x_pos_hare = -300.00
x_pos_tort = -300.00

y_pos_hare = 150.00
y_pos_tort = 0.00

while x_pos_hare < 300 and x_pos_tort < 300:
    time.sleep(0.5)

    x_pos_hare += move_hare()
    x_pos_tort += move_tort()

    if x_pos_tort < -300:
        x_pos_tort = -300
    if x_pos_hare < -300:
        x_pos_hare = -300

    hare.setposition(x_pos_hare, y_pos_hare)
    tort.setposition(x_pos_tort, y_pos_tort)

if x_pos_tort >= 300:
    print("TORTOISE WINS!")
    hare.hideturtle()
else:
    print("Hare wins.")
    tort.hideturtle()
time.sleep(10)
