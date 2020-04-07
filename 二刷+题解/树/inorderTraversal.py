#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   inorderTraversal.py
@Time    :   2020/04/07 15:23:34
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """ 递归做法 """
        res = []
        if not root:
            return res

        def helper(root):
            if root.left:
                helper(root.left)
            res.append(root.val)
            if root.right:
                helper(root.right)
        helper(root)
        return res

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """ 迭代算法 """
        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res

    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        """ 双色标记法 """
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if color == GRAY:
                res.append(node.val)
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
        return res

if __name__ == '__main__':
    pass