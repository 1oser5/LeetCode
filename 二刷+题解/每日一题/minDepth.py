# -*- encoding: utf-8 -*-
'''
@File    :   minDepth.py
@Time    :   2020/08/25 10:06:36
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
    def minDepth(self, root: TreeNode) -> int:
        ans = 0
        if not root.left and root.right:
            ans = 1
        elif root.right and root.left:
            ans = min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left:
            ans = self.minDepth(root.left) + 1
        else:
            ans = self.minDepth(root.right) + 1
        return ans
if __name__ == '__main__':
    pass