# -*- encoding: utf-8 -*-
'''
@File    :   canVisitAllRooms.py
@Time    :   2020/09/03 15:24:29
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import defaultdict
        table = defaultdict(list)
        for i, v in enumerate(rooms):
            table[i] += v
        visited = set()

        def dfs(s):
            if s in visited:
                return
            visited.add(s)
            while table[s]:
                cur = table[s].pop()
                dfs(cur)
        dfs(0)
        return len(visited) == len(rooms)


if __name__ == '__main__':
    s = Solution()
    c = s.canVisitAllRooms([[1],[2],[3],[]])
    print(c)