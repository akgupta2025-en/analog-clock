import turtle
import time
import math

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Analog Clock")

clock = turtle.Turtle()
clock.speed(0)
clock.hideturtle()
clock.pensize(3)

clock.penup()
clock.goto(0, -250)
clock.pendown()
clock.circle(250)


for number in range(1, 13):
    angle = math.radians(number * 30 - 90)

    x = 200 * math.cos(angle)
    y = 200 * math.sin(angle)

    clock.penup()
    clock.goto(x, y)
    clock.write(number, align="center", font=("Arial", 14, "bold"))


def draw_hand(length, angle, color):
    hand = turtle.Turtle()
    hand.speed(0)
    hand.color(color)
    hand.pensize(4)
    hand.hideturtle()

    hand.penup()
    hand.goto(0, 0)
    hand.setheading(angle)
    hand.pendown()
    hand.forward(length)

current_time = time.localtime()

hour = current_time.tm_hour % 12
minute = current_time.tm_min
second = current_time.tm_sec
second_angle = 90 - (second * 6)
minute_angle = 90 - (minute * 6)
hour_angle = 90 - ((hour * 30) + (minute * 0.5))
draw_hand(150, hour_angle, "black")
draw_hand(200, minute_angle, "blue")
draw_hand(220, second_angle, "red")

turtle.done()