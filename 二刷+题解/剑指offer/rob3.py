#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   rob3.py
@Time    :   2020/05/08 21:37:39
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
    def rob(self, root: TreeNode) -> int:
        ''' 备忘录居然ac不 '''
        memory = {}

        def helper(root):
            if not root:
                return 0
            if root in memory:
                return memory[root]
            do = root.val
            if root.left:
                do += self.rob(root.left.right) + self.rob(root.left.left)
            if root.right:
                do += self.rob(root.right.right) + self.rob(root.right.left)
            not_do = self.rob(root.right) + self.rob(root.left)
            res = max(do, not_do)
            memory.update({root: res})
            return res
        return helper(root)

    def rob1(self, root: TreeNode) -> int:
        ''' dp用到这题真的猛男, 0 表示不偷，1 表示偷 '''

        def helper(root):
            if not root:
                return [0, 0]
            res = [0, 0]

            l = helper(root.left)
            r = helper(root.right)

            res[0] = max(l) + max(r)  # 当前节点不偷，返回孩子节点最大值（偷或者不偷）
            res[1] = l[0] + r[0] + root.val  # 当前节点偷，返回孩子节点不偷

            return res
        res = helper(root)
        return max(res)

if __name__ == '__main__':
    s = Solution()
    #[3,2,3,null,3,null,1]
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(1)
    s.rob(root)

