import turtle
import math

myturtle = turtle.Turtle()

myturtle.shape("turtle")

myturtle.fillcolor("gold")
myturtle.speed(1)

myturtle.begin_fill()
myturtle.circle(100)
myturtle.end_fill()

myturtle.up()

myturtle.left(90)
myturtle.forward(70)
myturtle.left(90)
myturtle.forward(40)
myturtle.right(180)

myturtle.fillcolor("black")
myturtle.down()

myturtle.forward(80)
myturtle.left(45)
myturtle.forward(20)
myturtle.left(135)

myturtle.up()

myturtle.forward(108)
myturtle.left(135)

myturtle.down()

myturtle.forward(20)
myturtle.right(225)

myturtle.up()
myturtle.shape("circle")

myturtle.forward(60)
myturtle.stamp()
myturtle.right(90)
myturtle.forward(80)
myturtle.left(90)
myturtle.stamp()

myturtle.forward(90)

myturtle.shape("turtle")
myturtle.write("Great Job Today!", align="right", font=("Arial", 24, "normal"))

myturtle.hideturtle()

turtle.done()