#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   uniquePathsWithObstacles.py
@Time    :   2020/04/13 20:09:22
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][1] = 1
        for col in range(1, m+1):
            for raw in range(1, n+1):
                if obstacleGrid[col-1][raw-1] == 1:
                    continue
                dp[col][raw] = dp[col-1][raw] + dp[col][raw-1]
        return dp[-1][-1]
if __name__ == '__main__':
    s = Solution()
    c = s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print(c)