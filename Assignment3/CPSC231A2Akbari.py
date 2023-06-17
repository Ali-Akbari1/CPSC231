# CPSC 231, Ali Akbari, 30171539
# Tutorial T01, June 9
# Description:
# Python code that uses the turtle module to create a graphical representation of a line and a circle
# That is based on user input including, the centre of the circle, radius of the circle, and the endpoints of the line
# It then uses the math module to calculate the number of intersections between the line and circle
# Then displays the circle in red the line in blue and number of intersections in green text on an x and y axis


# Import turtle and math modules
import turtle
import math

# Initialize constants Width and Height for the window screen
WIDTH = 800
HEIGHT = 600

# Initialize constants MiddleX and MiddleY for the middle of the window screen
MIDDLEX = WIDTH/2
MIDDLEY = HEIGHT/2


# Initialize the drawing pointer
pointer = turtle.Turtle()

# Setting up the window so that (0,0) is on the bottom left
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()


# Draw the x and y axes
pointer.up()
pointer.goto(MIDDLEX, 0)
pointer.down()
pointer.goto(MIDDLEX, 600)
pointer.up()
pointer.goto(0, MIDDLEY)
pointer.down()
pointer.goto(800, MIDDLEY)
pointer.up()

# Get the input from the user for the centre of the circle and radius of the circle
xc = int(input("Enter x of centre of circle: "))
yc = int(input("Enter y of centre of circle: "))

r = float(input("Enter radius of circle: "))

# Get the input from the user for the start and end of the line
x1 = int(input("Enter x of start of line: "))
y1 = int(input("Enter y of start of line: "))

x2 = int(input("Enter x of end of line: "))
y2 = int(input("Enter y of end of line: "))


# Draw the circle and make it red
pointer.color("red")
pointer.goto(xc, yc - r)
pointer.down()
pointer.circle(r)
pointer.up()

# Draw the line and make it blue
pointer.color("blue")
pointer.up()
pointer.goto(x1, y1)
pointer.down()
pointer.goto(x2, y2)
pointer.up()


# Calculate a, b , and c for the quadratic formula
a = (x2-x1)**2 + (y2-y1)**2
b = 2*((x1-xc)*(x2-x1)+(y1-yc)*(y2-y1))
c = (x1-xc)**2 + (y1 - yc)**2 - r**2

# Get the alpha values from the quadratic formula
alpha1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
alpha2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)


# Set pointer colour green for the text
pointer.color("green")

# If the discriminant is less than zero there are no intersections
if (b**2 - (4*a*c)) < 0:
    pointer.goto(MIDDLEX, MIDDLEY)
    pointer.write("No Intersection!", align="center", font=("Arial", 16, "normal"))


# If the discriminant is equal to zero there is one intersection
elif (b**2 - (4*a*c)) == 0:
    pointer.goto(MIDDLEX, MIDDLEY)
    pointer.write("One Intersection!", align="center", font=("Arial", 16, "normal"))

# Otherwise discriminant is greater than zero
else:

    # If both alpha values are either greater than 1 or less than 0 there are no intersections
    if (alpha1 > 1 or alpha1 < 0) and (alpha2 > 1 or alpha2 < 0):
        pointer.goto(MIDDLEX, MIDDLEY)
        pointer.write("No Intersection!", align="center", font=("Arial", 16, "normal"))

    # If only one of the alpha values is greater than 1 or less than zero there is one intersection
    elif (alpha1 > 1 or alpha1 < 0) or (alpha2 > 1 or alpha2 < 0):
        pointer.goto(MIDDLEX, MIDDLEY)
        pointer.write("One Intersection!", align="center", font=("Arial", 16, "normal"))

    # Otherwise alpha values are between 0 and 1, and there are two intersections
    else:
        pointer.goto(MIDDLEX, MIDDLEY)
        pointer.write("Two Intersection!", align="center", font=("Arial", 16, "normal"))

# Exit out of the screen when you click on it
screen.exitonclick()

