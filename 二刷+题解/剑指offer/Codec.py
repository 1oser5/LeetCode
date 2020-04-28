#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Codec.py
@Time    :   2020/04/28 15:11:00
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        from collections import deque
        stack = deque()
        stack.append(root)
        res = []
        while stack:
            node = stack.popleft()
            if not node:
                res.append('null')
                continue
            res.append(str(node.val))
            stack.append(node.left)
            stack.append(node.right)
        return '[' + ','.join(res) + ']'
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        from collections import deque
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    print("[1,2,3,null,null,4,5]"[1:-1].split(','))