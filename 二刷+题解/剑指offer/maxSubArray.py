#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxSubArray.py
@Time    :   2020/04/16 15:34:54
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = float('-inf')
        cur = 0
        for i in nums:
            cur += i
            m = max(cur, m)
            if cur < 0:
                cur = 0
        return m
if __name__ == '__main__':
    pass