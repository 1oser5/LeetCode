#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   cuttingRope.py
@Time    :   2020/04/24 08:34:56
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(i):
                dp[i] = max(dp[i], (i-j)*j, j*dp[i-j])
        return dp[-1]
if __name__ == '__main__':
    pass