#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mergeKLists.py
@Time    :   2020/04/26 13:08:53
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """ 超时 """
        if not lists:
            return
        head = None
        for l in lists:
            head = self.mergeList(head, l)
        return head

    def mergeList(self, l1, l2):
        p = ListNode(-1)
        head = p

        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        if l2:
            p.next = l2
        if l1:
            p.next = l1
        return head.next


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(-1)
        p = dummy
        head = []
        n = len(lists)
        for i in range(n):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, index = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[index]:
                heapq.heappush(head, (lists[i], i))
                lists[index] = lists[index].next
        return dummy.next




if __name__ == '__main__':
    pass