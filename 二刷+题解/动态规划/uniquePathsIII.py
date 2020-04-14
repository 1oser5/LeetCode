#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   uniquePathsIII.py
@Time    :   2020/04/13 20:17:10
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   在二维网格 grid 上，有 4 种类型的方格：

1 表示起始方格。且只有一个起始方格。
2 表示结束方格，且只有一个结束方格。
0 表示我们可以走过的空方格。
-1 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        max_len = 2
        start_x, start_y = 0, 0
        res = [0]
        # 确认起点位置
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    max_len += 1
                if grid[i][j] == 1:
                    start_x = i
                    start_y = j
        visited = [[False] * n for _ in range(m)]

        def dfs(grid, x, y, visited, now_len):
            # 越界情况
            if x < 0 or x >= len(grid):
                return
            if y < 0 or y >= len(grid[0]):
                return
            # 障碍
            if grid[x][y] == -1:
                return
            # 终点，需要判断路径长度
            if grid[x][y] == 2:
                if now_len == max_len:
                    res[0] += 1
                return
            if visited[x][y] is False:
                visited[x][y] = True
                dfs(grid, x+1, y, visited, now_len+1)
                dfs(grid, x-1, y, visited, now_len+1)
                dfs(grid, x, y+1, visited, now_len+1)
                dfs(grid, x, y-1, visited, now_len+1)
                visited[x][y] = False
        dfs(grid, start_x, start_y, visited, 1)
        return res[-1]
if __name__ == '__main__':
    s = Solution()
    c = s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    print(c)
