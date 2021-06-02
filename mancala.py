import numpy as np


board = np.array([[0, 4, 4, 4, 4, 4, 4, 0],[0, 4, 4, 4, 4, 4, 4, 0]])

# choose point to play from 

# player1 
y = 0 

while np.sum(board) != 0: 

    print("Where would you like to move from?")
    x = int(input())

    move = board[y][x]+1
    board[y][x] = 0

    for i in range(1, move): 
        #print(i)
        place = x + i # this is the problem
        #print(place)
        if place > 7 and y == 0: 
            y = 1
            x = 0
            place = 0
            board[y][place] += 1 
            #print("Switch to 1", board)
        elif place > 7 and y == 1: 
            y = 0
            x = 0
            place = 0
            board[y][place] += 1 
            #print("Switch to 0", board)
        else: 
            board[y][place] += 1

    print(board)


    

