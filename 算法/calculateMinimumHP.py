#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   calculateMinimumHP.py
@Time    :   2020/01/13 15:47:52
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    # def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    #     from pprint import pprint
    #     dungeon = [[-j for j in i] for i in dungeon]
    #     m = len(dungeon)
    #     n = len(dungeon[0])
    #     dp = [[(float('inf'), 0)] * (n+1) for _ in range(m+1)]
    #     dp[0][1] = (0,0)
    #     dp[1][0] = (0,0)
    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if dungeon[i-1][j-1] < 0: # 当前格子为回血情况
    #                 dp[i][j] = (min(dp[i-1][j], dp[i][j-1])[0], dungeon[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])[1])
    #             else:
    #                 dp[i][j] = (min(dp[i-1][j], dp[i][j-1])[0] + dungeon[i-1][j-1], dungeon[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])[1])
    #     return dp[i][j][0] + 1 if dp[i][j][0] > 0 else 1
    def calculateMinimumHP1(self, dungeon):
        if not dungeon:
            return 
        r, c = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])
        for i in range(c-2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1]-dungeon[-1][i])
        for i in range(r-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1]-dungeon[i][-1])
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        return dp[0][0]
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0]*n + [float('inf')] for _ in range(m)] + [[float('inf')]*(n-1)+[1,1]]
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        return dp[0][0]    
# O(n) space
# def calculateMinimumHP(self, dungeon):
#     if not dungeon:
#         return 
#     r, c = len(dungeon), len(dungeon[0])
#     dp = [0 for _ in range(c)]
#     dp[-1] = max(1, 1-dungeon[-1][-1])
#     for i in range(c-2, -1, -1):
#         dp[i] = max(1, dp[i+1]-dungeon[-1][i])
#     for i in range(r-2, -1, -1):
#         dp[-1] = max(1, dp[-1]-dungeon[i][-1])
#         for j in range(c-2, -1, -1):
#             dp[j] = max(1, min(dp[j], dp[j+1])-dungeon[i][j])
#     return dp[0]
if __name__ == '__main__':
    s = Solution()
    s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
    # s.calculateMinimumHP1([[-3,5]])
    # print(s.calculateMinimumHP1([[2,1],[1,-1]]))