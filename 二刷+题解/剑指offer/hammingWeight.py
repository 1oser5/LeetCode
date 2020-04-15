#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   hammingWeight.py
@Time    :   2020/04/15 09:17:35
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   位运算真的秀
'''

# here put the import lib
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight1(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n-1
        return res

if __name__ == '__main__':
    pass