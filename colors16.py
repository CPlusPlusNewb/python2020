import turtle #  change the RGB colors
import random # for randomness

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

turt = turtle.Turtle() #was tommy, i just like the name turt more 
turt.shape("turtle")
turt.speed(130)
turt.ht()

number = 0
r = lambda: random.randint(0,255)

while (number < 10):
    cord1 = random.randint(-100,100)
    cord2 = random.randint(-100,100)
    cord3 = random.randint(-100,100)
    randomcolor = str('#%02X%02X%02X' % (r(),r(),r()))
    draw_circle(turt, randomcolor, cord1, cord2, cord3)
    number += 1

w = turtle.Screen()
w.exitonclick()
