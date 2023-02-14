import turtle

pen = turtle.Turtle()

# Let's make a method than can draw a curve
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

# Let's make a method than can draw a heart, should also take in a colour for the heart
def heart(colour):
    pen.fillcolor(colour)
    pen.begin_fill()
    pen.left(140)
    pen.forward(111.65)
    curve()
    pen.left(120)
    curve()
    pen.forward(111.65)
    pen.end_fill()

# Let's make a method that can write text, should also take in a colour for the text
def text(message, colour):
    pen.up()
    pen.setpos(-90, 95)
    pen.down()
    pen.color(colour)
    pen.write(message, font=("Arial", 12, "bold"))

# Let's make a method that does that brings it all together
def main():
    pen.speed(10)
    heart("pink")
    text("Happy Valentine's Day\nto my amazing network", "red")
    pen.ht()
    turtle.exitonclick()
    
# Let's call the main method
if __name__ == "__main__":
    main()
