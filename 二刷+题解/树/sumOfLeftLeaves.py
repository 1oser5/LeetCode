#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   sumOfLeftLeaves.py
@Time    :   2020/04/14 17:37:11
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = [0]
        if not root:
            return 0

        def helper(root, isLeft):
            if isLeft and not (root.left or root.right):
                res[0] += root.val
            if root.left:
                helper(root.left, True)
            if root.right:
                helper(root.right, False)
        helper(root, False)
        return res[0]
if __name__ == '__main__':
    pass