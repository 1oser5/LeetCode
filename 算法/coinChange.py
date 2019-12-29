#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   coinChange.py
@Time    :   2019/12/29 18:39:33
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return  -1 if dp[amount] == float('inf') else dp[amount]
if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5],10))