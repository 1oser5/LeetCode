#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   findAnagrams.py
@Time    :   2019/12/25 20:38:34
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_list = [0] * 26
        c_list = [0] * 26
        length = len(p)
        res = []
        for i in p:
            p_list[ord(i)-97] += 1
        for i, v in enumerate(s):
            c_list[ord(v)-97] += 1
            if i >= length:
                c_list[ord(s[i-length])-97] -= 1
            if c_list == p_list:
                res.append(i-length+1)
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams('cbaebabacd', 'abc'))
