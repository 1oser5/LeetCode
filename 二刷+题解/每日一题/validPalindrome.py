#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   validPalindrome.py
@Time    :   2020/05/19 08:15:47
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.isValid(s[low-1:high+1]) or self.isValid(s[low, high])
        return True
    def isValid(self, s):
        return s == s[::-1]




if __name__ == '__main__':
    pass