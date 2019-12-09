#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   isValidBST.py
@Time    :   2019/12/09 15:00:49
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
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
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            """bfs"""
            if not node: return True
            val = node.val
            if val <= lower or val >= upper: return False
            if not helper(root.right, val, upper):
                return False
            if not helper(root.left, lower, val):
                return False
            return True
        return helper(root)

    def isBST(self, root: TreeNode) -> bool:
        """dfs"""
        if not root: return True
        stack = [root.val, float('-inf'), float('inf')]
        while stack:
            if not root: continue
            root, lower, upper = stack.pop()
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append(root.right, val, upper)
            stack.append(root.left, lower, val)
        return True
    def BST(self, root: TreeNode) -> bool:
        """中序遍历"""
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder: return False
            inorder = root.val
            root = root.right
        return True
if __name__ == '__main__':
    pass