#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findCircleNum.py
@Time    :   2020/06/08 10:04:16
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List


class UnionFind(object):
    parents = {}

    def __init__(self, M):
        self._count = len(M)
        for i in range(len(M)):
            self.parents[i] = i

    def find(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        return x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.connected(x, y):
            return
        self.parents[self.find(x)] = self.find(y)
        self._count -= 1

    def count(self):
        return self._count

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        u = UnionFind(M)
        col = len(M)
        row = len(M[0])
        for i in range(col):
            for j in range(row):
                if M[i][j] == 1:
                    u.union(i, j)
        return u.count()

if __name__ == '__main__':
    s = Solution()
    c = s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
    print(c)