# Giwon Kim. Class of 2019
# Mini Project 4.

# Full documentation of the module can be found at
# https://docs.python.org/3.6/library/turtle.html

import turtle     # Allows us to use all function in turtle module
import random     # In order to create a minefield

# Basic initialization of the screen and the drawing turtle object
wn = turtle.Screen()    # Creates a screen object called 'wn'
wn.setworldcoordinates(0, -60, 300, 300) # Sets the lowerleft corner(0, -60) and upper-right corner (300, 300)
wn.bgcolor('grey')      # Starts with grey background
t = turtle.Turtle()     # Creates the turtle called 't'
t.hideturtle()          # Hides the appearance of the Turtle
t.speed(0)              # Turtle has no extra delay in carrying out its performance
turtle.tracer(0,0)      # The screen has no extra delay in rendering the graphics

# --------------------------------------------------------------------------#
# Your global variables and constants go below.
# --------------------------------------------------------------------------#
# This lis of mines is for mine()
minelist = []
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])
minelist.append([True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,])

# Stores already revealed-square coordinates in a list 'revaledsqrlist'
# This is for leftclickfn(x, y)
revealed_sqr_list = []

# Creat a list of coordinate of a square with a red "X"
# This is for rightclickfn(x, y)
coordlist = []

# --------------------------------------------------------------------------#
# Your functions go below.
# --------------------------------------------------------------------------#
# A function, gridsquare(), provides a grid of 15-by-15 squares that are 20 pixels long.
def gridlines():
    # Draw the vertical lines with 20 pixels long line spacing.
    x = 0
    # Since we need a grid of 15-by-15 squares that are 20 pixels long.
    # the total length is 300
    while x <= 300:
        t.penup()
        # Set the orientation of the turtle to the north.
        t.setheading(90)
        t.goto(x, 0)
        t.pendown()
        t.forward(300)
        # Move rightwards by 20 pixels to draw next vertical line.
        x = x + 20
    # Draw the horizontal lines with 20 pixels long line spacing.
    y = 0
    # Since we need a grid of 15-by-15 squares that are 20 pixels long.
    # the total length is 300
    while y <= 320: # But somehow if I set y<=300, then there are only 15 horizontal lines.
        t.penup()
        # Set the orientation of the turtle to the east.
        t.setheading(0)
        t.goto(0, y)
        t.pendown()
        t.forward(300)
        # Move upwards by 20 pixels to draw next vertical line.
        y = y + 20

# Takes a coorninate (x, y) and a color, which is the clicked coordinate and
# white or red color.
# fills a selected grid square with white or red color.
def coloring(x, y, chosencolor) :
    t.penup()
    # Set the orientation of the turtle to the east.
    t.setheading(0)
    # Since it's a set of 20-by-20 grid squares
    # By using x // 20 and y // 20, we can find the place of a selected square
    # so that it can fill the square with a selected color.
    gridx = x // 20
    gridy = y // 20
    # Going to the lower left corner of the selected square to fill up the color.
    t.goto(gridx * 20, gridy * 20)
    t.pendown()
    t.pencolor("black")
    t.fillcolor(chosencolor)
    t.begin_fill()
    for k in range(0, 4) :
        t.forward(20)
        t.left(90)
    t.end_fill()

# Each run of the program randomly generates a minefield
def mine() :
    for xcoord in range(0, 15) :
        for ycoord in range(0, 15) :
            # Setting the probability to 0.15
            # Whether to place a mine on a square is less than 0.15
            minelist[xcoord][ycoord] = (0.15 > random.random())
    return minelist   # True is less than 0.15
                      # False is more than 0.15

