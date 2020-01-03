#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   isValidSudoku.py
@Time    :   2020/01/03 16:28:53
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] in col: return False
            col.add(board[i][0])
            col.clear() # 清理列
            for j in range(n):
                if board[i][j] in row: return False
                row.add(board[i][j])
             
