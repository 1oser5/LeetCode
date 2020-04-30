#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxCoins.py
@Time    :   2020/04/30 09:05:57
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """ 一般回溯 超时"""

        res = [0]

        def helper(l, cur):
            if not l:
                res[0] = max(cur, res[0])
                return
            for i, v in enumerate(l):
                left = l[i-1] if i - 1 >= 0 else 1
                right = l[i+1] if i + 1 <= len(l) - 1 else 1
                helper(l[:i] + l[i+1:], cur + (left * v * right))
        helper(nums, 0)
        return res[0]


    def maxCoins1(self, nums: List[int]) -> int:

        def helper(start, end, nums, cache):
            if start == end - 1:
                return 0
            if (start, end) in cache:
                return cache[(start, end)]
            m = 0
            for i in range(start+1, end):
                temp = helper(start, i, nums, cache) + helper(i, end, nums, cache) + nums[start] * nums[end] * nums[i]
                m = max(temp, m)
            cache.update({(start, end): m})
            return m
        nums = [1] + nums + [1]
        return helper(0, len(nums)-1, nums, {})



if __name__ == '__main__':
    s = Solution()
    c = s.maxCoins([7,9,8,0,7,1,3,5,5,2])
    print(c)