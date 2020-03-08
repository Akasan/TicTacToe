from TicTacToe import TicTacToe
import numpy as np
import argparse
from abc import ABCMeta, abstractmethod


class Computer(metaclass=ABCMeta):
    @abstractmethod
    def battle(self):
        pass


class RandomComputer(Computer):
    def __init__(self):
        self.__ttt = TicTacToe()

    def battle(self, is_player_first=True):
        """ start buttle with compute

        Arguments:
            is_player_first {bool} -- True when starting from player
        """
        iteration = 0 if is_player_first else 1

        while True:
            print(f"Turn : {'Player' if iteration % 2 == 0 else 'Computer'}")
            print(self.__ttt.table)
            
            if iteration % 2 == 0:      # プレイヤー
                row, col = input("Row Col >>>").split(" ")
                is_X = True

            else:
                action_list = self.__ttt.get_avail_action()
                idx = np.random.randint(0, len(action_list))
                action = action_list[idx]
                row, col = action.split(" ")
                is_X = False

            end_flag = self.__ttt.set(row, col, is_X)
            if end_flag:
                break

            iteration += 1
        
        print(self.__ttt.table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--turn", help="set this when you play first", action="store_true")
    args = parser.parse_args()
    is_first = args.turn
    comp = RandomComputer()
    comp.battle(is_player_first=is_first)
