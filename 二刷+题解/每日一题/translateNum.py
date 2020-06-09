#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   translateNum.py
@Time    :   2020/06/09 09:44:58
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def translateNum(self, num: int) -> int:
        ''' dp normal solution '''
        num = str(num)
        size = len(num)
        dp = [0] * (size+1)
        dp[0], dp[1] = 1, 1  # single str only one choose
        for i in range(2, size+1):
            dp[i] = dp[i-1] + dp[i-2] if '10' <= num[i-2:i] <= '25' else dp[i-1]
        return dp[-1]

    def translateNum1(self, num: int) -> int:
        num = str(num)
        a = b = 1
        for i in range(2, len(num)+1):
            a, b = a + b if '10' <= num[i-2: i] <= '25' else a, a
        return a

if __name__ == '__main__':
    pass