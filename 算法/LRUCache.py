#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   LRUCache.py
@Time    :   2019/12/28 14:15:04
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

class Node(object):
    def __init__(self, key, value):
        self.next = None
        self.pre = None
        self.key = key
        self.value = value
# here put the import lib
class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self._remove(n)
            self._add(n)
            return self.d[key].value
        else: return -1
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            n = self.d[key]
            self._remove(n)
        new = Node(key, value)
        self._add(new)
        self.d[key] = new
        if len(self.d) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.d[n.key]
    def _remove(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p
    def _add(self, node):
        p = self.tail.pre
        p.next = node
        node.next = self.tail
        self.tail.pre = node
        node.pre = p
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    pass