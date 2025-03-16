import turtle

# answer 1
# Sabit noktalar ile üçgen çizen fonksiyon
def draw_triangle1():
    """Sabit noktalar ile üçgen çizen fonksiyon"""
    turtle.fillcolor("blue")  # Üçgenin dolgu rengini belirle
    turtle.begin_fill()
    
    # Üç kenarı çiz
    turtle.goto(150, 0)
    turtle.goto(75, 200)
    turtle.goto(0, 0)

    turtle.end_fill()
    turtle.done()

# Turtle'ı başlat
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

#draw_triangle1()

# answer 2 -----------------------------------------------------------------------------
def draw_triangle2(x1, y1, x2, y2, x3, y3, color="red"):
    """Verilen koordinatlara ve renge göre üçgen çizer"""
    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()

    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)

    turtle.end_fill()
    turtle.done()

#draw_triangle2(0, 0, 100, 0, 50, 80, "green")

# answer 3 -----------------------------------------------------------------------------
def draw_triangle(vertices, color="black"):
    """Üçgenin köşe noktalarını alıp çizim yapan fonksiyon"""
    if len(vertices) != 3:
        print("Üçgen için 3 köşe noktası gerekir!")
        return

    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.penup()
    turtle.goto(vertices[0])  # İlk noktaya git
    turtle.pendown()

    for point in vertices[1:]:
        turtle.goto(point)  # Diğer noktalara git

    turtle.goto(vertices[0])  # Başlangıç noktasına dön
    turtle.end_fill()
    turtle.done()

if __name__ == "__main__":
    try:
        points = [(0, 0), (120, 0), (60, 100)]
        color = input("Üçgenin rengini girin: ").strip() or "purple"
        draw_triangle(points, color)
    except Exception as e:
        print(f"Hata oluştu: {e}")
