#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   firstMissingPositive.py
@Time    :   2020/05/20 16:56:14
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            if 0 < nums[i] < size and i != nums[i] - 1:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1
        return size + 1

if __name__ == '__main__':
    pass