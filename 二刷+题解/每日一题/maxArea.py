#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxArea.py
@Time    :   2020/04/18 10:06:29
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        _max = 0
        while left < right:
            if height[left] < height[right]:
                _max = max(_max, (right-left) * height[left])
                left += 1
            elif height[left] >= height[right]:
                _max = max(_max, (right-left) * height[right])
                right -= 1
        return _max



if __name__ == '__main__':
    pass