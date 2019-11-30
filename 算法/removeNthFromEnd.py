#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   removeNthFromEnd.py
@Time    :   2019/11/30 10:38:45
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """	32 ms	13.7 MB"""
        # 增加一个特殊节点方便边界判断
        p = ListNode(-1)
        p.next,a,b = head,p,p
        # 第一个循环，b指针先往前走n步
        while n>0 and b:
            b,n = b.next,n-1
        # 假设整个链表长5，n是10，那么第一次遍历完后b就等用于空了
        # 于是后面的判断就不用做了，直接返回
        if not b:
            return head
        # 第二次，b指针走到链表最后，a指针也跟着走
        # 当遍历结束时，a指针就指向要删除的节点的前一个位置
        while b.next:
            a,b = a.next,b.next
        # 删除节点并返回	
        a.next = a.next.next
        return p.next	

if __name__ == '__main__':
    pass