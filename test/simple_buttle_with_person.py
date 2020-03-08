import sys
sys.path.append("..")
from TicTacToe import TicTacToe


ttt = TicTacToe()
cnt = 0
while True:
    print(ttt.table)
    row, col = input().split(" ")
    end_flag = ttt.set(row, col, True if cnt %2 == 0 else False)
    if end_flag:
        break
    cnt += 1
