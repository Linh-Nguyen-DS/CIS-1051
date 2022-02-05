import turtle

poly = turtle.Turtle()

n = int(input("How many sides do you want?"))
angle = 360/n

for i in range(n):
        poly.forward(60)
        poly.right(angle)
