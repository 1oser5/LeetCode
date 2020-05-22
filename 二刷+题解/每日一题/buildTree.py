#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   buildTree.py
@Time    :   2020/05/22 08:55:19
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
if __name__ == '__main__':
    pass