#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   largestRectangleArea.py
@Time    :   2020/05/13 09:40:45
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        ''' 暴力超时解 '''
        if not heights:
            return 0
        n = len(heights)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = heights[i-1]
        for i in range(n):
            _min = float('inf')
            for j in range(i, n):
                _min = min(_min, heights[j])
                dp[i][j] = (j-i+1) * _min
        return (max([max(i) for i in dp]))

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    c = s.largestRectangleArea([2,1,5,6,2,3])
    #c = s.largestRectangleArea([2,0,2])
    #c = s.largestRectangleArea([1])
    print(c)