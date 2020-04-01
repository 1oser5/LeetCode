#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   combinationSum4.py
@Time    :   2020/01/15 16:50:29
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
from pprint import pprint
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[1] = 1
        for q in range(max(nums)):
            dp[q] = sum([dp[q-j] + 1 if q - j >=0 else 0 for j in nums])
        print(dp)
        # for i in range(max(nums[i])+1, target + 1):
        #     dp[i] = sum([dp[i-j] + dp[j] if i - j >=0 else 0 for j in nums])
        # pprint(dp)
        return dp
if __name__ == '__main__':
    s = Solution()
    s.combinationSum4([1, 2, 3], 4)