#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findLength.py
@Time    :   2020/08/11 16:09:01
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
'''

# here put the import lib
class Solution:
    # dp solution
    def findLength(self, A: List[int], B: List[int]) -> int:
        a_size = len(A)
        b_size = len(B)
        ans = 0
        dp = [[0] * (a_size + 1) for _ in range(b_size)]
        for i in range(a_size-1, -1, -1):
            for j in range(b_size-1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans
    # 滑动窗口 sliding windows
    def findLength1(self, A: List[int], B: List[int]) -> int:
        def maxLength(partA, partB, length):
            ret = k = 0
            for i in range(length):
                if A[partA + i] == B[partB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret
        a_size = len(A)
        b_size = len(B)
        ans = 0
        for i in range(a_size):
            length = max(b_size, a_size - i)
            ans = max(ans, maxLength(i, 0, length))
        for j in range(b_size):
            length = max(a_size, b_size - j)
            ans = max(ans, maxLength(0, j, length))
        return ans
if __name__ == '__main__':
    pass