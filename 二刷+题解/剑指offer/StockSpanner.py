#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   StockSpanner.py
@Time    :   2020/05/13 21:50:42
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append((price, ans))
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == '__main__':
    pass