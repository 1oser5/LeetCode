#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   removeNthFromEnd.py
@Time    :   2020/06/15 10:42:27
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)  # Fantastic dummy node
        dummy.next = head
        fast = low = dummy
        # fast walk to reciprocal n node, because of dummy node
        # so fast need walk l n + 1 steps
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            low = low.next
        low.next = low.next.next
        return dummy.next
if __name__ == '__main__':
    pass