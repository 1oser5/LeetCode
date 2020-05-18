#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxProduct.py
@Time    :   2020/05/18 08:33:33
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, cmin, cmax = float('-inf'), 1, 1
        for i in range(len(nums)):
            cur = nums[i]
            if cur < 0:
                cmax, cmin = cmin, cmax
            cmax = max(cur, cur * cmax)
            cmin = min(cur, cur * cmin)
            res = max(cmax, res)
        return res

if __name__ == '__main__':
    s = Solution()
    s.maxProduct([-2,0,-1])