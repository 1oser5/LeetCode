#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   longestPalindrome.py
@Time    :   2020/05/21 08:56:08
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        size = len(s)
        res = 0
        start = 0
        for i in range(1, size-1):
            left = i - 1
            right = i + 1
            while left > 0 and right < size and s[left] == s[right]:
                left -= 1
                right += 1
            if right-left+1 > res:
                res = right-left+1
                start = left
        return ''.join(s[start:start+res][1:-1].split('#'))
if __name__ == '__main__':
    s = Solution()
    c = s.longestPalindrome("babad")
    print(c)