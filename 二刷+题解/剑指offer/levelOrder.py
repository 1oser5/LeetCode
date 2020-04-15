#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   levelOrder.py
@Time    :   2020/04/15 09:30:31
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root, level):
            if not root:
                return
            if len(res) - 1 < level:
                res.append([])
            res[level].append(root)
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        return res

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        """ 队列 """
        from collections import deque
        if not root:
            return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            temp = []
            # 这里 queue 不会一直刷新
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res

if __name__ == '__main__':
    pass