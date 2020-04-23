#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   missingNumber.py
@Time    :   2020/04/19 09:48:15
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] != mid:
                right -= 1
            else:
                left += 1
        return left



if __name__ == '__main__':
    pass