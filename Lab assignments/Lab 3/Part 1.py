import turtle

ring = turtle.Turtle()

ring.pensize(5)

for i in range(5):
    ring.penup()
    if i==0:
        ring.color("blue")
        ring.setpos(-50,50)
    elif i==1:
        ring.color("black")
        ring.setpos(65,50)
    elif i==2:
        ring.color("red")
        ring.setpos(180,50)
    elif i==3:
        ring.color("orange")
        ring.setpos(7.5,0)
    elif i==4:
        ring.color("green")
        ring.setpos(122.5,0)
    ring.pendown()
    ring.circle(50)

for i in range(4):
    ring.penup()
    if i==0:
        ring.setpos(-50,50)
        ring.right(180)
        ring.color("blue")
        ring.pendown()
        ring.circle(-50,345)
    elif i==1:
        ring.setpos(65,50)
        ring.color("black")
        ring.right(15)
        ring.pendown()
        ring.circle(-50,80)
    elif i==2:
        ring.setpos(180,50)
        ring.color("red")
        ring.left(80)
        ring.pendown()
        ring.circle(-50,80)
    elif i==3:
        ring.setpos(65,150)
        ring.color("black")
        ring.right(100)
        ring.pendown()
        ring.circle(-50,150)
