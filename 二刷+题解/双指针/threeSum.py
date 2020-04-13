#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   threeSum.py
@Time    :   2020/04/12 17:43:09
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for k in range(0, len(nums) -1):
            # 跳过重复解
            if k > 0 and nums[k] == nums[k-1]:
                continue
            # 不存在解
            if nums[k] > 0:
                break
            start = k+1
            end = len(nums) - 1
            while start < end:
                s = nums[k] + nums[start] + nums[end]
                if s < 0:
                    start += 1
                elif s > 0:
                    end -= 1
                else:
                    res.append([nums[k], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    # 去重
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
        return res

if __name__  == '__main__':
    s = Solution()
    #c = s.threeSum([-1, 0, 1, 2, -1, -4])
    #c = s.threeSum([0, 0, 0])
    c = s.threeSum([-2,0,1,1,2])
    print(c)