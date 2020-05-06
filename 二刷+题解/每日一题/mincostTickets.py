#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mincostTickets.py
@Time    :   2020/05/06 08:29:49
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """ 要加 lru_cache 才能用 """
        size = len(days)
        des = [1, 7, 10]

        def dp(i):
            if i > size:
                return 0
            ans = float('inf')
            j = i
            for c, d in zip(costs, des):
                while j < size and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)
            return ans
        return dp(0)

    def mincostTickets1(self, days: List[int], costs: List[int]) -> int:
        ans, day = [0] * (days[-1] + 30), {*days}
        for i in range(1, len(ans)):
            if i in day:
                ans[i] = min(
                    (ans[i-1] + costs[0]),
                    (ans[i-7] + costs[1]),
                    (ans[i-30] + costs[2])
                )
            else:
                ans[i] = ans[i-1]
        return ans[-1]


if __name__ == '__main__':
    pass