#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   numberOfSubarrays.py
@Time    :   2020/04/21 16:40:10
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        n = len(nums) - 1
        cur = 0
        res = 0
        while right <= n:
            if nums[right] & 1 == 1:
                cur += 1
            right += 1
            if cur == k:
                prev_right = right
                while right <= n and nums[right] & 1 == 0:
                    right += 1
                prev_left = left
                while nums[left] & 1 == 0:
                    left += 1
                res += (left+1-prev_left) * (right+1-prev_right)
                left += 1
                cur -= 1
        return res

if __name__ == '__main__':
    # s = Solution()
    # c = s.numberOfSubarrays([1,1,2,1,1], 3)
    # print(c)
    print(3&1)
    print(4&1)
    print(10&1)