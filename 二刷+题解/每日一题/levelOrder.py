#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   levelOrder.py
@Time    :   2020/05/13 09:20:40
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            temp = []
            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                if node:
                    temp.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if temp:
                res.append(temp)
        return res
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s.levelOrder(root)