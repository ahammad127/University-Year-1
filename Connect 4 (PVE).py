'''To run this programme you need to import numpy, random and sys. The functions that will be used are try statements (which try code and help block errors), for loops, while loops, if statements, making tuples and making arrays.'''
import numpy as np
from random import randint
import sys
end = False
'''Line 3 defines that the end of the game has not been reached.'''
gridtuple = [['O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O']]
Grid = np.array(gridtuple)
'''Lines 5 and 6 form the grid for the game.'''
print Grid
across = [0, 1, 2, 3]
down = [0, 1, 2]
def inp(r0):
    r0 = raw_input("Player's move - pick a number between 1 and 7: ")
    '''Line 10 allows an input.'''
    r1 = 4
    '''r1 is just a variable that I have to define so I can carry out the next piece of code. It doesn't have to be 4, it doesn't even have to be a number. It just has to be a defined variable.'''
    try:
        r1 = float(r0)
    except ValueError:
        print "Pick a NUMBER between 1 and 7!"
        r1 = float(inp(r0))
    '''Lines 16 to 20 check if it is possible to convert the string input to a float. If it can't convert the input then it prompts the user for a different input, as their original input couldn't have been a number, or else it would have converted it to a float.'''
    while r1 < 0 or r1 > 7:
        print "The number must be between 1 and 7!"
        r1 = float(inp(r0))
    return r1
'''Lines 22 to 24 check that the input is between 1 and 7 (because it is a 7 by 6 grid) using a while loop.'''
'''Line 25 returns the input as a float.'''
def altinp(r0):
    r0 = raw_input("Column full - choose another number: ")
    r1 = 4
    try:
        r1 = float(r0)
    except ValueError:
        print "Choose another NUMBER!"
        r1 = float(altinp(r0))
    while r1 < 0 or r1 > 7:
        print "The number must be between 1 and 7!"
        r1 = float(altinp(r0))
    return r1
'''The altinp() function does basically the same as the inp() function except it prompts the user for another input when the user tries to input a piece into a full column.'''
def intcheck(r0):
    global r1 #global r1 is the global variable r1, which will be the float that was returned from the inp() function.
    r = int(r1) #The variable r is r1 converted to an integer.    
    while abs(r - r1) != 0:
        print "The number must be a whole number!"
        r1 = inp(r0)
        r = int(r1)
    return r
'''The function intcheck() checks that the input is an integer by seeing if the difference between r and r1 is 0. If the difference is not 0 then the user is prompted for another input.'''
def altintcheck(r0):
    global r4
    r = int(r4)
    while abs(r - r4) != 0:
        print "The number must be a whole number!"
        r4 = altinp(r0)
        r = int(r4)
    return r
