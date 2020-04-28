#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   sortList.py
@Time    :   2020/04/28 08:25:36
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None   # 这里要截断链表，需要把slow.next赋为None
        l = self.sortList(head)
        r = self.sortList(mid)
        h = ListNode(0)
        dummy = h
        while l and r:
            if l.val < r.val:
                h.next, l = l, l.next
            else:
                h.next, r = r, r.next
            h = h.next
            h.next = l or r
        return dummy.next
if __name__ == '__main__':
    pass