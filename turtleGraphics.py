

# Draw a line and a box. Deterine whether the line is inside the box.

# In order to draw, we need a library to let us do that
# We will import that library
import turtle

# We will define some constants for the size of the window
WIDTH = 800
HEIGHT = 600

# Middle point of the window to display the text
MIDDLEX = WIDTH/2
MIDDLEY = HEIGHT/2

# we will also need to setup our window and get our drawing pointer (pen)
pointer = turtle.Turtle()

# Get the window so we can setit up with (0,0) and (800,600)in the top right corner
screen = turtle.Screen() # 
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0,0,WIDTH, HEIGHT)

# Let's hide the pointer
pointer.hideturtle()

#1. TAKE THE INPUT OF TWO ENDS OF A LINE
# AND A CENTRE OF A BOX AND A WIDTH AND HEIGHT OF A BOX

print("The program takes input for the two ends of a line, the centre and dimension of the box.")
print("The program will draw the shapes and tell if the line is fully inside the box")

# We will use integer pixel coordinates hence we cast string into integer
x1 = int(input("Enter x of start of line: "))
y1 = int(input("Enter y of start of line: "))

x2 = int(input("Enter x of end of line: "))
y2 = int(input("Enter y of end of line: "))

xc = int(input("Enter x of centre of box: "))
yc = int(input("Enter y of centre of box: "))

width = int(input("Enter width of the box: "))
height = int(input("Enter height of the box: "))


#2. DRAW THE LINE AND BOX

# draw the line
# pointer is up
pointer.up()
# go to the start of the line
pointer.goto(x1,y1)
# put down the pointer
pointer.down()
# draw the line
pointer.goto(x2,y2)
pointer.up()

# Draw the box
# can go to centre of box with pointer.goto(xc,yc)
#But let's actually go to top left corner of box
#       x coordinates minus half the width of the box
#       y coordinates minues half the height of the box
topleftx = xc - width/2
toplefty = yc - height/2
pointer.goto(topleftx, toplefty)
#put down the pen
pointer.down()
#draw each corner of the box
pointer.goto(topleftx+width, toplefty)
pointer.goto(topleftx+width, toplefty + height)
pointer.goto(topleftx, toplefty + height)
pointer.goto(topleftx, toplefty)
# pick up the pen
pointer.up()

#3. DETERMINE IF THE LINE IS INSIDE THE BOX
# check if (x1,y1) is inside the box
# this is true if      x1 is between topleftx and topleftx + width AND
#                      y1 is between  toplefty and toplefty + height 

x1Inside = x1 >= topleftx and x1 <= topleftx + width
y1Inside = y1 >= toplefty and y1 <= toplefty + height

# whether the start is inside

startInside = x1Inside and y1Inside

# check if (x2,y2) inside the box

x2Inside = x2 >= topleftx and x2 <= topleftx + width
y2Inside = y2 >= toplefty and y2 <= toplefty + height

endInside = x2Inside and y2Inside

fullInside = startInside and endInside

pointer.color("red")
pointer.goto(MIDDLEX, MIDDLEY)
#4. IF IT IS WE'LL PRINT THAT IT'S INSIDE
if fullInside:
	pointer.write("Line inside the box fully")
elif startInside:
	pointer.write("Start of line inside the box")
elif endInside:
	pointer.write("End of line inside the box")
else:
	pointer.write("Neither end of the line inside the box")


screen.exitonclick()
