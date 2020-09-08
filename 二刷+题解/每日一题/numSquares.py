# -*- encoding: utf-8 -*-
'''
@File    :   numSquares.py
@Time    :   2020/09/08 14:03:14
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            j = 1
            while i - j * j >= 0:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
if __name__ == '__main__':
    s = Solution().numSquares(12)
    print(s)