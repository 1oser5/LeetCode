#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   orangesRotting.py
@Time    :   2020/05/21 09:15:19
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotting-oranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        stack = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        # 找到所有的 腐烂的橘子
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append((i, j, time))
        while stack:
            x, y, time = stack.popleft()
            for di, dj in directions:
                if 0 <= di+x < m and 0 <= dj+y < n and grid[di+x][dj+y] == 1:
                    grid[di+x][dj+y] = 2
                    stack.append((di+x, dj+y, time+1))
        for i in grid:
            if 1 in i:
                return -1
        return time

if __name__ == '__main__':
    s = Solution()
    s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])