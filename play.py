from mancala_env import MancalaEnv  
import gym 
from gym import spaces
from collections import defaultdict
import random
import pickle


def q_learning(env, n_episodes=100000, gamma=0.9, alpha=0.1, epsilon=0.1):
    # Initialize Q-table
    Q_table = defaultdict(lambda: [0]*6)  # 6 possible actions

    # Epsilon-greedy action selection
    def epsilon_greedy(state, epsilon):
        valid_actions = env.get_valid_actions(board=state[0], player=state[1])
        # print("player", state[1], "valid actions:", valid_actions)
        # print("board state:", state[0])
        if len(valid_actions) == 0:
            done = True
            return done
        if random.random() < epsilon:
            return random.choice(valid_actions)
        else:
            return max(valid_actions, key=lambda x: Q_table[str(state)][x])

    # Main Q-learning loop
    for episode in range(n_episodes):
        state = env.reset()
        done = False
        print("Episode", episode)
        while not done:
            action = epsilon_greedy(state, epsilon)  # Assuming state[0] is the board
            next_state, reward, done, _ = env.step(action)
            
            # Q-value update
            old_value = Q_table[str(state[0])][action]
            next_max = max(Q_table[str(next_state[0])])
            
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            Q_table[str(state[0])][action] = new_value

            state = next_state

    return Q_table

def save_table(Q_table):
    with open("Q_table.pkl", "wb") as f:
        pickle.dump(dict(Q_table), f)

def load_table():
    with open("Q_table.pkl", "rb") as f:
        Q_table = defaultdict(lambda: [0]*6, pickle.load(f))
    return Q_table

def play(Q_table):
    state = env.reset()
    done = False
    
    while not done:
        env.render()
        if state[1] == 1:  # Agent's turn
            action = max(list(range(6)), key=lambda x: loaded_Q_table[str(state[0])][x])
            print("Agent's move:", action)
            print(env.info)
        else:  # Your turn
            action = int(input("Your move: "))
        next_state, reward, done, _ = env.step(action)
        state = next_state
    
    print("The winner is Player", env.info['extra_info']['winner']) 

if __name__ == "__main__":
    env = MancalaEnv()
    Q_table = q_learning(env)
    save_table(Q_table)
    # loaded_Q_table = load_table()
    # play(loaded_Q_table)