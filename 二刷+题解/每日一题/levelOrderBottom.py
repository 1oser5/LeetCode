# -*- encoding: utf-8 -*-
'''
@File    :   levelOrderBottom.py
@Time    :   2020/09/08 08:19:51
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(root, depth):
            if not root:
                return
            if len(res) < depth:
                res.append([])
            res[depth-1].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1)
        return res[::-1]
if __name__ == '__main__':
    pass