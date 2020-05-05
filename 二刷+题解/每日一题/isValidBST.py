#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   isValidBST.py
@Time    :   2020/05/05 20:33:12
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def bst(root, left, right):
            if not root:
                return True
            if root.val <= left or root.val >= right:
                return False
            return bst(root.left, left, root.val) and bst(root.right, root.val, right)

        return bst(root, float('-inf'), float('inf'))
if __name__ == '__main__':
    s = Solution()
    s.isValidBST()