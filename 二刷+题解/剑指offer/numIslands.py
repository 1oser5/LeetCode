#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   numIslands.py
@Time    :   2020/04/27 15:03:19
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        if not grid:
            return island
        m = len(grid)
        n = len(grid[0])
        memory = set()
        for col in range(m):
            for row in range(n):
                if (col, row) in memory or grid[col][row] == '0':
                    continue
                island += 1
                self.bfs(col, row, memory, grid)
        return island

    def bfs(self, x, y, memory, grid):
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
                continue
            if grid[x][y] == '0' or (x, y) in memory:
                continue
            memory.add((x, y))
            stack.append((x+1, y))
            stack.append((x-1, y))
            stack.append((x, y-1))
            stack.append((x, y+1))
if __name__ == '__main__':
    s = Solution()
    #c = s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    c = s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]])
    print(c)