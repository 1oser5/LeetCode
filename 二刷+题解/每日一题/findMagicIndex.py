#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findMagicIndex.py
@Time    :   2020/08/12 08:31:26
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if v == i:
                return i
        return -1
if __name__ == '__main__':
    pass