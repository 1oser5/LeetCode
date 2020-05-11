#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   coinChange.py
@Time    :   2020/05/11 09:14:08
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if(i >= coin):
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != float("inf") else -1

if __name__ == '__main__':
    s = Solution()
    s.coinChange([1, 2, 5], 11)
    # s.coinChange([2], 3)
    # s.coinChange([1], 0)