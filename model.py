import copy
from collections import deque 
from random import randint
from typing import List
import numpy as np

class LifeModel:
    def __init__(self, rows, cols):
        self.rows, self.cols = rows + 2, cols + 2
        self.board = np.zeros((self.rows, self.cols), dtype=np.int64)
        self.prev_states = deque()
        self.states_count = 5
        self.board_init()

    def get_board(self):
        #tboard = copy.deepcopy(self.board)
        return np.copy(self.board)
    
    def board_init(self)-> None:
        #print(self.cols, self.rows)
        """
        self.board = [[0 for j in range(self.cols)]\
                      for i in range(self.rows)]
        self.board = np.array(self.board, dtype=np.int64)
        """
        self.board = np.zeros((self.rows, self.cols), dtype=np.int64)
        for i in range( 1, self.rows - 1):
            for j in range( 1, self.cols - 1):
                self.board[i][j] = randint(0, 1)
        #self.board = np.random.randint(0, 2, self.board.shape)
        #print(self.board.shape)
        self.prev_states = deque()

    def board_next(self)-> bool:
        #tboard = copy.deepcopy(self.board)
        tboard = np.copy(self.board)
        for i in range( 1, self.rows - 1):
            for j in range( 1, self.cols - 1):
                if tboard[i][j] == 0:
                    res = 0
                    for ii in range( i - 1, i + 2):
                        for jj in range( j - 1, j + 2):
                            res += tboard[ii][jj]
                    if res == 3:
                        self.board[i][j] = 1  
                elif tboard[i][j] == 1:
                    res = 0
                    for ii in range( i - 1, i + 2):
                        for jj in range( j - 1, j + 2):
                            if not (ii == i and jj == j):
                                res += tboard[ii][jj]
                    if not(res == 2 or res == 3):
                        self.board[i][j] = 0

        """         
        res = 0 
        for i in range( 1, self.rows - 1):
            for j in range( 1, self.cols - 1):
                res += self.board[i][j]
        """
        # self.board == tboard: #or (self.board in self.prev_states):
        if np.count_nonzero(self.board) == 0 or np.array_equal(self.board, tboard):
            for pboard in self.prev_states:
                if np.array_equal(self.board, pboard):
                    return True
            
        if len(self.prev_states) < self.states_count:
            self.prev_states.appendleft(np.copy(self.board))
        else:
            self.prev_states.appendleft(np.copy(self.board))
            self.prev_states.pop()
        
        return False

    def show(self) -> None:
        print()
        for row in self.board:
            print(row)
        print()
        
if __name__ == "__main__":
    LM = LifeModel(10, 10)
    LM.board_init()
    LM.show()
    LM.board_next()
    LM.show()
    LM.board_next()
    LM.show()
    
