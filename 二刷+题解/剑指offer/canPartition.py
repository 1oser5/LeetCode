#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   canPartition.py
@Time    :   2020/05/15 19:06:26
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
# here put the import lib
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memory = set()

        def helper(l, cur, k):
            if cur == k and sum(l) == k:
                return True
            if cur > k or cur in memory:
                return False
            memory.add(cur)
            n = len(l)
            for i in range(n):
                if helper(l[:i] + l[i+1:], cur + l[i], k):
                    return True
        return helper(nums, 0, sum(nums)//2) or False
if __name__ == '__main__':
    s = Solution()
    c = s.canPartition([1, 5, 11, 5])
    c = s.canPartition([1, 2, 3, 5])
    print(c)