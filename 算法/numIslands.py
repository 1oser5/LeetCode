#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   numIslands.py
@Time    :   2019/12/08 10:53:10
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

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

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """dfs solution"""
        # 特判
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        mark = [[ False for _ in range (n)] for _ in range(m)]
        count = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def dfs(i, j):
            mark[i][j] = True
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if 0 <= new_i < m and 0 <= new_j < n and not mark[new_i][new_j] and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not mark[i][j]:
                    dfs(i, j)
                    count += 1
        return count
    
    def nobodyIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    queue = deque()
                    count += 1
                    marked[i][j] = True
                    queue.append((i,j))
                    while queue:
                        x, y = queue.popleft()
                        for d in directions:
                            new_x = x + d[0]
                            new_y = y + d[1]
                            if not marked[new_x][new_y] and grid[new_x][new_y] == '1' and 0 <= new_x < m and 0<= new_y < n:
                                queue.append((new_x,new_y))
                                marked[new_x][new_y]  = True
                    return count
if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(grid)
    result = solution.nobodyIslands(grid)
    print(result)
