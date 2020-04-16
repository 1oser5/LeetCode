#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   MinStack.py
@Time    :   2020/04/16 17:46:38
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackB = []
        self.stackA = []


    def push(self, x: int) -> None:
        self.stackA.append(x)
        if not self.stackB or self.stackB[-1] >= x:
            self.stackB.append(x)


    def pop(self) -> None:
        c = self.stackA.pop()
        if self.stackB[-1] == c:
            self.stackB.pop()


    def top(self) -> int:
        return self.stackA[-1]

    def min(self) -> int:
        return self.stackB[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
if __name__ == '__main__':
    pass