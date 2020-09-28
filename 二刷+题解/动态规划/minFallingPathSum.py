#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minFallingPathSum.py
@Time    :   2020/09/28 11:12:27
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        length = len(A)
        dp = [[float('inf')] * (length + 2) for _ in range(length + 1)]
        for i in range(1, length+1):
            dp[0][i] = 0
        for i in range(1, length + 1):
            for j in range(1, length + 1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j],
                               dp[i-1][j+1]) + A[i-1][j-1]
        return min(dp[-1])



if __name__ == '__main__':
    s = Solution()
    # s.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    s.minFallingPathSum([[69]])
