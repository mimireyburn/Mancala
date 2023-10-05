from mancala_env import MancalaEnv  

env = MancalaEnv()

n_episodes = 100

for episode in range(n_episodes): 
    state = env.reset()
    done = False

    print("Episode: ", episode)

    while not done: 
        action = env.action_space.sample()
        next_state, reward, done, info = env.step(action)