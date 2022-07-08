import turtle
radius=turtle.numinput('Input Needed', 'Enter the radius of a circle')
turtle.circle(radius)
areal=3.14*(radius**2)
circumference=2*3.14*radius
print (f'Your radius is {radius}, your areal is {areal:.2f} and \
your circumference is {circumference:.2f}!')
