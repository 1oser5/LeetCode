#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   longestCommonPrefix.py
@Time    :   2020/06/15 09:02:05
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        pre, size = strs[0], len(strs)
        for index in range(size):
            pre = self.lcp(strs[index], pre)
            if not pre:  # no content just break
                break
        return pre

    def lcp(self, str1, str2):
        size1 = len(str1)
        size2 = len(str2)
        index = 0
        while index < min(size1, size2):
            if str1[index] != str2[index]:
                break
            index += 1

        return str1[:index]

if __name__ == '__main__':
    s = Solution()
    c = s.longestCommonPrefix(["flower","flow","flight"])
    print(c)