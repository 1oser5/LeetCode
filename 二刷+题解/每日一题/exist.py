# -*- encoding: utf-8 -*-
'''
@File    :   exist.py
@Time    :   2020/09/14 08:38:54
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, index):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != word[index]:
                return
            # finish match
            if index == length - 1:
                return True
            temp, board[x][y] = board[x][y], '#'
            for i, j in directions:
                if dfs(x + i, y + j, index + 1):
                    return True
            board[x][y] = temp

        m, n = len(board), len(board[0])
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        length = len(word)
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

if __name__ == '__main__':
    s = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")