# -*- encoding: utf-8 -*-
'''
@File    :   binaryTreePaths.py
@Time    :   2020/09/04 08:29:00
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def traceback(root, cur):
            if not root:
                return
            cur += str(root.val)
            if not root.left and not root.right:
                res.append(cur)
            else:
                cur += '->'
            traceback(root.left, cur)
            traceback(root.right, cur)

        traceback(root, '')
        return res
if __name__ == '__main__':
    pass