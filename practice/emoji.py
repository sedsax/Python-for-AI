import turtle

def draw_smile_face(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    # Eyes
    for ex in [-20, 20]:
        turtle.penup()
        turtle.goto(x + ex, y + 60)
        turtle.pendown()
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(7)
        turtle.end_fill()

    # Smile
    turtle.penup()
    turtle.goto(x - 20, y + 35)
    turtle.pendown()
    turtle.width(5)
    turtle.goto(x + 23, y + 35)

    turtle.penup()
    turtle.goto(x - 20, y + 35)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.width(5)
    turtle.circle(25, 120)
    turtle.width(1)

def draw_surprised_face(x, y):
    turtle.penup()
    turtle.goto(x+36, y+20)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    # Eyes
    for ex in [-20, 20]:
        turtle.penup()
        turtle.goto(x + ex, y + 60)
        turtle.pendown()
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(7)
        turtle.end_fill()

    # Surprised mouth
    turtle.penup()
    turtle.goto(x+8, y + 25)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x+8, y + 25)
    turtle.pendown()
    turtle.circle(15)

# Ekranı ayarla
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

draw_smile_face(-100, -50)
draw_surprised_face(100, -50)

turtle.done()