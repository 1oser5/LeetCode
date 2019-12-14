#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minimumTotal.py
@Time    :   2019/12/14 15:36:12
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        p = [[float('inf') for _ in range(len(triangle[i])+1)] for i in range(m)]
        p[0][0] = triangle[0][0]
        for i in range(1,m):
            for j in range(len(triangle[i])):
                p[i][j] = triangle[i][j] + min(p[i-1][j-1], p[i-1][j])
        return min(p.pop())
if __name__ == '__main__':
    s = Solution()
    s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])