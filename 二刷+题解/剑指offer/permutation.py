#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   permutation.py
@Time    :   2020/05/20 21:18:16
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def permutation(self, S: str) -> List[str]:
        res = []

        def helper(cur, l):
            if not l and cur not in res:
                res.append(''.join(cur))
                return
            for i in range(len(l)):
                helper(cur + [l[i]], l[:i] + l[i+1:])
        helper([], list(S))
        return res
if __name__ == '__main__':
    pass