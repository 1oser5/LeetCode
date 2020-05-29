#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   rob.py
@Time    :   2020/05/29 09:07:59
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * (size + 2)
        for i in range(2, size+2):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
        return dp[-1]
if __name__ == '__main__':
    pass