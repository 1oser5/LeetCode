#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   preorderTraversal.py
@Time    :   2020/04/07 16:32:37
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """ 递归 """
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        """ 迭代 """
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack:
            tail = stack.pop()
            ans.append(tail.val)
            if tail.right:  # 先检查右子节点
                stack.append(tail.right)
            if tail.left:  # 再检查左子节点， 这样出栈时就是先左后右的顺序
                stack.append(tail.left)
        return ans

if __name__ == '__main__':
    pass