#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findDuplicate.py
@Time    :   2020/05/20 16:01:46
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ''' 二分查找 '''
        size = len(nums)
        left = 1
        right = size - 1
        while left < right:
            mid = left + (right - left) // 2  # 防止越界
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left


    def findDuplicate2(self, nums: List[int]) -> int:
        ''' 快慢指针 wise'''
        fast = nums[nums[0]]
        slow = nums[0]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow





if __name__ == '__main__':
    s = Solution()
    s.findDuplicate([1,3,4,2,2])