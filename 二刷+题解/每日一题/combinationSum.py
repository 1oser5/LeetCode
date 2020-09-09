# -*- encoding: utf-8 -*-
'''
@File    :   combinationSum.py
@Time    :   2020/09/09 08:13:30
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 排序
        candidates.sort()

        def dfs(cur, path):
            if cur == target and sorted(path) not in res:
                res.append(sorted(path))
            for candidate in candidates:
                # 剪枝
                if candidate + cur > target:
                    break
                dfs(cur + candidate, path + [candidate])
        dfs(0, [])
        return res
if __name__ == '__main__':
    s = Solution().combinationSum([8,7,4,3]
,11)
    print(s)