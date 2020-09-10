# -*- encoding: utf-8 -*-
'''
@File    :   rotateRight.py
@Time    :   2020/09/10 13:30:24
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        length = 1
        mark = head
        # 计算链表长度
        while mark.next:
            length += 1
            mark = mark.next
        # 取余数
        k %= length
        fast, slow = head, head
        while k > 0 and fast.next:
            fast = fast.next
            k -= 1
        # 整除情况直接返回head
        if fast == slow:
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    s = Solution()
    c = s.rotateRight(l, 2)
    print(c.val)