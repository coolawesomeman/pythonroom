# author: coolawesomeman

import turtle

n = 6
length = 100
angle = 180 - (180 * (n - 2) / n)
numbers = range( 1,100 )
colors = ["red", "blue" ,"green" ,"yellow" ]






t = turtle.Turtle()

for number in numbers:
	for color in colors:
		t.color(color)
		t.forward(number)
		t.left(90)
	t.left(8)