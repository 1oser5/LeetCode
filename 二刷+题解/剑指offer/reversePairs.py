#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   reversePairs.py
@Time    :   2020/04/24 07:25:07
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.merge_sort(nums, 0, len(nums)-1, [])
        return self.cnt

    def merge(self, nums, start, mid, end, temp):
        i, j = start, mid+1
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                self.cnt += mid - i + 1
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= end:
            temp.append(nums[j])
            j += 1

        for i in range(len(temp)):
            nums[start+i] = temp[i]
        temp.clear()

    def merge_sort(self, nums, start, end, temp):
        if start >= end:
            return
        mid = (start + end) >> 1
        self.merge_sort(nums, start, mid, temp)
        self.merge_sort(nums, mid + 1, end, temp)
        self.merge(nums, start, mid, end, temp)



if __name__ == '__main__':
    s = Solution()
    s.reversePairs([7,5,6,4])