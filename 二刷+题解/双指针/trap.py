#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   trap.py
@Time    :   2020/04/12 15:53:26
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''

# here put the import lib
class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        res = 0
        max_l, max_r = 0, 0
        while start <= end:
            if max_l < max_r:
                max_l = max(height[start], max_l)
                res += max_l - height[start]
                start += 1
            else:
                max_r = max(height[end], max_r)
                res += max_r - height[end]
                end -= 1
        return res






if __name__ == '__main__':
    pass