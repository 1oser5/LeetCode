# -*- encoding: utf-8 -*-
'''
@File    :   cuttingRope.py
@Time    :   2020/09/11 08:35:39
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(i - 1):
                dp[i] = max(dp[i], max(j * dp[i-j], j * (i - j))) # j * dp[i-j] 表示继续切，j * (i - j)表示不切
        return dp[-1] % 1000000007
if __name__ == '__main__':
    pass