#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lowestCommonAncestor1.py
@Time    :   2020/04/15 17:23:28
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val: return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        return root if l and r else l or r



if __name__ == '__main__':
    pass