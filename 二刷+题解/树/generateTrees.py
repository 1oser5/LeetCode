#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   generateTrees.py
@Time    :   2020/04/08 10:32:01
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(start, end):
            all_trees = []
            if start > end:
                return [None,]

            for index in range(start, end):
                left_trees = helper(start, index)

                right_trees = helper(index+1, end)

                for l in left_trees:
                    for r in right_trees:
                        cur = TreeNode(index)
                        cur.left = l
                        cur.right = r
                        all_trees.append(cur)
            return all_trees
        all_trees = helper(1, n+1)
        return all_trees

if __name__ == '__main__':
    s = Solution()
    s.generateTrees(3)