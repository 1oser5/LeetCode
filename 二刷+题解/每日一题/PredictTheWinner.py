# -*- encoding: utf-8 -*-
'''
@File    :   PredictTheWinner.py
@Time    :   2020/09/03 15:39:46
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = nums[i]
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0
if __name__ == '__main__':
    s = Solution()
    s.PredictTheWinner([1,5,2])