#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   sortList.py
@Time    :   2019/12/14 14:45:21
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
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
        p = head
        pre = None
        while p.next:
            s = p
            while s.next:
                if s.val > s.next.val:
                    s.next = s.next.next
                    s.next.next = s
                    if pre:
                        pre.next = s.next
                s = s.next
            p = p.next
if __name__ == '__main__':
    pass