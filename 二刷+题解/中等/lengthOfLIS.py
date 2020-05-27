#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lengthOfLIS.py
@Time    :   2020/05/26 19:31:16
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return
        size = len(nums)
        dp = [1] * size
        for i in range(size):
            for j in range(i):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
if __name__ == '__main__':
    s = Solution()
  #  s.lengthOfLIS([10,9,2,5,3,7,101,18])
   # c = s.lengthOfLIS([10,9,2,5,3,4])
    c = s.lengthOfLIS([3,2,1])
    print(c)
