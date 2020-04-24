#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pathSum.py
@Time    :   2020/04/24 08:24:25
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
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        def helper(node, temp, cur):
            if cur == 0 and not (node.left or node.right):
                res.append(temp)
                return
            if node.left:
                helper(node.left, temp + [node.left.val], cur-node.left.val)
            if node.right:
                helper(node.right, temp + [node.right.val], cur-node.right.val)
        helper(root, [root.val], sum-root.val)
        return res
if __name__ == '__main__':
    pass