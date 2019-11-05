#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   reverseList.py
@Time    :   2019/11/05 21:50:44
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''52 ms	19.4 MB'''
        if (head is None or head.next is None):
            return head
        cur = self.reverseList(head.next)
        # 下一个节点指向当前节点
        head.next.next = head
        #将当前节点指向None，防止环
        head.next = None
        return cur

if __name__ == '__main__':
    pass