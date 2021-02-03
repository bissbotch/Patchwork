from graphics import *

def linspace(start, stop, n):
    step = (stop - start) / n
    return [start + step * i for i in range(n)]

#drawing the first patch
def firstPatch(win, x, y, colour, size):

    radius = size/10

    for n, j in enumerate(linspace(y, y+size, 5)):
        i = x

        for _ in range(4):

            #draws a circle only
            if n % 2 == 0:

                circle = Circle(Point(i+radius, j+radius), radius)
                circle.draw(win)
                circle.setFill(colour)
                circle.setOutline(colour)

                n += 1
                i += radius * 2

            #draws two circles and a rectangle
            else:

                #first circle
                circle = Circle(Point(i+radius, j+radius), radius)
                circle.draw(win)
                circle.setFill(colour)
                circle.setOutline(colour)

                #second circle
                circle = Circle(Point(i+radius*2, j+radius), radius)
                circle.draw(win)
                circle.setFill(colour)
                circle.setOutline(colour)

                #the middle square
                square = Rectangle(Point(i+radius, j),
                                   Point(i+radius*2, j+radius*2))
                square.draw(win)
                square.setFill(colour)
                square.setOutline(colour)

                n += 1
                i += radius * 3

#draws final patch
def finalPatch(win, x, y, colour, size):

    num = size // 10

    for a in linspace(0, size, 10):

        #draws top half
        line = Line(Point(x+a, y), Point(x+size, y+a+num))
        line.draw(win)
        line.setFill(colour)

        #draws bottom half
        line = Line(Point(x, y+a), Point(x+a+num, y+size))
        line.draw(win)
        line.setFill(colour)

def main():

    #gets number of patches
    while True:

        numPatches = input('Enter the patchwork size (5 or 7): ').strip()

        if numPatches in ('5', '7'):
            numPatches = int(numPatches)
            break

        print('Please enter a valid size.')

    #valid colours list
    valid = ['red', 'blue', 'cyan', 'green', 'magenta', 'orange']
    colors = []

    while True:

        for i in range(3):

            while True:
                colour = input(f'Enter a colour {i+1}: ')
                colour = colour.strip()

                if colour in valid:
                    colors.append(colour)
                    break

                print('Please enter a valid colour:', valid)

        if len(set(colors)) < 2:
            print('Please chose at least 2 different colours.')
            colors = []
        else:
            break

    #creates the window
    side = 100
    size = side * numPatches

    win = GraphWin('Patchwork', size, size)
    coordinates = linspace(0, size, numPatches)

    #draws the patches
    for i in range(numPatches):
        for j in range(numPatches):

            x, y = coordinates[i], coordinates[j]

            #vertical border
            if y == 0:
                line = Line(Point(x, y), Point(x, y+size))
                line.draw(win)
                line.setFill("black")

            #horizontal border
            if x == 0:
                line = Line(Point(x, y), Point(x+size, y))
                line.draw(win)
                line.setFill("black")

            #gets colour of the patch
            if 0 < i < numPatches-1:

                if j < numPatches // 2:
                    print("column i=",i)
                    print("row j=",j)
                    colour = colors[1]
                    print(colour)
                elif j > numPatches // 2:
                    print("column i=",i)
                    print("row j=",j)
                    colour = colors[2]
                    print(colour)
                else:
                    print("column i=",i)
                    print("row j=",j)
                    colour = colors[0]
                    print(colour)


            else:
                colour = colors[0]
                print(colour, "the else")

            #draws final patch
            if (i+j) % 2 == 0:
                finalPatch(win, x, y, colour, side)

            #draws first patch
            else:
                firstPatch(win, x, y, colour, side)

main()
