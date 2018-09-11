from turtle import Turtle, Screen
import math


# turtle.forward(x) takes in a pixel value
# turtle.left/right(x) takes in a degree value
# turtle.color("red","blue") takes in a common color name or hex value. First is outline value and second is fill value
# turtle.begin_fill() at start of fill code
# turtle.end_fill() at end of fill code
# turtle.penup() to not draw line
# turtle.pendown() to start drawing again
# turtle.setheading(x) takes in a value in degrees to head in 0-360
# turtle.speed(x) increases speed of draw - max 10

wn = Screen()
wn.bgcolor('lightblue')

spaceship = Turtle()
spaceship.color('red')
#spaceship.penup()

speed = 1

def travel():
    spaceship.forward(speed)
    wn.ontimer(travel, 10)

wn.onkey(lambda: spaceship.setheading(90), 'Up')
wn.onkey(lambda: spaceship.setheading(180), 'Left')
wn.onkey(lambda: spaceship.setheading(0), 'Right')
wn.onkey(lambda: spaceship.setheading(270), 'Down')

wn.listen()

travel()

wn.mainloop()