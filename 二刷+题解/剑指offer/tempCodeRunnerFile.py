class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res = []

#         def helper(root, level):
#             if not root:
#                 return
#             if len(res) - 1 < level:
#                 res.append([])
#             res[level].append(root)
#             helper(root.left, level+1)
#             helper(root.right, level+1)
#         helper(root, 0)
#         return res
#     def levelOrder1(self, root: TreeNode) -> List[List[int]]:
#         """ 队列 """
#         from collections import deque
#         if not root:
#             return []
#         res, queue = [], deque()
#         queue.append(root)
#         while queue:
#             temp = []
#             # 这里 queue 不会一直刷新
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 temp.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(temp)
#         return res
