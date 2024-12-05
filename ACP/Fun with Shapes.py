import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")  

pen = turtle.Turtle()

def draw_polygon(sides, side_length, fill_color):
    pen.fillcolor(fill_color)  
    pen.begin_fill()
    for _ in range(sides):
        pen.forward(side_length)
        pen.left(360 / sides)
    pen.end_fill()

# Draw an equilateral triangle
draw_polygon(3, 100, "red")

pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Draw a rectangle
draw_polygon(4, 100, "green")

pen.penup()
pen.goto(150, 0)
pen.pendown()

# Draw a hexagon
draw_polygon(6, 50, "yellow")

turtle.done()