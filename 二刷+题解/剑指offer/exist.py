#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   exist.py
@Time    :   2020/04/26 20:40:27
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m = len(board)
        n = len(board[0])

        def dfs(x, y, k):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            temp, board[x][y] = board[x][y], '/'
            res = dfs(x+1, y, k+1) or dfs(x, y+1, k+1) or dfs(x-1, y, k+1) or dfs(x, y-1, k+1)
            board[x][y] = temp
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    # s.exist([["a"]], "ab")
    s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
    #print(0<3<2)