# Returns a list of surrounding squares' coordinates
def neighborsquares(x, y) :
    neighborsquarelist = []
    gridx = int(x // 20) * 20
    gridy = int(y // 20) * 20
    # Northernmost row
    if 0 < gridx < 280 and gridy == 280 :
        surrounding = ((-20, 0), (20, 0), (-20, -20), (0, -20), (20, -20))
                    # surrounding = ((-20  , 0),           (20  , 0),
                    #                (-20, -20), (0, -20), (20, -20))
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    # Easternmost column
    elif gridx == 280 and 0 < gridy < 280 :
        surrounding = ((-20, 20), (0, 20), (-20, 0), (-20, -20), (0, -20))
                    # surrounding = ((-20 , 20), (0 , 20),
                    #                (-20  , 0),
                    #                (-20, -20), (0, -20))
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    # Westernmost column
    elif (gridx == 0) and (0 < gridy < 280) :
        surrounding = ((0, 20), (20, 20), (20, 0), (0, -20), (20, -20))
                    # surrounding = ((0 , 20), (20 , 20),
                    #                          (20  , 0),
                    #                (0, -20), (20, -20))
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    # Southernmost row
    elif 0 < gridx < 280 and gridy == 0 :
        surrounding = ((-20, 20), (0, 20), (20, 20), (-20, 0), (20, 0))
                    # surrounding = ((-20 , 20), (0 , 20), (20 , 20),
                    #                (-20  , 0),           (20  , 0))
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    # NorthEast vertex
    elif gridx == 280 and gridy == 280 :
        surrounding = ((-20, 0), (-20, -20), (0, -20))
                    # surrounding = ((-20  , 0),
                    #                (-20, -20), (0, -20))
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    # NorthWest vertex
    elif gridx == 0 and gridy == 280 :
        surrounding = ((20, 0), (0, -20), (20, -20))
                    # surrounding = (          (20  , 0)
                    #                (0, -20), (20, -20))
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    # SouthEast vertex
    elif gridx == 280 and gridy == 0 :
        surrounding = ((-20, 20), (0, 20), (-20, 0))
                    # surrounding = ((-20 , 20), (0 , 20)
                    #                (-20  , 0)         )
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    # SouthWest vertex
    elif gridx == 0 and gridy == 0 :
        surrounding = ((0, 20), (20, 20), (20, 0))
                    # surrounding = ((0 , 20), (20 , 20),
                    #                          (20  , 0))
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    else :
        surrounding = ((-20, 20), (0, 20), (20, 20), (-20, 0), (20, 0), (-20, -20), (0, -20), (20, -20))
                    # surrounding = ((-20 , 20), (0 , 20), (20 , 20),
                    #                (-20  , 0),           (20  , 0),
                    #                (-20, -20), (0, -20), (20, -20))
        for (surr_row, surr_column) in surrounding :
            neighborsquarelist.append((gridx + surr_row, gridy + surr_column))
    return neighborsquarelist


# If a revealed square has no mine on it, it should specify the number of mines
# among its neighbors (if there are no neighboring mines, leave it white blank)
def numneighbormines(x, y, minelist1) :
    neighborsquarelist = neighborsquares(x, y)
    minenum = 0
    for (coordx, coordy) in neighborsquarelist :
        if minelist1[int(coordx//20)][int(coordy//20)] == True :
            minenum = minenum + 1
    return minenum

# A left click on a square that has no neighboring mines reveals not just
# that square, but all neighboring squares and doesn't stop until it reveals
# squares that do have neighboring mines.
# Returns a list of coordinates of squares that do have neighboring mines.
def cascading_reveal(x, y) :
    # Gets coordinates of neighbor squares
    NeighborsCoords = neighborsquares(x, y)
    # Gets the number of neighboring mines
    minenum = numneighbormines(x, y, minelist1)
    gridx = int(x//20) * 20
    gridy = int(y//20) * 20
    # Base case
    if minenum > 0 :
        cascadelist = []
        cascadelist.append((gridx, gridy)) # Stores all coordinates of squares that do have neighboring mines.
        return cascadelist
    # Recursive case
    else :
        cascadelist = []
        cascadelist.append((gridx, gridy))
        for (i, j) in NeighborsCoords :
            if (i, j) not in confirmlist : # confirmlist is a list of examined coordinates,
                confirmlist.append((i, j)) # so that it can continue to checking all neighbors without repeating to check the same one.
                cascadelist = cascadelist + cascading_reveal(i, j)
        return cascadelist

# When the user left click a mine, then write a sign "You have lost!"
def lostsign() :
    t.penup()
    t.goto(90, -40)
    t.pendown()
    t.write("You have lost!", font=('Arial', 40, "bold"))

# When the user successfully finish the game without clicking a mine, then write a sign "Congrats, you won!"
def winsign() :
    t.penup()
    t.goto(60, -40)
    t.pendown()
    t.write("Congrats, you won!", font=('Arial', 40, "bold"))

# Returns a list of the total number of squares that have no mine.
# So that I can notice when the user successfully finish the game without clicking a mine
def white_square_num(minelist1) :
    whitesquareslist = []
    for xcoord in range(0, 15) :
        for ycoord in range(0, 15) :
            if minelist1[xcoord][ycoord] == False :
                whitesquareslist.append((xcoord, ycoord))
    return whitesquareslist

# Provides a Reset button
class drawResetButton :
    """ Represents the reset button """
    def __init__(self, xl, yl, xu, yu) :
        self.coord = (xl, yl, xu, yu)

    # draws a reset button
    def drawbutton(self) :
        t.penup()
        t.goto(self.coord[0], self.coord[1]) # go to lower left corner
        t.setheading(90) # to the North
        t.pendown()
        t.pencolor('black')
        t.fillcolor('yellow')
        t.begin_fill()
        for k in range(4) :
            t.forward(30)
            t.right(90)
        t.end_fill()

    # In order to write a letter "Reset" in the box
    def write_reset(self) :
        t.penup()
        t.goto(245, -35)
        t.pendown()
        t.write('Reset', font=("Arial", 18, "bold"))


# What to do if the user left-clicks on the coordinates (x,y)
def leftclickfn(x, y) :
    if x > 0 and y > 0 :
        gridx = int(x // 20)
        gridy = int(y // 20)
        # if the probability is less than 0.15 (True), then it has a mine
        if minelist1[gridx][gridy] == True :
            # Fills with a red color
            coloring(x, y, 'red')
            # Append revealed square coordinate
            # to mark a red "X" only on unrevealed grey squares
            revealed_sqr_list.append((gridx, gridy))
            # Shows up a sign "You have lost!"
            lostsign()
        # if the probability is more than 0.15 (False), then it has no mine
        else :
            minenum = numneighbormines(x, y, minelist1)
            if minenum == 0 :
                # Confirmlist is a list of examined coordinates,
                # so that it can continue to checking all neighbors without repeating to check the same one.
                global confirmlist # Sets confirmlist as a global variable, so that it can be used in entire codes.
                confirmlist = []
                cascadelist = cascading_reveal(x, y)
                for (i, j) in cascadelist :
                    # Fills with a white color
                    coloring(i, j, 'white')
                    gridi = int(i//20)
                    gridj = int(j//20)
                    # Append revealed square coordinate
                    # to mark a red "X" only on unrevealed grey squares
                    revealed_sqr_list.append((gridi, gridj))
                    newminenum = numneighbormines(i, j, minelist1)
                    if not newminenum == 0 :
                        t.penup()
                        t.goto(gridi * 20 + 7.5, gridj * 20 + 5)
                        t.pendown()
                        t.pencolor('black')
                        t.write(newminenum, font=("Arial", 18))
            else :
                # Fills with a white color
                coloring(x, y, 'white')
                # Append revealed square coordinate
                # to mark a red "X" only on unrevealed grey squares
                revealed_sqr_list.append((gridx, gridy))
                t.penup()
                t.goto(gridx * 20 + 7.5, gridy * 20 + 5)
                t.pendown()
                t.pencolor('black')
                t.write(minenum, font=("Arial", 18))

    # To display a sign "Congrats, you won!", when the user finds out all white squares successfully.
        all_non_mines = white_square_num(minelist1)
        # Finds out if all elements of all_non_mines are there in revealed_sqr_list
        if set(all_non_mines).issubset(set(revealed_sqr_list)) :
            winsign() # Displays a sign "Congrats, you won!"

    # If the user left click the "Reset" button, then play another game
    if 240 < x and x < 270 and -45 < y and y < -15 :
        # Cover the previous game with a grey square.
        t.penup()
        t.setheading(0)
        t.goto(0, 0)
        t.pendown
        t.pencolor('black')
        t.fillcolor('grey')
        t.begin_fill()
        for k in range(0, 4) :
            t.forward(300)
            t.left(90)
        t.end_fill()
        # Erase the sentence "You have lost!" for a new game
        t.penup()
        t.setheading(0)
        t.goto(60, -40)
        t.pendown
        t.pencolor('black')
        t.fillcolor('grey')
        t.begin_fill()
        for k in range(0, 4) :
            t.forward(177)
            t.left(90)
        t.end_fill()
        # Provides a 15-by-15 grid squares
        gridlines()
        # Calling a new random minelist
        minelist2 = mine()
        # Removes the contents from the list for a new game
        del revealed_sqr_list[:]
        # Removes the contents from the list for a new game
        del coordlist[:]

# What to if the user right-clicks on the coordinates (x,y)
# A right click on an unrevealed square places a red "X" to mark a possible mine.
# Another right click takes the "X" off.
def rightclickfn(x, y):
    gridx = int(x // 20)
    gridy = int(y // 20)
    # To mark a red "X" only on unrevealed grey squares
    if (gridx, gridy) not in revealed_sqr_list :
        # If the squre already had a red "X", then remove it with another right click
        if (gridx * 20, gridy * 20) in coordlist :
            # Fills the grey square to take the red "X" off
            coloring(x, y, 'grey')
            # Remove the coordinate from the list "coordlist",
            # so that a user can mark it again with a red "X".
            coordlist.remove((gridx * 20, gridy * 20))
        # Mark with a red "X" to a possible mine square.
        elif x > 0 and y > 0 :
            t.penup()
            t.goto(gridx * 20 + 7.5, gridy * 20 + 5)
            t.pendown()
            t.pencolor("red")
            t.write('X', font=("Arial", 18, "bold"))
            # Append the coordinate to the list "coordlist"
            coordlist.append((gridx * 20, gridy * 20))

# --------------------------------------------------------------------------#
# Your main code goes below.
# --------------------------------------------------------------------------#
# Generates a grid lines
gridlines()

# Calling a new random minelist
minelist1 = mine()

# Provides a "Reset" button
drawresetbtn = drawResetButton(240, -45, 210, -10)
drawresetbtn.drawbutton()
drawresetbtn.write_reset()

wn.onclick(leftclickfn, 1) # if the user left-clicks, call leftclickfn
wn.onclick(rightclickfn, 2) # if user right-clicks.
wn.mainloop()  # Wait for user to click somewhere on the screen object
