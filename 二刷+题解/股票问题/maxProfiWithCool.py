#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfiWithCool.py
@Time    :   2020/05/19 14:27:22
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' 状态机 '''
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float('-inf')
        dp_pre_0 = 0
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0
if __name__ == '__main__':
    pass