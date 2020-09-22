# -*- encoding: utf-8 -*-
'''
@File    :   minCameraCover.py
@Time    :   2020/09/22 08:52:25
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
    res = 0
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 1
            left, right = dfs(root.left), dfs(root.right)
            if left == 0 or right == 0:
                self.res += 1
                return 2
            if left == 1 and right == 1:
                return 0
            if (left + right) >= 3:
                return 1
            return -1
        if dfs(root) == 0:
            self.res += 1
        return self.res

if __name__ == '__main__':
    pass