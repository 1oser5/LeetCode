#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minimumTotal.py
@Time    :   2020/05/21 11:06:57
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ''' 自顶向下 开大数组'''
        m = len(triangle)
        dp = [[float('inf')] * (len(triangle[i])+2) for i in range(m)]
        dp[0][1] = triangle[0][0]
        for i in range(1, m):
            for j in range(1, len(triangle[i])+1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j-1]
        return min(dp[-1])

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        ''' 自底向上 天秀 '''
        size = len(triangle)
        for i in range(size-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
if __name__ == '__main__':
    s = Solution()
    c = s.minimumTotal2([[2],[3,4],[6,5,7],[4,1,8,3]])
    print(c)