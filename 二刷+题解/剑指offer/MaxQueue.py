#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   MaxQueue.py
@Time    :   2020/04/26 15:18:47
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class MaxQueue(object):

    def __init__(self):
        from collections import deque
        self.que = deque()
        self.sort_que = deque()

    def max_value(self) -> int:
        return self.sort_que[0] if self.sort_que else -1

    def push_back(self, value: int) -> None:
        self.que.append(value)
        while self.sort_que and self.sort_que[-1] < value:
            self.sort_que.pop()
        self.sort_que.append(value)

    def pop_front(self) -> int:
        if not self.que: return -1
        res = self.que.popleft()
        if res == self.sort_que[0]:
            self.sort_que.popleft()
        return res



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
if __name__ == '__main__':
    pass