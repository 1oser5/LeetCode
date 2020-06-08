#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   numIslands.py
@Time    :   2020/06/08 11:06:03
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib

class UnionFind(object):

    def __init__(self, n):
        self._count = n
        self.parents = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.connected(x, y):
            return
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] > self.rank[root_y]:
            self.parents[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parents[root_x] = root_y
        else:
            self.parents[root_y] = root_x
            self.rank[root_x] += 1
        self._count -= 1

    def count(self):
        return self._count
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        dummy = col * row

        def get_index(x, y):
            return x * col + y

        u = UnionFind(dummy+1)  # add dummy
        directions = [(1, 0), (0, 1)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    u.union(get_index(i, j), dummy)  # water connect to dummy node
                if grid[i][j] == '1':
                    for d in directions:
                        new_x = i + d[0]
                        new_y = j + d[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            u.union(get_index(i, j), get_index(new_x, new_y))

        return u.count() - 1

if __name__ == '__main__':
    s = Solution()
    s.numIslands([["1","1","1","1","1","1","1"],["0","0","0","0","0","0","1"],["1","1","1","1","1","0","1"],["1","0","0","0","1","0","1"],["1","0","1","0","1","0","1"],["1","0","1","1","1","0","1"],["1","1","1","1","1","1","1"]])