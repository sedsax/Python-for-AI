import turtle
import emojis

turtle.speed(0)
turtle.bgcolor("white")
turtle.title("Emojiler")

# Emojileri yan yana çiz
emojis.draw_smiley(-250, -50)
emojis.draw_cool(-80, -50)
emojis.draw_surprised(90, -50)
emojis.draw_laughing(260, -50)

turtle.done()