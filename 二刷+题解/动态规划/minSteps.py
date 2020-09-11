# -*- encoding: utf-8 -*-
'''
@File    :   minSteps.py
@Time    :   2020/09/11 08:47:59
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            m = float('inf')
            for j in range(1, i):
                # 非素数
                if i % j == 0:
                    m = min(m, dp[j] + i // j)
            dp[i] = m
        return dp[-1]


if __name__ == '__main__':
    s = Solution().minSteps(6)
    print(s)