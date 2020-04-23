#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minNumber.py
@Time    :   2020/04/23 21:51:02
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def fast_sort(l, r):
            if l > r:
                return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i-1)
            fast_sort(i+1, r)
        strs = [str(num) for num in nums]
        fast_sort(0, len(strs)-1)
        return ''.join(strs)
if __name__ == '__main__':
    print(int("102") > int("0210"))
    print(int("0210"))