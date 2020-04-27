#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   isSubStructure.py
@Time    :   2020/04/26 17:22:05
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
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False
        if not A:
            return False
        if self.isSame(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def isSame(self, t1, t2):
        if t2:
            if not t1:
                return False
            if t1.val != t2.val:
                return False
            l = self.isSame(t1.left, t2.left)
            r = self.isSame(t1.right, t2.right)
            return l and r
        return True

    def isSame(self, t1, t2):
        if t2:
            if not t1:
                return False
            if t1.val != t2.val:
                return False
            l = self.isSame(t1.left, t2.left)
            r = self.isSame(t1.right, t2.right)
            return l and r
        return True




if __name__ == '__main__':
    pass