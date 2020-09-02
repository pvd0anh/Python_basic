import turtle
import random

def main():
    turtle.setup(600, 600)
    turtle.bgcolor('black')
    turtle.hideturtle()
    turtle.speed(0)
    stars()
    skyline(-300, -400, 300, 'gray')
    skyline(0, -400, 300, 'gray')
    skyscrapers(-300, -100, 'gray')
    window(10, 50, 20, 'yellow')    # Middle Skyscraper Window
    window(-100, 150, 20, 'yellow') # Middle Skyscraper Window
    window(-100, 120, 20, 'yellow') # Middle Skyscraper Window
    window(-20, -120, 20, 'yellow') # Middle Skyscraper Window
    window(-200, -40, 20, 'yellow') # Left Skyscraper Window
    window(125, 85, 20, 'yellow')   # Right Skyscraper Window
    batlight(115, 133, 8, 'silver')
    batsignal(107, 133, 'yellow')
    batlight(250, 240, 30, 'yellow')
    batsymbol(235, 275, 'black')

def stars():
    for stars in range(75):
        x = random.randrange(-300, 300)
        y = random.randrange(-100, 300)
        turtle.pencolor('white')
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot()

def skyline(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor('gray')
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

def skyscrapers(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()    # (-300, -100)
    turtle.begin_fill()
    turtle.forward(70)  # (-230, -100)
    turtle.left(90)
    turtle.forward(100) # Left Skyscraper Wall (-230, 0)
    turtle.right(90)    # Left Skyscraper
    turtle.forward(100) # Left Skyscraper Roof (-130, 0)
    turtle.left(90)
    turtle.forward(200) # Middle Skyscraper Wall (-130, 200)
    turtle.right(90)    # Middle Skyscraper
    turtle.forward(150) # Middle Skyscraper Roof (20, 200)
    turtle.right(90)    # Middle Skyscraper
    turtle.forward(225) # Middle Skyscraper Wall (20, -25)
    turtle.left(90)
    turtle.forward(75)  # (95, -25)
    turtle.left(90)
    turtle.forward(150) # 1st Right Skyscraper Wall (95, 125)
    turtle.right(90)    # 1st Right Skyscraper
    turtle.forward(100) # 1st Right Skyscraper Roof (195, 125)
    turtle.right(90)    # 1st Right Skyscraper 
    turtle.forward(100) # 1st Right Skyscraper Wall (195, 25)
    turtle.left(90)     
    turtle.forward(50)  # 2nd Right Skyscraper Roof (195, 75)
    turtle.right(90)    # 2nd Right Skyscraper
    turtle.forward(175) # 2nd Right Skyscraper Wall (195, -75)
    turtle.left(90)     
    turtle.forward(105) # (300, -100)
    turtle.right(90)
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(600) # Complete Skyscraper Box
    turtle.right(90)
    turtle.forward(1)    
    turtle.end_fill()

def window(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

def batlight(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def batsignal(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor('yellow')
    turtle.pensize(4)
    turtle.pendown()
    turtle.right(34)
    turtle.forward(180)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pensize(6)
    turtle.pendown()
    turtle.right(6)
    turtle.forward(160)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pensize(6)
    turtle.pendown()
    turtle.right(6)
    turtle.forward(160)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pensize(4)
    turtle.pendown()
    turtle.right(7)
    turtle.forward(180)

def batsymbol(x, y, color):
    turtle.penup()
    turtle.pensize(1)
    turtle.pencolor('black')
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(15)
    turtle.forward(20)
    turtle.right(105)
    turtle.forward(10)
    turtle.right(45)
    turtle.forward(20)
    turtle.left(25)
    turtle.forward(10)
    turtle.right(105)
    turtle.forward(10)
    turtle.left(25)
    turtle.forward(23)
    turtle.right(45)
    turtle.forward(10)
    turtle.right(110)
    turtle.forward(24)
    turtle.left(90)
    turtle.forward(5)
    turtle.right(85)
    turtle.forward(13)
    turtle.right(85)
    turtle.forward(5)
    turtle.end_fill()
    turtle.done()
    
# Call the main function.
main()