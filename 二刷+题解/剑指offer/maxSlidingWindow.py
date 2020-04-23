#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxSlidingWindow.py
@Time    :   2020/04/22 16:49:20
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ 递减单调栈 """
        deque = []
        res = []
        n = len(nums)
        for i in range(n):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            while i - deque[0] > k - 1:
                deque.pop(0)
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res



if __name__ == '__main__':
    s = Solution()
    # c = s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
    c = s.maxSlidingWindow([7,2,4], 2)
    print(c)