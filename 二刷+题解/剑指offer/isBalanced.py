#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   isBalanced.py
@Time    :   2020/04/17 08:36:15
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            if left == -1: return -1
            right = helper(root.right)
            if right == -1: return -1
            return max(right, left) + 1 if abs(right - left) <= 1 else -1
        return helper(root) != -1
if __name__ == '__main__':
    pass