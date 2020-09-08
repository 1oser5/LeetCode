# -*- encoding: utf-8 -*-
'''
@File    :   maxTurbulenceSize.py
@Time    :   2020/09/08 09:12:24
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        length = len(A)
        if length == 1 or max(A) == min(A):
            return 1
        dp = [1 for i in range(length)]
        for i in range(1, length - 1):
            if A[i-1] < A[i] > A[i+1] or A[i-1] > A[i] < A[i+1]:
                dp[i] = dp[i-1] + 1
        return max(dp) + 1

    def maxTurbulenceSize1(self, A: List[int]) -> int:
        length = len(A)
        if length <= 1:
            return 1
        f = 1
        g = 1
        res = 1
        for i in range(1, length):
            if A[i-1] > A:
                f2 = f + 1
            else:
                f2 = 1
            if A[i-1] < A:
                g2 = g + 1
            else:
                g2 = 1
            f = f2
            g = g2
            res = max(res, f)
            res = max(res, g)
        return res
if __name__ == '__main__':
    pass