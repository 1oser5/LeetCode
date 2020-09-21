# -*- encoding: utf-8 -*-
'''
@File    :   subsets.py
@Time    :   2020/09/20 10:39:41
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯法
        res = []

        def dfs(cur, remain):
            res.append(cur)
            if not remain:
                return
            for i in range(len(remain)):
                dfs(cur + [remain[i]], remain[i + 1:])
        dfs([], nums)
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [r + [num] for r in res]
        return res

if __name__ == '__main__':
    s = Solution()
    s.subsets1([1,2,3])