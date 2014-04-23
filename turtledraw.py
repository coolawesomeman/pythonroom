# author: coolawesomeman

import turtle

n = 
length = 100
angle = 180 - (180 * (n - 2) / n)
numbers = [ 1, 2, 3, 4, 5]


t = turtle.Turtle()

for number in numbers:
 t.forward(length)
 t.left(angle)
