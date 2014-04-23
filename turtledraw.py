# author: coolawesomeman

import turtle

n = 
length = 100
angle = 180 - (180 * (n - 2) / n)
numbers = range( 1,101)


t = turtle.Turtle()

for number in numbers:
 t.forward(length)
 t.left(angle)
