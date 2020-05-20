#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   listOfDepth.py
@Time    :   2020/05/20 21:04:48
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

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        from collections import deque
        stack = deque()
        stack.append(tree)
        res = []
        while stack:
            temp = ListNode(0)
            head = temp
            size = len(stack)
            for _ in range(size):
                node = stack.popleft()
                if not node:
                    continue
                temp.next = ListNode(node.val)
                temp = temp.next
                stack.append(node.left)
                stack.append(node.right)
            if head.next:
                res.append(head.next)
        return res

if __name__ == '__main__':
    pass