#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   equationsPossible.py
@Time    :   2020/06/08 09:07:35
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''


# here put the import lib
class UnionFind(object):
    parents = {}

    def __init__(self, equations):
        for eq in equations:
            self.parents[eq[0]] = eq[0]
            self.parents[eq[3]] = eq[3]

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


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(equations)
        for eq in equations:
            if eq[1] == '=':
                uf.union(eq[0], eq[3])

        for eq in equations:
            if eq[1] == '!':
                if uf.connected(eq[0], eq[3]):
                    return False
        return True


if __name__ == '__main__':
    pass