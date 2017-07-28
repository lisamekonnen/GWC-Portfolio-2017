from turtle import *
import math

### Name of the Turtle
t = Turtle()

### Set Up Screen and Starting Position.
setup(1000,800)
t.setposition(0, 0)

### Asking Client (User) About The Color of Shapes
color = input('Enter the color you want: ')
print('Ok we will make a shape that color')
t.pencolor(color)

### Asking the Client (User) About How Many Sides
side = int(input('Enter the side you want: '))
print('Ok we will make a shape with that amount of sides')

### Make the Shape With Loop (Angle/Length)
for x in range(0, side):
    t.pendown()
    t.forward(100)
    angle = int(360/side)
    t.right(angle)

# Close window on click.
exitonclick()
