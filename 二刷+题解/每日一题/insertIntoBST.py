# -*- encoding: utf-8 -*-
'''
@File    :   insertIntoBST.py
@Time    :   2020/09/30 08:08:31
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST1(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        pos = root
        while pos:
            if val < pos.val:
                if pos.left:
                    pos = pos.left
                else:
                    pos.left = TreeNode(val)
                    break
            else:
                if pos.right:
                    pos = pos.right
                else:
                    pos.right = TreeNode(val)
                    break
        return root

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


if __name__ == '__main__':
    pass
