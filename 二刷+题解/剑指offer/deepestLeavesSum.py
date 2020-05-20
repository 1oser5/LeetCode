#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   deepestLeavesSum.py
@Time    :   2020/05/20 21:32:41
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        from collections import deque
        stack = deque()
        stack.append(root)
        res = []
        while stack:
            temp = []
            size = len(stack)
            for _ in range(size):
                node = stack.popleft()
                if not node:
                    continue
                stack.append(node.left)
                stack.append(node.right)
                temp.append(node.val)
            if temp:
                res.append(temp)
        return sum(res[-1])
if __name__ == '__main__':
    pass