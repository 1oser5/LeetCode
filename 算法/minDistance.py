#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   minDistance.py
@Time    :   2020/01/08 14:09:03
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
from pprint import pprint
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """ up-down """
        def track(word1, word2, memo={}):
            if not (word1 or word2): return 0
            if not len(word1) or not len(word2):
                return len(word1) or len(word2)
            if word1[0] == word2[0]:
                return track(word1[1:], word2[1:], memo)
            if (word1, word2) not in memo:
                inserted = 1 + track(word1, word2[1:])
                deleted = 1 + track(word1[1:], word2)
                replaced = 1 + track(word1[1:], word2[1:])
                memo[(word1, word2)] = min(inserted, deleted, replaced)
            return memo[(word1, word2)]
        return track(word1, word2)
    def minnDistance1(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp  = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        return dp[-1][-1]
if __name__ == '__main__':
    s = Solution()
    # s.minDistance('horse', 'ros')
    s.minDistance('intention', 'execution')