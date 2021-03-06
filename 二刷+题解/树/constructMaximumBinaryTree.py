#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   constructMaximumBinaryTree.py
@Time    :   2020/04/14 21:05:11
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

 

示例 ：

输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    /
     2  0
       \
        1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def helper(l):
            if not l:
                return
            m = max(l)
            for i, v in enumerate(l):
                # 最大值
                if v == m:
                    node = TreeNode(v)
                    node.left = helper(l[:i])
                    node.right = helper(l[i+1:])
                    return node
        return helper(nums)


if __name__ == '__main__':
    s = Solution()
    s.constructMaximumBinaryTree([3,2,1,6,0,5])