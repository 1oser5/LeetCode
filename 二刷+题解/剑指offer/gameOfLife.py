#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   gameOfLife.py
@Time    :   2020/04/28 10:19:30
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        memory = {}
        for col in range(m):
            for row in range(n):
                memory.update({(col, row): board[col][row]})
                board[col][row] = self.isAlive(col, row, board, memory)

    def isAlive(self, x, y, board, memory):
        count = self.isTrue(x+1, y, board, memory) + self.isTrue(x+1, y+1, board, memory) + self.isTrue(x+1, y-1, board, memory) + self.isTrue(x-1, y, board, memory) + self.isTrue(x-1, y-1, board, memory) + self.isTrue(x-1, y+1, board, memory) + self.isTrue(x, y-1, board, memory) + self.isTrue(x, y+1, board, memory)
        if board[x][y] == 1:
            if count < 2 or count > 3:
                return 0
        if board[x][y] == 0:
            if count == 3:
                return 1
        return board[x][y]

    def isTrue(self, x, y, board, memory):
        if not 0 <= x < len(board) or not 0 <= y < len(board[0]):
            return 0
        if (x, y) in memory:
            return memory[(x, y)]
        return board[x][y]



if __name__ == '__main__':
    s = Solution()
    c = s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])