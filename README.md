# Mancala
*A personal project to learn and understand RL methods* 

Teaching a model to play Mancala using Reinforcement Learning.

## Mancala

### Board
The board is composed of 12 holes and 2 stores. Each player has 6 holes and 1 store. The holes are filled with a number of stones. The stores are empty at the beginning of the game. We represent the board as follows:

``` 
[4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
```

### Rules
The game starts with 4 stones in each hole. The player can choose a hole on their side of the board and pick up all the stones in it. They then distribute the stones in the following holes, one by one, in a counter-clockwise direction. The player can also drop a stone in their own store. 

If the last stone is dropped in the player's store, they can play again. If the last stone is dropped in an empty hole on the player's side, they capture all the stones in the opposite hole and puts them in their own store. 

The game ends when a player has no more stones on their side of the board. The player with the most stones in their store wins.


## Steps
- [x] Implement Mancala game and full rules
- [x] Play locally against a random agent
- [ ] Implement a simple RL algorithm
- [ ] Play against the RL agent
- [ ] Implement complex RL algorithm
- [ ] Play against the RL agent