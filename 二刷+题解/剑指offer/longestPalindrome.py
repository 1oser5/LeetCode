#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   longestPalindrome.py
@Time    :   2020/05/14 08:57:20
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """ 暴力算法 """
        if not s:
            return ''
        s = '#' + '#'.join(list(s)) + '#'
        n = len(s)
        res = ''
        for i in range(n):
            left, right = i-1, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                res = res if len(res) > len(s[left:right+1]) else s[left:right+1]
                left -= 1
                right += 1
        return ''.join(res.split('#'))

    def longestPalindrome1(self, s: str) -> str:
        if len(s) < 2:
            return s
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0
        for i in range(n):
            dp[i][i] = True
        for j in range(1, n):
            for i in range(0, j):
                if s[j] == s[i]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        start = i
                        max_len = cur_len
        return s[start:start+max_len]

if __name__ == '__main__':
    s = Solution()
   # c = s.longestPalindrome("cbbd")
   # c = s.longestPalindrome1("babad")
    c = s.longestPalindrome1("ac")
    print(c)