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
def isValidSudoku( board):
    seen = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c != '.':
                seen += [(c,j),(i,c),(i//3,j//3,c)]
    print(seen)
    print(set(seen))
    return len(seen) == len(set(seen))
             
if __name__ == '__main__':
    isValidSudoku([
    ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])