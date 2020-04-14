#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minDepth.py
@Time    :   2020/04/14 17:50:10
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(not root): return 0
        if(not root.left): return self.minDepth(root.right)+1
        if(not root.right): return self.minDepth(root.left)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
if __name__ == '__main__':
    pass