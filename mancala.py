import numpy as np

board = np.array([[0, 4, 4, 4, 4, 4, 4, 0],[0, 4, 4, 4, 4, 4, 4, 0]])

# choose point to play from 

row = 0 

def swap_player(row): 
    if row == 1: 
        row = 0
    else: 
        row = 1
    return row

def something(row, board):
    print("Which place would you like to move from?") 
    start = int(input()) # choose place
    player = row
    print("What player is it now?", player)
    moves = board[row][start] + 1   # scale from index
    board[row][start] = 0
    # print("moves:", moves)
    for i in range(1,moves): # move pieces from spot
        # print("i:", i)

        place = start + i 
        # print("place:", place)

        if place > 7 and row == 0: 
            board[1][place-6] += 1 # switch to other side

        if place > 7 and row == 1: 
            board[0][place-6] += 1

        elif place <= 7: 
            # print(row, place)
            board[row][place] += 1

    else: 
        print(board)
        print("player", player)
        
        row = swap_player(player)
        print("row", row)
        
    return board, player

while np.sum(board) != 0:
    something(row, board)

# while np.sum(board) != 0: 

#     print("Which place would you like to move from?")
#     x = int(input())

#     move = board[y][x]+1
#     board[row][x] = 0
#     place = x + 1

#     for i in range(move): 
#         #print(i)
#         place = x + i + 1 # this is the problem
#         #print(place)
#         if place > 7 and y == 0: 
#             y = 1
#             x = 0
#             p
#             board[y][1] += 1 
#             #print("Switch to 1", board)
#         elif place > 7 and y == 1: 
#             y = 0
#             x = 0
#             board[y][1] += 1 
#             #print("Switch to 0", board)
#         else: 
#             board[y][place] += 1
#     else:

#         print(board)