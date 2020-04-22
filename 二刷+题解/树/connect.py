#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   connect.py
@Time    :   2020/04/22 10:48:17
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """ 空间复杂度 n 复杂度 """
        from collections import deque
        if not root:
            return
        Q = deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root

    def connect1(self, root: 'Node') -> 'Node':
        if not root:
            return
        left_most = root
        while left_most.left:
            head = left_most
            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next
            left_most = left_most.left

        return root


if __name__ == '__main__':
    pass