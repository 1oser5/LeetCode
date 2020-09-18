# -*- encoding: utf-8 -*-
'''
@File    :   permuteUnique.py
@Time    :   2020/09/18 09:26:43
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, candidate):
            if not candidate:
                res.append(cur)
            for i in range(len(candidate)):
                if i > 0 and candidate[i-1] == candidate[i]:
                    continue
                dfs(cur + [candidate[i]], candidate[:i] + candidate[i+1:])
        dfs([], sorted(nums))
        return res
if __name__ == '__main__':
    pass