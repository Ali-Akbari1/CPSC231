# Draw a line and a box. Determine whether the line is inside the box

# In order to draw, we need a library to let us do that

import turtle

# We will define some constants for the size of the window

WIDTH = 800
HEIGHT = 600

# Middle point of the window to display the text

MIDDLEX = WIDTH/2
MIDDLEY = HEIGHT/2

# We will also need to set up our window and get our drawing pointer(pen)

pointer = turtle.Turtle()

# Get the window, so we can set it up with (0,0) and (800,600) in the top right corner

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

# Let's hide the pointer

pointer.hideturtle()

# We will use integer pixel coordinates hence we cast string into integer

x1 = int(input("Enter x start of line: "))
y1 = int(input("Enter y start of line: "))

x2 = int(input("Enter x of end of line: "))
y2 = int(input("Enter y of end of line: "))

xc = int(input("Enter x of centre of box: "))
yc = int(input("Enter y of centre of box: "))

width = int(input("Enter width of the box: "))
height = int(input("Enter height of the box: "))

# Draw the LINE and BOX

# Draw the line
# Pointer is up

pointer.up()
pointer.goto(x1, y1)
pointer.down()
pointer.goto(x2, y2)
pointer.up()

# Draw the box
# Go to top left corner of the box
# x coordinates minus half the width of the box
# y coordinates minus half the height of the box

topleftx = xc - width/2
toplefty = yc - height/2

pointer.goto(topleftx,toplefty)
pointer.down()
# Draw each corner of the box

pointer.goto(topleftx + width, toplefty)
pointer.goto(topleftx + width, toplefty + height)
pointer.goto(topleftx, toplefty + height)
pointer.goto(topleftx, toplefty)

pointer.up()

# DETERMINE IF THE LINE IS INSIDE THE BOX
# Check if (x1,y1) is inside the box
# This is true x1 is between topleftx and topleftx + width AND
# y1 is between toplefty and toplefty + height

x1Inisde = (x1 >= topleftx) and (x1 <= topleftx + width)
y1Inside = (y1 >= toplefty) and (y1 <= toplefty + height)

startInside = x1Inisde and y1Inside

# Check if (x2, y2) inside the box

x2Inisde = (x2 >= topleftx) and (x2 <= topleftx + width)
y2Inside = (y2 >= toplefty) and (y2 <= toplefty + height)

endInside = x2Inisde and y2Inside

fullInside = startInside and endInside

pointer.color("red")
pointer.goto(MIDDLEX, MIDDLEY)
if fullInside:
    pointer.write("Line is inside the box fully. ")
elif startInside:
    pointer.write("Start of line is inside the box ")
elif endInside:
    pointer.write("End of the line is inside the box ")
else:
    pointer.write("Neither end of the line is inside the box")


screen.exitonclick()

