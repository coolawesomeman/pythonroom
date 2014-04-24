# author: coolawesomeman

import turtle

n = 6
length = 100
angle = 180 - (180 * (n - 2) / n)
numbers = range( 5,100 )
colors = ["red", "blue" ,"green" ,"yellow" ,"pink", "magenta"]


t = turtle.Turtle()

for number in numbers:
 t.forward(number)
	   
 t.left(50)
