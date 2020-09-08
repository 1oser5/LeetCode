# -*- encoding: utf-8 -*-
'''
@File    :   combine.py
@Time    :   2020/09/08 08:04:27
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(cur, remain):
            if len(cur) == k:
                return res.append(cur)
            for i in range(len(remain)):
                helper(cur + [remain[i]], remain[i+1:])
        helper([], [i for i in range(1, n+1)])
        return res

if __name__ == '__main__':
    pass