#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxValue.py
@Time    :   2020/04/09 14:34:55
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        col = len(grid)
        row = len(grid[0])
        dp = [[0] * (row+1) for _ in range(col+1)]
        for i in range(1, col+1):
            for j in range(1, row+1):
                dp[i][j] = grid[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    s.maxValue([[1,3,1],[1,5,1],[4,2,1]])