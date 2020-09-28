# -*- encoding: utf-8 -*-
'''
@File    :   findMode.py
@Time    :   2020/09/27 08:40:23
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        current, count, maxCount = 0, 0, 0
        res = []

        def inOrderTraversal(root):
            if not root:
                return
            nonlocal res, current, count, maxCount
            inOrderTraversal(root.left)
            curVal = root.val
            if curVal == current:
                count += 1
            else:
                current = curVal
                count = 1
            if count == maxCount:
                res.append(current)
            elif count > maxCount:
                res = [curVal]
                maxCount = count
            inOrderTraversal(root.right)
        inOrderTraversal(root)
        return res




if __name__ == '__main__':
    pass