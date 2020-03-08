import pandas as pd
import numpy as np

from error import *

class TicTacToe:
    __CROSS = -1                                                        # Value for describing X
    __CIRCLE = 1                                                        # Value for describing O     
    __ROW = 3                                                           # The number of row
    __COL = 3                                                           # The number of column
    __INDEX = list("123")                                               # Row index list
    __COLUMNS = list("ABC")                                             # Column index list
    __CONVERT_TABLE = {0: "-", 1: "X", -1: "O"}                         # table for converting number to text for print table
    __CONVERT_ROW = {k: v for k, v in zip(__INDEX, range(__ROW))}       # table for converting text to number of Row
    __CONVERT_COL = {k: v for k, v in zip(__COLUMNS, range(0, 3))}      # table for converting text to number of Column

    def __init__(self):
        self.__table = pd.DataFrame(np.zeros((3, 3), dtype=np.int8), 
                                    index=self.__INDEX, 
                                    columns=self.__COLUMNS)

        self.__AVAIL_ACTION = {f"{r} {c}": True for r in self.__INDEX for c in self.__COLUMNS}

    @property
    def table(self):
        """ get table

        Examples:
            >>> ttt = TicTacToe()
            >>> print(ttt.table)
              A  B  C
            1  -  -  -
            2  -  -  -
            3  -  -  - 
        """
        return self.__table.replace(self.__CONVERT_TABLE)
    

    @property
    def avail_action(self):
        return [k for k, v in self.__AVAIL_ACTION.items() if v]

    def set(self, row, col, is_X=True):
        """ set piece to table

        Arguments:
            row {str} -- row index
            col {str} -- column index

        Keyword Arguments:
            is_X {bool} -- whether mode is setting X's piece (default: True)

        Returns:
            {bool} -- True when game is finished
        """ 
        # check arguments' type
        assert type(row) == str, TypeError("row must be set as string")
        assert type(col) == str, TypeError("col must be set as string")

        # check arguments are valid specification
        assert row in self.__INDEX, InvalidRowError(row)
        assert col in self.__COLUMNS, InvalidColumnError(col)

        # convert text to number
        self._update_avail_action(row, col)
        row = self.__CONVERT_ROW[row]
        col = self.__CONVERT_COL[col]

        # check specified position is already set or not
        if self._is_exist(row, col):
            raise ExistError()

        # update table
        self.__table.iloc[row, col] = 1 if is_X else -1

        return self._is_finish() | self._is_full()   # check whether game is finished or not

    def _update_avail_action(self, row, col):
        """ update available action's list

        Arguments:
            row {str} -- row index
            col {str} -- column index
        """
        self.__AVAIL_ACTION[f"{row} {col}"] = False

    def _is_full(self):
        """ check there're no plcae to set

        Returns:
            {bool} -- True when there're no place to set
        """
        return True if not 0 in self.__table.values else False

    def _is_exist(self, row, col):
        """ check whether specified position is already set

        Arguments:
            row {int} -- position of row
            col {int} -- position of column

        Returns:
            {bool} -- True when specified position is already set
        """
        return True if not self.__table.iloc[row, col] == 0 else False
    
    def _is_finish(self):
        """ check whether game is finished

        Returns:
            {bool} -- True when game is finished
        """
        val = self.__table.values
        win_flag = {"X": False, "O": False}

        # check vertical
        vertical_sum = np.sum(val, axis=0)
        is_X_win = any([self._win_X(val) for val in vertical_sum])
        is_O_win = any([self._win_O(val) for val in vertical_sum])
        win_flag["X"] |= is_X_win
        win_flag["O"] |= is_O_win

        # check horizontal
        horizontal_sum = np.sum(val, axis=1)
        is_X_win = any([self._win_X(val) for val in horizontal_sum])
        is_O_win = any([self._win_O(val) for val in horizontal_sum])
        win_flag["X"] |= is_X_win
        win_flag["O"] |= is_O_win
 
        # check cross
        # decending direction
        base_dec = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        dec_sum = np.sum(val * base_dec)
        is_X_win = True if dec_sum == 3 else False
        is_O_win = True if dec_sum == -3 else False
        win_flag["X"] |= is_X_win
        win_flag["O"] |= is_O_win
 
        # ascendig direction
        base_asc = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        asc_sum = np.sum(val * base_asc)
        is_X_win = True if asc_sum == 3 else False
        is_O_win = True if asc_sum == -3 else False
        win_flag["X"] |= is_X_win
        win_flag["O"] |= is_O_win
 
        if win_flag["X"]:
            print("X is win")
            return True
        elif win_flag["O"]:
            print("O is win")
            return True

        return False

    def _win_X(self, val):
        """ check game is finished by X for vertical or horizontal sum

        Arguments:
            val {list(int)} -- sum of vertical or horizontal

        Returns:
            {bool} -- True when game is finished by X
        """
        return True if val == 3 else False

    def _win_O(self, val):
        """ check game is finished by O for vertical or horizontal sum

        Arguments:
            val {list(int)} -- sum of vertical or horizontal

        Returns:
            {bool} -- True when game is finished by O
        """
        return True if val == -3 else False


if __name__ == "__main__":
    t = TicTacToe()
    cnt = 0
    while True:
        print(t.table)
        row, col = input("Row Column >>").split(" ")
        flag = t.set(row, col, True if cnt %2 == 0 else False)
        if flag:
            break
        cnt += 1

    print(t.table)
