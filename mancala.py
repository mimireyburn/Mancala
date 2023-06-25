#Define the mancala board
board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]

#Define player's turn
player = 0 #0 indicates player 1 and 1 indicates player 2
player_bank = [6, 13] 
opponent_bank = [13,6]

# Find slot opposite the current one on the board
def getOpposite(player, current_slot): 
    if player == 0 and current_slot < 6: 
        opposite_cell = 6 + (6 - current_slot)
    elif player == 1 and current_slot > 6: 
        opposite_cell = 6 - (current_slot - 6)
    else: 
        opposite_cell = None
    return opposite_cell

# Print the board in traditional layout
def printBoard(board): 
    player_one = "|   |"
    for slot in range(7): 
        player_one += " " + str(board[slot]) + " |"

    player_two = " "  
    for slot in reversed(range(7,14)): 
        player_two += " " + str(board[slot]) + " |"

    graphic_board = player_two + "\n" + player_one
    print(graphic_board)

# Check if anyone has one 
def checkWinner(board): 
    if sum(board[0:6]) == 0 or sum(board[7:13]) == 0:
        print("Game over!")
        for slot in range(0,6): 
            board[6] += board[slot]
            board[slot] = 0
        for slot in range(7,13): 
            board[13] += board[slot]
            board[slot] = 0
        if board[6] > board[13]: 
            print("Player 1 Wins!")
            return True
        elif board[6] < board[13]: 
            print("Player 2 Wins!")
            return True
        else: 
            print("Player 1 and Player 2 Draw!")
            return True
    else:
        return False


#Define gameplay function
def play_mancala(board, player):
    
    while checkWinner(board) == False: 

        #Display current board
        print("Current Mancala Board")
        printBoard(board)

        try: 
            #Ask current player to select a slot 
            current_slot = int(input("Player "+str(player+1)+": Select a slot to sow from (1-6): "))
            current_slot -= 1 #adjusting for list index (1-6 --> 0-5)

            # If player 2, position if 7 further in list
            if player == 1: 
                current_slot = current_slot + 7

            #Check slot selection
            if board[current_slot] == 0:
                print("Error: There are no stones in this slot.")
                return play_mancala(board, player)
            else: 
                #sow stones
                stones_in_hand = board[current_slot]
                board[current_slot] = 0

            # sow stones
            for stone in range(1, stones_in_hand+1):
                # dont add to opponent bank 
                if current_slot + stone == opponent_bank[player]: 
                    current_slot += 1
                # check if past end of the list
                if current_slot + stone > 13:
                    if (current_slot+stone)-14 == opponent_bank[player]: 
                        current_slot += 1
                    board[(current_slot+stone)-14] += 1
                    last_slot = (current_slot+stone)-13
                # lay stones
                else: 
                    board[current_slot + stone] += 1
                    last_slot = current_slot + stone

            # get cell opposite where last stone was places
            opposite_cell = getOpposite(player, last_slot)

            # check if player gets another go
            if last_slot == player_bank[player]:
                play_mancala(board, player)

            # check if player can capture
            elif board[last_slot] == 1 and opposite_cell != None and board[opposite_cell] > 0: 
                board[player_bank[player]] += board[opposite_cell] + 1
                board[opposite_cell] = 0 
                board[last_slot] = 0 
            
            # Swap players
            play_mancala(board, not player)

        # Handle incorrect / accidental inputs
        except ValueError: 
            print("******** Choose a value from 1-6 ********")
            play_mancala(board, player)

play_mancala(board, player)


        
    