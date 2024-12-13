import turtle

myturtle = turtle.Turtle()

def draw_triangle(side_length):
    for i in range(3):
        myturtle.right(120)
        myturtle.forward(side_length)
    turtle.right(180)
    
draw_triangle(20)

turtle.done()