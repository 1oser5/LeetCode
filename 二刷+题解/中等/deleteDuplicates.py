#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   deleteDuplicates.py
@Time    :   2020/06/10 14:18:50
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        a = dummy
        b = head
        while b and b.next:
            if a.next.val != b.next.val:
                b = b.next
                a = a.next
            else:
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(4)
    n7 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    c = s.deleteDuplicates(n1)
    print(c)
