#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   reverseList.py
@Time    :   2020/04/15 08:47:13
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = []
        if not head:
            return
        if not head.next:
            return head
        def helper(prev, cur):
            if cur.next:
                helper(cur, cur.next)
            else:
                res.append(cur)
            cur.next = prev
            prev.next = None
        helper(head, head.next)
        return res[0]
    def reverseList(self, head: ListNode) -> ListNode:
        """ 链表的题目，多想想双指针吧 """
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    head = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    s = Solution()
    c = s.reverseList(head)
    print(c.val)
