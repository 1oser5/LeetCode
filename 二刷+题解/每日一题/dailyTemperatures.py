#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   dailyTemperatures.py
@Time    :   2020/06/11 09:36:52
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return[]
        stack = []
        size = len(T)
        res = [0] * size
        for index in range(size):
            while stack and T[stack[-1]] < T[index]:
                c = stack.pop()
                res[c] = index - c
            stack.append(index)
        return res
if __name__ == '__main__':
    s = Solution()
    s.dailyTemperatures([73,74,75,71,69,72,76,73])