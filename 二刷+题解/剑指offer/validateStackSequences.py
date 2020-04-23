#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   validateStackSequences.py
@Time    :   2020/04/23 21:16:49
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = []
        for p in pushed:
            res.append(p)
            while popped and res and popped[0] == res[-1]:
                res.pop()
                popped.pop(0)
        return len(res) == 0
if __name__ == '__main__':
    s = Solution()
    s.validateStackSequences([1,0], [1,0])