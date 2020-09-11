# -*- encoding: utf-8 -*-
'''
@File    :   combinationSum3.py
@Time    :   2020/09/11 08:18:56
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def dfs(cur, cur_l, remain):
            if cur == n and len(cur_l) == k:
                res.append(cur_l)
                return
            for i in range(len(remain)):
                # 剪枝
                if remain[i] + cur > n:
                    break
                dfs(cur + remain[i], cur_l + [remain[i]], remain[i+1:])
        res = []
        dfs(0, [], list(range(1, 10)))
        return res
if __name__ == '__main__':
    s = Solution()
    c = s.combinationSum3(3, 7)
    print(c)