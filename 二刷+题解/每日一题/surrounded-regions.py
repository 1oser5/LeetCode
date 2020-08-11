#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   surrounded-regions.py
@Time    :   2020/08/11 15:42:55
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        cols = len(board)
        rows = len(board[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= cols or y >= rows or board[x][y] != 'O':
                return
            board[x][y] = '#'
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

        for i in range(cols):
            dfs(i, 0)
            dfs(i, rows - 1)

        for j in range(rows):
            dfs(0, j)
            dfs(cols - 1, j)

        for i in range(cols):
            for j in range(rows):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
