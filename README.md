# TicTacToe

## Description
This repo is implementation of TicTacToe game in python.
Finally, I want to use this repo for studying reinforcement learning.

## Play game
You can play game by following below.

```python
from TicTacToe import TicTacToe

ttt = TicTacToe()
cnt = 0
while True:
    print(ttt.table)      # you can describe current game state
    row, col = input().split(" ")
    end_flag = ttt.set(row, col, True if cnt %2 == 0 else False)
    if end_flag:
        break
    cnt += 1
```
