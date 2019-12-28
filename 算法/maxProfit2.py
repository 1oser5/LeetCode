#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   maxProfit2.py
@Time    :   2019/12/28 19:41:45
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        not_hold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, not_hold, notHold_cooldown = max(hold, not_hold - p), max(not_hold, notHold_cooldown), hold + p
        return max(not_hold, notHold_cooldown)
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,2,3,0,2]))