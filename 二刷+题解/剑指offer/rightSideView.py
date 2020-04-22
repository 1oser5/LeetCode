#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   rightSideView.py
@Time    :   2020/04/22 10:00:30
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView1(self, root: TreeNode) -> List[int]:
        """ dfs """
        res = []

        def dfs(root, depth):
            if not root:
                return
            if depth >= len(res):
                res.append(0)
            res[depth] = root.val
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, 0)
        return res

    def rightSideView2(self, root: TreeNode) -> List[int]:
        """ bfs """
        from collections import deque
        max_depth = -1
        q = deque([(root, 0)])
        right_val = dict()
        while q:
            node, depth = q.popleft()
            if node is None:
                continue
            max_depth = max(max_depth, depth)
            right_val.update({depth: node.val})
            q.append((node.left, depth+1))
            q.append((node.right, depth+1))
        return [right_val[depth] for depth in range(max_depth+1)]




if __name__ == '__main__':
    root  = TreeNode(1)
    l  = TreeNode(2)
    root.left = l
    r  = TreeNode(3)
    root.right = r
    s = TreeNode(5)
    b = TreeNode(4)
    r.right = b
    l.right = s
    c = Solution()
    c.rightSideView2(root)


