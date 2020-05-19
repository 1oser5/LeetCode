#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfitWIthTwo.py
@Time    :   2020/05/19 19:11:48
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_2_0, dp_i_1_0 = 0, 0
        dp_i_2_1, dp_i_1_1 = float('-inf'), float('-inf')
        for price in prices:
            dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + price)
            dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - price)
            dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + price)
            dp_i_1_1 = max(dp_i_1_1, - price)
        return dp_i_2_0
if __name__ == '__main__':
    pass