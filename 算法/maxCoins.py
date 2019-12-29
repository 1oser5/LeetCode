#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   maxCoins.py
@Time    :   2019/12/29 17:08:43
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Top-Down
        def foo(i, j):
            if i >= j-1:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            temp = 0
            for k in range(i + 1, j): # 不取 i 和 j
                last_burn = nums[i] * nums[k] * nums[j]
                temp =  max(last_burn + foo(i, k) + foo(k, j), temp)
                dp[(i, j)] = temp
                return temp
        nums = [1] + [x for x in nums if x > 0] + [1]
        dp = {}
        return foo(0,len(nums)-1)
if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([76,64,21,97,60]))