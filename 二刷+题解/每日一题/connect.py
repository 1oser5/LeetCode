# -*- encoding: utf-8 -*-
'''
@File    :   connect.py
@Time    :   2020/09/28 09:43:01
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
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
        # 层级遍历
        if not root:
            return
        stack = [(root, 0)]
        while True:
            node, level = stack.pop(0)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
            if not stack:
                break
            if level == stack[0][1]:
                node.next = stack[0][0]
        return root

if __name__ == '__main__':
    pass