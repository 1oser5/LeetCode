#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxDistance.py
@Time    :   2020/05/21 12:18:01
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        land = set()
        sea = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land.add((i, j))
                else:
                    sea.add((i, j))
        res = []
        for l in land:
            cur_x, cur_y = 0, 0
            cur = 0
            for s in sea:
                dis = self.getDes(l, s)
                if dis >= cur:
                    cur = dis
                    cur_x, cur_y = s
            res.append((cur_x, cur_y))
        print(res)
        x = sum([x[0] for x in res])
        y = sum([x[1] for x in res])
        return x, y

    def getDes(self, t, p):
        x1, y1 = t
        x2, y2 = p
        return abs(x1-x2) + abs(y1-y2)
if __name__ == '__main__':
    s = Solution()
    c = s.maxDistance([[1,0,1],[0,0,0],[1,0,1]])
    print(c)