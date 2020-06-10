#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   isPalindrome.py
@Time    :   2020/06/10 14:06:37
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        y = x
        while y > 0:
            c = y % 10
            res = 10*res + c
            y = y // 10
        return res == x

if __name__ == '__main__':
    s = Solution()
    c = s.isPalindrome(121)
    print(c)