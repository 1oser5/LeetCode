#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   minWindow.py
@Time    :   2020/01/08 16:32:36
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or set(t) -set(s): return ""
        
if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ab",'b'))
    print(s.minWindow("ab",'a'))
    print(s.minWindow("ADOBECODEBANC","ABC"))