# -*- encoding: utf-8 -*-
'''
@File    :   postorderTraversal.py
@Time    :   2020/09/29 08:13:30
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        巧妙迭代，利用前序遍历和后序遍历的相似性


        前序遍历:
        root, left, right

        后序遍历:
        left, right, root

        后序遍历可以通过前序遍历反转 left, right 位置再倒序得到, holy shit!
        """
        if not root:
            return
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            # 注意入栈顺序
            stack.append(node.left)
            stack.append(node.right)
        return res[::-1]

if __name__ == '__main__':
    pass