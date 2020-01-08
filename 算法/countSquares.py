#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   countSquares.py
@Time    :   2020/01/08 20:11:39
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
from pprint import pprint
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1) ]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return  sum([sum(i) for i in dp])
if __name__ == '__main__':
    s = Solution()
    s.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])