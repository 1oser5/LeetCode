#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxIncreaseKeepingSkyline.py
@Time    :   2020/05/20 20:42:03
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        m_max = [max(i) for i in grid]
        n_max = [max(j) for j in zip(*grid)]
        res = 0
        for i in range(m):
            for j in range(n):
                res += min(m_max[i], n_max[j]) - grid[i][j]
        return res
if __name__ == '__main__':
    s = Solution()
    s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])