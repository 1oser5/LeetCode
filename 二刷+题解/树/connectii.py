#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   connectii.py
@Time    :   2020/04/22 16:15:04
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

        while left_most.right or left_most.left:
            head = left_most
            while head:
                if head.next:
                    if head.right and head.left:
                        head.left.next = head.right
                    elif head.left and head.next.left:
                        head.left.next = head.next.left
                    elif head.left and head.next.right:
                        head.left.next = head.next.right
                    elif head.right and head.next.left:
                        head.right.next = head.next.left
                    elif head.right and head.next.right:
                        head.right.next = head.next.right

                head = head.next
            if left_most.left:
                left_most = left_most.left
            else:
                left_most = left_most.right
        return root









if __name__ == '__main__':
    pass