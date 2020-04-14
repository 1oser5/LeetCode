#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   minSubArrayLen.py
@Time    :   2020/04/14 16:45:57
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not (s and nums):
            return 0
        min_l = float('inf')
        n = len(nums)
        left = 0
        cur = 0
        for i in range(n):
            cur += nums[i]
            while cur >= s:
                min_l = min((i+1-left), min_l)
                cur -= nums[left]
                left += 1
        return min_l if min_l != float('inf') else 0


if __name__ == '__main__':
    s = Solution()
    c = s.minSubArrayLen(7, [2,3,1,2,4,3])
    c = s.minSubArrayLen(3, [1,1])
    #c = s.minSubArrayLen(11, [1,2,3,4,5])
    print(c)