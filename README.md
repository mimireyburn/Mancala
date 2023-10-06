# Mancala Bot
*A personal project to learn RL methods and how to win at Mancala*

I recently watched the AlphaGo film. While Go is a very complex game, Mancala is very simple and by teaching a model to win, I think it's likely that I could use emergent patterns and behaviours to learn how to win at Mancala myself. I also wanted to understand how to implement RL algorithms and this seemed like a good way to do it.

### Board
The board is composed of 12 holes and 2 stores. Each player has 6 holes and 1 store. The holes are filled with a number of stones. The stores are empty at the beginning of the game. We represent the board as follows:

``` 
[4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
```

### Rules
The game starts with 4 stones in each hole. The player can choose a hole on their side of the board and pick up all the stones in it. They then distribute the stones in the following holes, one by one, in a counter-clockwise direction. The player can also drop a stone in their own store. 

If the last stone is dropped in the player's store, they can play again. If the last stone is dropped in an empty hole on the player's side, they capture all the stones in the opposite hole and puts them in their own store. 

The game ends when a player has no more stones on their side of the board. The player with the most stones in their store wins.

## To-Do
- [ ] Debug Agent recursively choosing empty slot 0

## Steps
- [x] Implement Mancala game and full rules
- [x] Play locally against a random agent
- [x] Implement a simple RL algorithm
- [x] Play against the RL agent
- [ ] Implement complex RL algorithm
- [ ] Play against the RL agent