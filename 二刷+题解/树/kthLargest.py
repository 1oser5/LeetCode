#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   kthLargest.py
@Time    :   2020/04/14 20:57:07
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
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []

        def helper(root):
            if root.left:
                helper(root.left)
            res.append(root.val)
            if root.right:
                helper(root.right)
        helper(root)
        return res[-k]

if __name__ == '__main__':
    pass