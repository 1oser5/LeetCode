#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   detectCycle.py
@Time    :   2020/06/16 11:06:43
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
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while True:
            # no cycle
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next   # fast walk 2 step once
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
if __name__ == '__main__':
    pass