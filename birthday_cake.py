import turtle

def draw_cake():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Birthday Wish with Cake")

    pen = turtle.Turtle()
    pen.speed(3)

    # Draw the base of the cake
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    pen.color("chocolate")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(200)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

    # Draw candles
    pen.penup()
    pen.goto(-80, 50)
    pen.pendown()
    pen.color("yellow")
    for _ in range(3):
        pen.begin_fill()
        for _ in range(2):
            pen.forward(20)
            pen.left(90)
            pen.forward(50)
            pen.left(90)
        pen.end_fill()
        pen.penup()
        pen.forward(60)
        pen.pendown()

    # Add flames
    pen.penup()
    pen.goto(-70, 100)
    pen.color("orange")
    for _ in range(3):
        pen.begin_fill()
        pen.circle(10)
        pen.end_fill()
        pen.penup()
        pen.forward(60)
        pen.pendown()

    # Write Happy Birthday
    pen.penup()
    pen.goto(-90, -200)
    pen.color("black")
    pen.write("Happy Birthday!", font=("Arial", 24, "bold"))
    pen.hideturtle()

    screen.mainloop()

# Call the function to draw the cake
draw_cake()
