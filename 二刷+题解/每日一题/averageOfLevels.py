# -*- encoding: utf-8 -*-
'''
@File    :   averageOfLevels.py
@Time    :   2020/09/14 08:57:33
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = [root]
        res = []
        while stack:
            s, count = 0, 0
            # 保存了当前 stack的长度
            length = len(stack)
            for _ in range(length):
                cur = stack.pop(0)
                if not cur:
                    continue
                s += cur.val
                count += 1
                stack.append(cur.left)
                stack.append(cur.right)
            if count:
                res.append(s / count)
        return res
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    s = Solution()
    c = s.averageOfLevels(root)
    print(c)