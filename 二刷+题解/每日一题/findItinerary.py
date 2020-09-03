# -*- encoding: utf-8 -*-
'''
@File    :   findItinerary.py
@Time    :   2020/09/03 13:38:41
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''
from typing import List
# here put the import lib
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        d = defaultdict(list)
        for f, t in tickets:
            d[f] += [t]

        for f in d:
            d[f].sort()  # 邻接表排序

        res = []

        def dfs(s):
            while d[s]:
                dfs(d[s].pop(0))
            res.append(s)

        dfs('JKL')
        return res[::-1]

if __name__ == '__main__':
    pass