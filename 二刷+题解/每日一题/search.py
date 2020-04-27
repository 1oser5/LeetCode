#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   search.py
@Time    :   2020/04/27 09:27:17
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        if target == nums[0]:
            return 0
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif target < nums[left]:
                if nums[mid] < target or nums[mid] >= nums[left]:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            else:
                if nums[mid] < nums[left] or nums[mid] > target:
                    right = mid - 1
                if nums[mid] >= nums[left] and nums[mid] < target:
                    left = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    #c = s.search([4,5,6,7,0,1,2], 0)
   # c = s.search([1], 2)#
    c = s.search([3,1], 1)#
    print(c)