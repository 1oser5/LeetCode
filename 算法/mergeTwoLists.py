#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mergeTwoLists.py
@Time    :   2019/11/11 21:32:00
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''	68 ms	13.8 MB'''
        head = ListNode(-1)
        l = head
        while l1 and l2:
            if l1.val <= l2.val:
               l.next = l1
               l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        l.next = l1 if l1 is not None else l2
        return head.next


if __name__ == '__main__':
    pass