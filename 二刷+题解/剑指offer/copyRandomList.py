#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   copyRandomList.py
@Time    :   2020/04/23 13:43:10
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            c = Node(node.val, None, None)
            visited[node] = c
            c.next = dfs(node.next)
            c.random = dfs(node.random)
            return c
        return dfs(head)


if __name__ == '__main__':
    pass