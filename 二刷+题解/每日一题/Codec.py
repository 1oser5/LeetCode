#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Codec.py
@Time    :   2020/06/16 10:48:23
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
        def dfs(node):
            if not node:
                vals.append('#')
            else:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        vals = []
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            v = next(vals)
            if v == '#':
                return
            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node
        vals = iter(data.split(','))
        return dfs()


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    codec.deserialize(codec.serialize(root))