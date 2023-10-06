import gym 
from gym import spaces
import random

class MancalaEnv(gym.Env): 
    def __init__(self):
        super(MancalaEnv, self).__init__()
        # Initialise state and action spaces
        # State is the board and the player's turn
        # Action is the slot chosen by the current player 
        
        self.player_bank = [6, 13]
        self.opponent_bank = [13,6]

        self.action_space = spaces.Discrete(6)
        self.observation_space = spaces.Tuple((spaces.Discrete(14), spaces.Discrete(2)))

        self.info = {
            'event': None,
            'extra_info': {}
        }

        self.current_state = None
        self.reset()


    def get_valid_actions(self, board, player):
        start_slot = self.opponent_bank[player] + 1
        valid_actions = []
        for slot in range(6):
            board_slot = (slot + start_slot) % 14
            if board[board_slot] != 0:
                valid_actions.append(slot)
        return valid_actions
    

    def opposite(self, board, player, current_slot, info):
        if (player == 0 and current_slot < 6) or (player == 1 and current_slot > 6):
            opponent_cell = 12 - current_slot
            # capture stones, if avaliable
            if board[opponent_cell] != 0:
                info['extra_info']['captured_stones'] = board[opponent_cell]
                board[self.player_bank[player]] += board[opponent_cell]
                board[opponent_cell] = 0
        return board, info


    def checkWinner(self, board): 
        if sum(board[0:5]) == 0 or sum(board[7:12]) == 0:
            for slot in range(0,6): 
                board[6] += board[slot]
                board[slot] = 0
            for slot in range(7,13): 
                board[13] += board[slot]
                board[slot] = 0
            if board[6] > board[13]: 
                return True, board
            elif board[6] < board[13]: 
                return True, board 
            else: 
                return True, board 
        else:
            return False, board


    def calculateReward(self, board, player):
        if player == 0:
            return (board[6] - board[13])*10000
        else:
            return (board[13] - board[6])*10000


    def printBoard(self, board): 
        player_one = "|   |"
        for slot in range(7): 
            player_one += " " + str(board[slot]) + " |"

        player_two = " "  
        for slot in reversed(range(7,14)): 
            player_two += " " + str(board[slot]) + " |"

        graphic_board = player_two + "\n" + player_one
        print(graphic_board)


    def step(self, action):
        # Perform one step in the environment and return next_state, reward, done and info
        # Next state is the board after the action has been performed
        # Reward is the reward for the current player 
        # Greedy: (number of stones captured )
        # Smart : Look ahead to consider final winning state
        # Done is a boolean indicating whether the game is over
        # Info is a dictionary containing any debugging information, not used for trianing 

        # Check if action is valid
        if action < 0 or action > 5: 
            self.info['event'] = 'invalid_action'
            # return next_state, reward, done, info
            return self.current_state, -1, False, self.info

        # Check if game is over 
        done, self.current_state[0] = self.checkWinner(self.current_state[0])
        if done: 
            self.info['event'] = 'game_over'
            self.info['extra_info']['winner'] = self.checkWinner(self.current_state[0])
            # return next_state, reward, done, info
            return self.current_state, self.calculateReward(self.current_state[0], self.current_state[1]), True, self.info

        current_slot = action
        # print("Board before", self.current_state[0])

        # Shift action for player 2
        if self.current_state[1] == 1: 
            current_slot = action + 7

        # Check there are stones in that slot on the board
        if self.current_state[0][current_slot] == 0: 
            self.info['event'] = 'empty_slot'
            # return next_state, reward, done, info
            return self.current_state, -1e5, False, self.info

        stones_in_hand = self.current_state[0][current_slot]
        # empty action slot 
        self.current_state[0][current_slot] = 0

        # Distribute stones from next slot onwards
        current_slot +=1

        # Distribute stones
        for stone in range(stones_in_hand):
            # Check if opponent bank 
            if current_slot == self.opponent_bank[self.current_state[1]]: 
                current_slot += 1

            current_slot = current_slot % 14
            self.current_state[0][current_slot] += 1
            
            current_slot += 1   

        current_slot -= 1   
        
        # Check if ended on player's own bank
        if current_slot == self.player_bank[self.current_state[1]]: 
            # Player gets another turn
            self.info['event'] = 'extra_turn'
            # return next_state, reward, done, info
            return self.current_state, self.calculateReward(self.current_state[0], self.current_state[1]), False, self.info

        # Check if ended on empty slot and if on player's side
        if self.current_state[0][current_slot] == 1 and ((self.current_state[1] == 0 and current_slot < 6) or (self.current_state[1] == 1 and current_slot > 6)): 
            self.info['event'] = 'potential_capture'
            # Capture if possible
            self.current_state[0], self.info = self.opposite(self.current_state[0], self.current_state[1], current_slot, self.info) 
        
        # Switch player
        self.current_state[1] = (self.current_state[1] + 1) % 2
        self.info['event'] = 'switch_player'
        # return next_state, reward, done, info
        return self.current_state, self.calculateReward(self.current_state[0], self.current_state[1]), False, self.info


    def reset(self): 
        # Reset the state of the environment to an initial state and return that state 
        # Reset player turn too 
        self.info = {
            'event': None,
            'extra_info': {}
        }
        self.current_state = [[4,4,4,4,4,4,0,4,4,4,4,4,4,0], random.randint(0,1)]
        return self.current_state

    def render(self, mode='human'):
        # Optional: Render the environment state to terminal or GUI
        self.printBoard(self.current_state[0]) 