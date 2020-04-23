#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   buildTree.py
@Time    :   2020/04/23 14:27:28
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。


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

        def helper(pre_root, in_left, in_right):
            if in_left > in_right:
                return
            i = self.reverse[self.po[pre_root]]
            node = TreeNode(self.po[pre_root])
            node.left = helper(pre_root+1, in_left, i-1)
            node.right = helper(i-in_left+pre_root+1, i+1 , in_right)
            return node

        self.reverse, self.po = {}, preorder
        for i in range(len(inorder)):
            self.reverse[inorder[i]] = i
        return helper(0, 0, len(inorder)-1)




if __name__ == '__main__':
    pass