#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   productExceptSelf.py
@Time    :   2020/06/04 19:06:40
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, l, r = [1], 1, 1
        size = len(nums)
        for i in range(size-1):
            l *= nums[i]
            res.append(l)
        for i in range(size-1, 0, -1):
            r *= nums[i]
            res[i-1] *= r
        return res
if __name__ == '__main__':
    pass