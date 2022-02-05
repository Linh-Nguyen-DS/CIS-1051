#CIS 1051
#Section 009
#Linh Nguyen

import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    file = open("data/irma.csv", 'r')
    t.penup()
    for line in file:
        words = line.split(",")
        if words[0] == "Date":
            continue
        lat = float(words[2])
        lon = float(words[3])
        wind = float(words[4])
        t.goto(lon,lat)
        t.pendown()
        if wind < 74:
            t.pensize(1)
            t.write("0")
            t.pencolor("white")
        elif 74 <= wind < 96:
            t.pensize(2)
            t.write("1")
            t.pencolor("blue")
        elif 96 <= wind < 111:
            t.pensize(3)
            t.write("2")
            t.pencolor("green")
        elif 111 <= wind < 130:
            t.pensize(4)
            t.write("3")
            t.pencolor("yellow")
        elif 130 <= wind < 157:
            t.pensize(5)
            t.write("4")
            t.pencolor("orange")
        else:
            t.pensize(6)
            t.write("5")
            t.pencolor("red")
        print(words, sep = "\t")

if __name__ == "__main__":
    irma()
