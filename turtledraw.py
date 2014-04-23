# author: coolawesomeman

import turtle

n = 6
length = 100
angle = 180 - (180 * (n - 2) / n)
numbers = range( 0,n )
colors = ["red", "blue" ,"green" ,"yellow" ,"pink", "magenta"]


t = turtle.Turtle()

for number in numbers:
	for color in colors:

	    t.color(color)
	    t.forward(100)
	    t.left(175)
