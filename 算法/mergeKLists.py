#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mergeKLists.py
@Time    :   2019/12/17 15:25:31
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        for index in range(len(lists)-1):
            p1 = lists[index] 
            p2 = lists[index+1]
            q = ListNode(0)
            s = q
            while p1 and p2:
                if p1.val < p2.val:
                    s.next = p1
                    p1 = p1.next
                else:
                    s.next = p2
                    p2 = p2.next
                s = s.next
            s.next = p1 if p1 else p2
            lists[index+1] = q.next
        return lists[-1]
    
    def mergeK(self, lists):
        """合并到一个数组，在进行排序 92 ms	16.6 MB	"""
        node = []
        head = ListNode(0)
        dummy = head
        for i in lists:
            while i:
                node.append(i.val)
                i = i.next
        for j in sorted(node):
            dummy.next = ListNode(j)
            dummy = dummy.next
        return head.next
if __name__ == '__main__':
    pass