#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   inorderTraversal.py
@Time    :   2019/11/26 20:33:35
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        '''52 ms	13.8 MB'''
        res = []
        def foo(r):
            if r == None: return
            foo(r.left)
            res.append(r.val)
            foo(r.right)
        foo(root)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.inorderTraversal([1,None,2,3]))