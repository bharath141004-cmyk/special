
import turtle
import math

screen = turtle.Screen()
screen.setup(900, 800)
screen.bgcolor("black")
screen.title("A Little Secret ❤️")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("#ffb6c1")

points = []

for scale in range(11, 17):
    for i in range(120):
        angle = i * 2 * math.pi / 120

        x = 16 * math.sin(angle) ** 3 * scale
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * scale

        points.append((x, y))

index = 0

def animate_heart():
    global index

    if index < len(points):
        x, y = points[index]
        t.goto(x, y)

        t.write(
            "I love you",
            align="center",
            font=("Arial", 8, "bold")
        )

        index += 1
        screen.update()
        screen.ontimer(animate_heart, 40)

    else:
        t.goto(0, -300)
        t.color("#ff1493")
        t.write(
            "Forever in my heart",
            align="center",
            font=("Arial", 18, "bold")
        )
        screen.update()

screen.ontimer(animate_heart, 500)
turtle.done()
