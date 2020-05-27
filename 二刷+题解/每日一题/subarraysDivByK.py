#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   subarraysDivByK.py
@Time    :   2020/05/27 09:21:52
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        size = len(A)
        cur = 0
        res = 0
        count[0] = 1
        for i in range(size):
            cur += A[i]
            less = cur % K
            if less in count:
                res += count[less]
            count[less] += 1
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.subarraysDivByK([4,5,0,-2,-3,1], 5)
    print(c)