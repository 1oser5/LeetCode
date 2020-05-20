#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   generateParenthesis.py
@Time    :   2020/05/20 21:48:24
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(left, right, cur):
            if not left and not right:
                res.append(''.join(cur))
                return
            if left > 0:
                helper(left-1, right, cur + ['('])
            if right > 0 and left < right:
                helper(left, right-1, cur + [')'])
        helper(n, n, [])
        return res
if __name__ == '__main__':
    s = Solution()
    s.generateParenthesis(3)
