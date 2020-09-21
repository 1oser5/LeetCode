# -*- encoding: utf-8 -*-
'''
@File    :   convertBST.py
@Time    :   2020/09/21 08:16:48
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
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
    s = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.convertBST(root.right)
        self.s += root.val
        root.val = self.s
        self.convertBST(root.left)
        return root

if __name__ == '__main__':
    pass