import turtle

def drawBase():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.circle(100)

def drawMidSection():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(70)

def drawHead():
    turtle.penup()
    turtle.goto(0, 140)
    turtle.pendown()
    turtle.circle(40)

    # Gözler
    turtle.penup()
    turtle.goto(-15, 180)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(15, 180)
    turtle.pendown()
    turtle.circle(5)

    # Ağız
    turtle.penup()
    turtle.goto(-20, 160)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(40)

def drawArms():
    # Sol kol
    turtle.penup()
    turtle.goto(-70, 70)
    turtle.pendown()
    turtle.setheading(165)
    turtle.forward(55)

    turtle.penup()
    turtle.goto(-122, 86)
    turtle.pendown()
    turtle.setheading(105)
    turtle.forward(55)

    turtle.penup()
    turtle.goto(-135, 138)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(20)

    turtle.penup()
    turtle.goto(-135, 138)
    turtle.pendown()
    turtle.setheading(140)
    turtle.forward(20)

    # Sağ kol
    turtle.penup()
    turtle.goto(70, 70)
    turtle.pendown()
    turtle.setheading(35)
    turtle.forward(70)

    turtle.penup()
    turtle.goto(125, 110)
    turtle.pendown()
    turtle.setheading(70)
    turtle.forward(20)

    turtle.penup()
    turtle.goto(125, 110)
    turtle.pendown()
    turtle.setheading(20)
    turtle.forward(20)


def drawHat():
    # Şapkanın alt kısmı (kenar)
    turtle.penup()
    turtle.goto(-50, 200)  # Alt kısmın başlangıç noktası
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(100)  # Alt kısmın genişliği
    turtle.left(90)
    turtle.forward(20)  # Alt kısmın yüksekliği
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()

    # Şapkanın üst kısmı (gövde)
    turtle.penup()
    turtle.goto(-25, 210)  # Üst kısmın başlangıç noktası
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward(50)  # Üst kısmın genişliği
    turtle.left(90)
    turtle.forward(50)  # Üst kısmın yüksekliği
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()

def main():
    turtle.speed(5)
    drawBase()
    drawMidSection()
    drawHead()
    drawArms()
    drawHat()
    turtle.done()

if __name__ == "__main__":
    main()