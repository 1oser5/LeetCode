#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   maxProduct.py
@Time    :   2020/05/12 09:11:39
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, imax, imin = float('-inf'), 1, 1
        for i in range(len(nums)):
            # 负数反转大小
            cur = nums[i]
            if cur < 0:
                imax, imin = imin, imax
            imax = max(cur, imax * cur)
            imin = min(cur, imin * cur)
            res = max(imax, res)
        return res



if __name__ == '__main__':
    s = Solution()
    #c = s.maxProduct([2,3,-2,4])
    #c = s.maxProduct([-2,0,-1])
    c = s.maxProduct([0, 2])
    #c = s.maxProduct([-4,-3])
    print(c)