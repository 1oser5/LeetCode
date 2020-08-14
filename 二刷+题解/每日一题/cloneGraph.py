# -*- encoding: utf-8 -*-
'''
@File    :   cloneGraph.py
@Time    :   2020/08/12 16:17:50
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    # dfs solution
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}

        def dfs(node):
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)

    # bfs solutions
    def cloneGraph1(self, node: 'Node') -> 'Node':
        lookup = {}

        def bfs(node):
            if not node: return
            clone = Node(node.val, [])
            lookup[node] = clone
            from collections import deque
            queue = deque([node])
            while queue:
                cur = queue.leftpop()
                for n in cur.neighbors:
                    if n not in lookup:
                        n = Node(n.val, [])
                        queue.append(n)
                    lookup[cur].neighbors.append(lookup[n])
            return clone
        return bfs(node)




if __name__ == '__main__':
    pass