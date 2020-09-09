# -*- encoding: utf-8 -*-
'''
@File    :   lastStoneWeightII.py
@Time    :   2020/09/09 11:05:25
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)/2.0
        candidates = {0}
        for x in stones:
            addition = set()
            for y in candidates:
                if x+y <= target:
                    addition.add(x+y)
            candidates = candidates.union(addition)
        return int(2*(target-max(candidates)))


if __name__ == '__main__':
    s = Solution().lastStoneWeightII([2,7,4,1,8,1])
