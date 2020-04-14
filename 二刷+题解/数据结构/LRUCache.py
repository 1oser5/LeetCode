#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   LRUCache.py
@Time    :   2020/04/14 12:43:56
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   使用双向链表配合哈希表完成 LRU（Least Recently Used）算法
'''


class Node(object):
    """ 节点类 """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoubleList(object):
    """ 双向链表 """
    def __init__(self):
        self.length = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addFirst(self, node):
        """ 头部插入 """
        # 非空链表
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.length += 1

    def remove(self, node):
        """ 删除链表中的 node 节点 """
        p = self.head.next
        while p:
            if p.value == node.value and p.key == node.key:
                p.prev.next = p.next
                p.next.prev = p.prev
                self.length -= 1
                return

    def removeLast(self):
        """ 删除链表中最后一个节点，并返回该节点 """
        n = self.tail.prev
        n.prev.next = self.tail
        self.tail.prev = n.prev
        return n

    def __len__(self):
        return self.length

    def show(self):
        p = self.head.next
        while p:
            print(p.key, p.value)
            p = p.next


if __name__ == '__main__':
    D = DoubleList()
    n = Node(1, 2)
    D.addFirst(n)
    D.addFirst(n)
    D.show()
