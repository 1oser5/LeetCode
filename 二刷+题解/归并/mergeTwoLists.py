#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mergeTwoLists.py
@Time    :   2020/04/13 15:37:12
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
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
        dum = l = ListNode(0)
        while l2 or l1:
            if l2.val > l1.val:
                cur = ListNode(l1.val)
                l1 = l1.next
            else:
                cur = ListNode(l2.val)
                l2 = l2.next
            l.next = cur
            l = l.next
        l.next = l2
        l.next = l1
        return dum.next




if __name__ == '__main__':
    pass