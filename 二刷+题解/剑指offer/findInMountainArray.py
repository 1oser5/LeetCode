#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findInMountainArray.py
@Time    :   2020/04/29 08:18:59
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self):
        self.stack = [1,2,3,4,5,3,1]

    def get(self, index: int) -> int:
        return self.stack[index]

    def length(self) -> int:
        return len(self.stack)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left = 0
        right = n
        top = 0
        while left <= right:
            mid = (left + right) >> 1
            if mid < n - 1 and mountain_arr.get(mid) <= mountain_arr.get(mid+1):
                left = mid + 1
            elif mid > 1 and mountain_arr.get(mid) <= mountain_arr.get(mid-1):
                right = mid - 1
            else:
                top = mid
                break
        l, l_most = 0, top
        while l <= l_most:
            mid = (l + l_most) >> 1
            if mountain_arr.get(mid) < target:
                l = mid + 1
            elif mountain_arr.get(mid) > target:
                l_most = mid - 1
            else:
                return mid
        right_most = n - 1
        while top <= right_most:
            mid = (right_most + top) >> 1
            if mountain_arr.get(mid) < target:
                right_most = mid - 1
            elif mountain_arr.get(mid) > target:
                top = mid + 1
            else:
                return mid
        return -1



if __name__ == '__main__':
    s = Solution()
    m = MountainArray()
    c = s.findInMountainArray(3, m)
    print(c)