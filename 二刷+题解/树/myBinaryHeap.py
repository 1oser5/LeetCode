#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   myBinaryHeap.py
@Time    :   2020/04/14 11:16:12
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   手写一个最大堆
'''

# here put the import lib


class MaxPQ(object):
    """ 最大堆 """

    def __init__(self):
        self.pq = [0]
        self.length = 0

    def parent(self, root):
        """ 父节点的索引 """
        return root // 2

    def right(self, root):
        """ 父节点的索引 """
        return root * 2 + 1

    def left(self, root):
        """ 父节点的索引 """
        return root * 2

    def max(self):
        """ 返回最大值 """
        return self.pq[1]

    def insert(self, e):
        """ 插入元素 """
        self.length += 1
        self.pq.append(e)
        self.swim(self.length)

    def delMax(self):
        """ 删除并返回当前队列中最大元素 """
        m = self.pq[1]
        self.exch(1, self.length)
        self.pq.pop()
        self.length -= 1
        self.sink(1)
        return m

    def swim(self, k):
        """ 上浮第 k 个元素，以维护最大堆性质 """
        while k > 1 and self.less(self.parent(k), k):
            self.exch(self.parent(k), k)
            k = self.parent(k)

    def sink(self, k):
        """ 下沉第 k 个元素，以维护最大堆性质 """
        while self.left(k) <= self.length:
            older = self.left(k)
            if self.right(k) <= self.length and self.less(older, self.right(k)):
                older = self.right(k)
            # k 比俩孩子都大
            if self.less(older, k):
                break
            self.exch(k, older)
            k = older

    def exch(self, i, j):
        """ 交换数组的两个元素 """
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def less(self, i, j):
        """ 交换数组的两个元素 """
        return self.pq[i] < self.pq[j]

    def show(self):
        print(self.pq[1:])


if __name__ == '__main__':
    pq = MaxPQ()
    pq.insert(1)
    pq.insert(2)
    pq.insert(3)
    pq.insert(7)
    pq.insert(5)
    pq.show()
    pq.delMax()
    pq.show()


