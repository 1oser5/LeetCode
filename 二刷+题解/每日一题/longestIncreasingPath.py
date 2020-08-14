# -*- encoding: utf-8 -*-
'''
@File    :   longestIncreasingPath.py
@Time    :   2020/08/14 14:06:39
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memory = {}
        col = len(matrix)
        row = len(matrix[0])
        res = 0

        def bfs(x, y, prev, index):
            if x >= col or x < 0 or y >= row or y < 0 or matrix[x][y] <= prev:
                return index
            if (x, y) in memory:
                return memory[(x, y)]
            # set memory
            memory[(x, y)] = index
            right = bfs(x + 1, y, matrix[x][y], index + 1)
            left = bfs(x - 1, y, matrix[x][y], index + 1)
            up = bfs(x, y + 1, matrix[x][y], index + 1)
            down = bfs(x, y - 1, matrix[x][y], index + 1)
            return max(right, left, up, down)
        for i in range(col):
            for j in range(row):
                cur = bfs(i, j, float('-inf'), 0)
                res = max(cur, res)
        print(res)
        return res
if __name__ == '__main__':
    s = Solution()
    s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])