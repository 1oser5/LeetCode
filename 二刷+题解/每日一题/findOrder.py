#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findOrder.py
@Time    :   2020/05/17 11:07:33
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        need = defaultdict(list)
        visited = [0] * numCourses
        res = []
        for c, p in prerequisites:
            need[p].append(c)
            # 计数
            visited[c] += 1
        res = [i for i in range(numCourses) if visited[i] == 0]
        bfs = res
        for i in bfs:
            for j in need[i]:
                visited[j] -= 1
                if visited[j] == 0:
                    res.append(j)
        return res if len(res) == numCourses else []

if __name__ == '__main__':
    s = Solution()
    c = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print(c)