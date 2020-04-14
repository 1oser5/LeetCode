#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   addTwoNumbers.py
@Time    :   2020/04/14 08:50:47
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def get_stack(l):
            stack = []
            while l:
                stack.append((l.val))
                l = l.next
            return stack
        stack1 = get_stack(l1)
        stack2 = get_stack(l2)

        ans = None
        add = 0
        while stack1 or stack2 or add:
            a = 0 if not stack1 else stack1.pop()
            b = 0 if not stack2 else stack2.pop()
            cur = a + b + add
            add = cur // 10
            cur %= 10
            node = ListNode(cur)
            node.next = ans
            ans = node
        return ans




if __name__ == '__main__':
    print(5//10)