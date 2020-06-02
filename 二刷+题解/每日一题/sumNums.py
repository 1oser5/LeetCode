#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   sumNums.py
@Time    :   2020/06/02 12:05:30
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res
if __name__ == '__main__':
    pass