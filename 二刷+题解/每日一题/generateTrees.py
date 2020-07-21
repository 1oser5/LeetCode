#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   generateTrees.py
@Time    :   2020/07/21 11:23:44
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end + 1):
                left = generate(start, i - 1)
                right = generate(i + 1, end)

                for l in left:
                    for r in right:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        allTrees.append(cur)
            return allTrees
        return generate(1, n) if n else []
if __name__ == '__main__':
    pass