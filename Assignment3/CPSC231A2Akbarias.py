# CPSC 231, Ali Akbari, 30171539
# Tutorial T01, June 9
# WRITE DESCRIPTION HERE

# Draw your axis black, your circle red, your line blue.

import turtle
import math

WIDTH = 800
HEIGHT = 600

MIDDLEX = WIDTH/2
MIDDLEY = HEIGHT/2


pointer = turtle.Turtle()

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()


# Draw Axis
pointer.up()
pointer.goto(MIDDLEX, 0)
pointer.down()
pointer.goto(MIDDLEX, 600)
pointer.up()
pointer.goto(0, MIDDLEY)
pointer.down()
pointer.goto(800, MIDDLEY)
pointer.up()

# Input from User

xc = int(input("Enter x of centre of circle: "))
yc = int(input("Enter y of centre of circle: "))
r = float(input("Enter radius of circle: "))

x1 = int(input("Enter x of start of line: "))
y1 = int(input("Enter y of start of line: "))

x2 = int(input("Enter x of end of line: "))
y2 = int(input("Enter y of end of line: "))


# Draw circle
pointer.color("red")
pointer.goto(xc, yc - r)
pointer.down()
pointer.circle(r)
pointer.up()

# Draw line
pointer.color("blue")
pointer.up()
pointer.goto(x1, y1)
pointer.down()
pointer.goto(x2, y2)
pointer.up()


# Calculate the number of intersection points between the circle and line. Then, produce a conditional
# statement that lets you display a message indicating the number of intersection points to the user.

a = (x2-x1)**2 + (y2-y1)**2
b = 2*((x1-xc)*(x2-x1)+(y1-yc)*(y2-y1))
c = (x1-xc)**2 + (y1 - yc)**2 - r**2
alpha1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
alpha2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)

print(alpha1)
print(alpha2)

pointer.color("green")


print((b**2 - (4*a*c)))

# No intersections
if (b**2 - (4*a*c)) < 0:
    pointer.goto(MIDDLEX,MIDDLEY)
    pointer.write("No Intersection!", align="center", font=("Arial", 16, "normal"))
# One intersection
elif (b**2 - (4*a*c)) == 0:
    pointer.goto(MIDDLEX, MIDDLEY)
    pointer.write("One Intersection!", align="center", font=("Arial", 16, "normal"))
    # Two intersections
# (b**2 - (4*a*c)) > 0
else:
    if (alpha1 > 1 or alpha1 < 0) and (alpha2 > 1 or alpha2 < 0):
        pointer.goto(MIDDLEX, MIDDLEY)
        pointer.write("No Intersection!", align="center", font=("Arial", 16, "normal"))
    elif (alpha1 > 1 or alpha1 < 0) or (alpha2 > 1 or alpha2 < 0):
        pointer.goto(MIDDLEX, MIDDLEY)
        pointer.write("One Intersection!", align="center", font=("Arial", 16, "normal"))
    else:
        pointer.goto(MIDDLEX, MIDDLEY)
        pointer.write("Two Intersection!", align="center", font=("Arial", 16, "normal"))

screen.exitonclick()

