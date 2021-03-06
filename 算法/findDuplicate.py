#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findDuplicate.py
@Time    :   2019/12/17 13:37:30
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = sorted(nums)
        pre = float('inf')
        for i in s:
            if i == pre:
                return pre
            i = pre
    def findD(self, nums):
        """二分查找"""
        right = len(nums) - 1
        left = 1
        count = 0
        while left < right:
            mid = (left + right) // 2
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
    def findDD(self, nums):
        """快慢指针"""
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        find = 0
        while True:
            find = nums[find]
            slow = nums[slow]
            if slow == find:
                return find
if __name__ == '__main__':
    pass