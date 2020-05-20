#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxAreaOfIsland.py
@Time    :   2020/05/20 21:56:49
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def bfs(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 0
                return bfs(x+1, y) + bfs(x, y+1) + bfs(x, y-1) + bfs(x-1, y) + 1
            return 0
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(bfs(i, j), res)
        return res
if __name__ == '__main__':
    s = Solution()
    # c = s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    c = s.maxAreaOfIsland([[1]])
    #c = s.maxAreaOfIsland([[1,1],[1,0]])
    print(c)