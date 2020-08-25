# -*- encoding: utf-8 -*-
'''
@File    :   findSubsequences.py
@Time    :   2020/08/25 08:00:00
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 回溯算法
        memory = []
        res = []
        def generate(l, r, memory):
            if l in memory:
                return
            if len(l) >= 2:
                res.append(l)
                memory.append(l)
            for i in range(len(r)):
                # 只有大于等于时继续递归
                if not l or r[i] >= l[-1]:
                    generate(l+[r[i]], r[i+1:], memory)
        generate([], nums, memory)
        return res

if __name__ == '__main__':
    s = Solution()
    s.findSubsequences([4, 6, 7, 7])