print "You will play as the red piece" 
while end == False: #This loop allows the game to keep running until a winner is declared or a draw is reached.
    yp = 5 #yp is a variable that defines the y 'axis' of the grid. It is 5 because all of the pieces will 'fall' onto y-postion 5 first.
    r0 = 100 #r0 is another example of a variable that needs only to be defined to be used for later code.
    r1 = inp(r0) #The input from the user gets stored as r1.
    r = intcheck(r1) #The integer value of the input is stored as r.
    while Grid[yp][r - 1] != 'O': #This while loop makes sure that pieces are stacked and that pieces do not replace eachother.
        ypp = yp
        if ypp == 0:
            r1 = altinp(r0)
            r = intcheck(r1)
            yp2 = 5
            '''The if statement prompts for an alternative input if the column is full and makes sure it is an integer.'''
            while Grid[yp2][r - 1] != 'O':
                yp2 = yp2 - 1
                yp = yp2 + 1
                '''This while loops makes sure that the alternative input is stacked on top of a piece and that it doesn't just replace the piece.'''
        yp = yp - 1
    Grid[yp][r - 1] = 'R' #This line puts the user's input on the grid
    print Grid
    for r in across: #This for loop looks for a horizontal 4 in a row in the bottom row of the grid
        yp = 5
        s = r + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[yp][s] == 'R' and Grid[yp][t] == 'R' and Grid[yp][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        '''The above if statement highlights the winning 4 in a row (if there is one), labels the winner and terminates the programme.'''
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for r in across: #This for loop looks for a horizontal 4 in a row in the 5th row of the grid
        yp = 4
        s = r + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[yp][s] == 'R' and Grid[yp][t] == 'R' and Grid[yp][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for r in across: #This for loop looks for a horizontal 4 in a row in the 4th row of the grid
        yp = 3
        s = r + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[yp][s] == 'R' and Grid[yp][t] == 'R' and Grid[yp][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for r in across: #This for loop looks for a horizontal 4 in a row in the 3rd row of the grid
        yp = 2
        s = r + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[yp][s] == 'R' and Grid[yp][t] == 'R' and Grid[yp][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for r in across: #This for loop looks for a horizontal 4 in a row in the 2nd row of the grid
        yp = 1
        s = r + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[yp][s] == 'R' and Grid[yp][t] == 'R' and Grid[yp][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for r in across: #This for loop looks for a horizontal 4 in a row in the top row of the grid
        yp = 0
        s = r + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[yp][s] == 'R' and Grid[yp][t] == 'R' and Grid[yp][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down: #This loop look 4 a vertical 4 in a row in the 1st column of the grid
        r = 0
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[s][r] == 'R' and Grid[t][r] == 'R' and Grid[u][r] == 'R':
            Grid[yp][r] = 'W'
            Grid[s][r] = 'W'
            Grid[t][r] = 'W'
            Grid[u][r] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down: #This loop look 4 a vertical 4 in a row in the 2nd column of the grid
        r = 1
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[s][r] == 'R' and Grid[t][r] == 'R' and Grid[u][r] == 'R':
            Grid[yp][r] = 'W'
            Grid[s][r] = 'W'
            Grid[t][r] = 'W'
            Grid[u][r] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down: #This loop look 4 a vertical 4 in a row in the 3rd column of the grid
        r = 2
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[s][r] == 'R' and Grid[t][r] == 'R' and Grid[u][r] == 'R':
            Grid[yp][r] = 'W'
            Grid[s][r] = 'W'
            Grid[t][r] = 'W'
            Grid[u][r] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down: #This loop look 4 a vertical 4 in a row in the 4th column of the grid
        r = 3
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[s][r] == 'R' and Grid[t][r] == 'R' and Grid[u][r] == 'R':
            Grid[yp][r] = 'W'
            Grid[s][r] = 'W'
            Grid[t][r] = 'W'
            Grid[u][r] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down: #This loop look 4 a vertical 4 in a row in the 5th column of the grid
        r = 4
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[s][r] == 'R' and Grid[t][r] == 'R' and Grid[u][r] == 'R':
            Grid[yp][r] = 'W'
            Grid[s][r] = 'W'
            Grid[t][r] = 'W'
            Grid[u][r] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down: #This loop look 4 a vertical 4 in a row in the 6th column of the grid
        r = 5
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[s][r] == 'R' and Grid[t][r] == 'R' and Grid[u][r] == 'R':
            Grid[yp][r] = 'W'
            Grid[s][r] = 'W'
            Grid[t][r] = 'W'
            Grid[u][r] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down: #This loop look 4 a vertical 4 in a row in the 7th column of the grid
        r = 6
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][r] == 'R' and Grid[s][r] == 'R' and Grid[t][r] == 'R' and Grid[u][r] == 'R':
            Grid[yp][r] = 'W'
            Grid[s][r] = 'W'
            Grid[t][r] = 'W'
            Grid[u][r] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 2
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp + 1
        tp = sp + 1
        up = tp + 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
            r = r + 1
            s = s + 1
            t = t + 1
            u = u + 1
    yp = 1
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp + 1
        tp = sp + 1
        up = tp + 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
            r = r + 1
            s = s + 1
            t = t + 1
            u = u + 1
    yp = 0
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp + 1
        tp = sp + 1
        up = tp + 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
            r = r + 1
            s = s + 1
            t = t + 1
            u = u + 1
    '''The above for loops between lines 299 and 358 look for diagonal 4 in a rows throughout the grid'''
    yp = 5
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 4
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 3
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 2
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 1
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 0
    for r in across:
        s = r + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][r] == 'R' and Grid[sp][s] == 'R' and Grid[tp][t] == 'R' and Grid[up][u] == 'R':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Red wins!"
            sys.exit("Game over")
        r = r + 1
        s = s + 1
        t = t + 1
        u = u + 1
    '''The above for loops between lines 359 and 479 look for diagonal 4 in a rows (in the other diagonal direction) throughout the grid'''
    yp = 5  
    print "Computer's move"
    y = randint(0,6) #The computer's chosen piece will be a random number.
    while Grid[yp][y] != 'O': 
        yp = yp - 1
    Grid[yp][y] = 'Y'
    '''The above while loop stacks the pieces'''
    print Grid
    for y in across:
        yp = 5
        s = y + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[yp][s] == 'Y' and Grid[yp][t] == 'Y' and Grid[yp][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for y in across:
        yp = 4
        s = y + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[yp][s] == 'Y' and Grid[yp][t] == 'Y' and Grid[yp][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for y in across:
        yp = 3
        s = y + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[yp][s] == 'Y' and Grid[yp][t] == 'Y' and Grid[yp][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for y in across:
        yp = 2
        s = y + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[yp][s] == 'Y' and Grid[yp][t] == 'Y' and Grid[yp][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for y in across:
        yp = 1
        s = y + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[yp][s] == 'Y' and Grid[yp][t] == 'Y' and Grid[yp][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for y in across:
        yp = 0
        s = y + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[yp][s] == 'Y' and Grid[yp][t] == 'Y' and Grid[yp][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[yp][s] = 'W'
            Grid[yp][t] = 'W'
            Grid[yp][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down:
        y = 0
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[s][y] == 'Y' and Grid[t][y] == 'Y' and Grid[u][y] == 'Y':
            Grid[yp][y] = 'W'
            Grid[s][y] = 'W'
            Grid[t][y] = 'W'
            Grid[u][y] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down:
        y = 1
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[s][y] == 'Y' and Grid[t][y] == 'Y' and Grid[u][y] == 'Y':
            Grid[yp][y] = 'W'
            Grid[s][y] = 'W'
            Grid[t][y] = 'W'
            Grid[u][y] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down:
        y = 2
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[s][y] == 'Y' and Grid[t][y] == 'Y' and Grid[u][y] == 'Y':
            Grid[yp][y] = 'W'
            Grid[s][y] = 'W'
            Grid[t][y] = 'W'
            Grid[u][y] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1    
    for yp in down:
        y = 3
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[s][y] == 'Y' and Grid[t][y] == 'Y' and Grid[u][y] == 'Y':
            Grid[yp][y] = 'W'
            Grid[s][y] = 'W'
            Grid[t][y] = 'W'
            Grid[u][y] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down:
        y = 4
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[s][y] == 'Y' and Grid[t][y] == 'Y' and Grid[u][y] == 'Y':
            Grid[yp][y] = 'W'
            Grid[s][y] = 'W'
            Grid[t][y] = 'W'
            Grid[u][y] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down:
        y = 5
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[s][y] == 'Y' and Grid[t][y] == 'Y' and Grid[u][y] == 'Y':
            Grid[yp][y] = 'W'
            Grid[s][y] = 'W'
            Grid[t][y] = 'W'
            Grid[u][y] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    for yp in down:
        y = 6
        s = yp + 1
        t = s + 1
        u = t + 1
        if Grid[yp][y] == 'Y' and Grid[s][y] == 'Y' and Grid[t][y] == 'Y' and Grid[u][y] == 'Y':
            Grid[yp][y] = 'W'
            Grid[s][y] = 'W'
            Grid[t][y] = 'W'
            Grid[u][y] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        yp = yp + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 2
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp + 1
        tp = sp + 1
        up = tp + 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
            y = y + 1
            s = s + 1
            t = t + 1
            u = u + 1
    yp = 1
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp + 1
        tp = sp + 1
        up = tp + 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
            y = y + 1
            s = s + 1
            t = t + 1
            u = u + 1
    yp = 0
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp + 1
        tp = sp + 1
        up = tp + 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][r] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
            y = y + 1
            s = s + 1
            t = t + 1
            u = u + 1
    yp = 5
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 4
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 3
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 2
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 1
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
    yp = 0
    for y in across:
        s = y + 1
        t = s + 1
        u = t + 1
        sp = yp - 1
        tp = sp - 1
        up = tp - 1
        if Grid[yp][y] == 'Y' and Grid[sp][s] == 'Y' and Grid[tp][t] == 'Y' and Grid[up][u] == 'Y':
            Grid[yp][y] = 'W'
            Grid[sp][s] = 'W'
            Grid[tp][t] = 'W'
            Grid[up][u] = 'W'
            print Grid
            print "Yellow wins!"
            sys.exit("Game over")
        y = y + 1
        s = s + 1
        t = t + 1
        u = u + 1
        '''Allof the above for loops check to see if the yellow piece has won in the same way that the red pieces are checked.'''