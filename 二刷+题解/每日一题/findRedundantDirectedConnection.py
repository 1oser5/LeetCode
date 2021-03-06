#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findRedundantDirectedConnection.py
@Time    :   2020/09/17 08:17:23
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

# 并查集模板


class DisJoinSet:
    def __init__(self, N):
        self.pa = list(range(N + 1))
        self.cnt = N

    def find_root(self, x):
        if x != self.pa[x]:
            self.pa[x] = self.find_root(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if root_x != root_y:
            self.pa[root_x] = root_y
            # 合并成功，连通分量减1
            self.cnt -= 1
            return True
        else:
            # 合并失败，存在环，返回false
            return False


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
            根据题目，存在冗余连接有以下俩种情况：
            1.根节点存在父节点，这样所有的节点的度为 1
            2.非根节点和其余非根节点存在连接，这样有一个节点的度为2
        """
        n = len(edges)
        # 检查是否存在入度为2的结点
        cnt = [0] * (n + 1)
        for s, e in edges:
            cnt[e] += 1
        node = 0
       # cnt中的索引对应是图中的结点， 编号：1~N
        for idx, num in enumerate(cnt):
            if num == 2:
                node = idx
                break

        # 情况1：如果不存在入度为2的点，做法和冗余连接1一样
        if node == 0:
            # 实例化一个并查集
            utf = DisJoinSet(n)
            for s, e in edges:
                if not utf.union(s, e):
                    # 合并失败，说明加入这条边后，就存在环了，此时这条边就是答案了
                    return [s, e]

        # 情况2：如果存在入度为2的点
        if node != 0:
            utf = DisJoinSet(n)
            # 找到与入度为2的点相连的两条边，因为只添加一条额外边，所以在
            # delete长度为2时，结束循环
            delete = []
            for s, e in edges:
                if e == node:
                    delete.append([s, e])
                    if len(delete) > 1:
                        break
            # 题目要求删除最后出现的边，选择delete中的最后一个元素
            last_s, last_e = delete[-1]
            for s, e in edges:
                # 不将边[last_s, last_e]添加到并查集中
                if s == last_s and e == last_e:
                    continue
                utf.union(s, e)
            # 如果连通分量为1， 说明不加边delete[-1]， 整个图能连通，不存在环，delete[-1]就是要删除的边
            if utf.cnt == 1:
                return delete[-1]
            else:
                # 反之delete[0]就是要删除的边。
                return delete[0]


if __name__ == '__main__':
    s = Solution()
    c = s.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]])
    print(c)
