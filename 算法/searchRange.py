#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   searchRange.py
@Time    :   2019/12/02 20:30:14
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        l, r = 0, len(nums)-1
        while  l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        
        if not nums or nums[l] != target:
            return [-1, -1]
        
        a, b = l, len(nums)-1
        while a < b:
            mid = (a + b + 1) // 2
            if nums[mid] <= target:
                a = mid
            else:
                b = mid - 1
        return [l, a]
if __name__ == '__main__':
    pass