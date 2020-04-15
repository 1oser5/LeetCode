#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findRepeatNumber.py
@Time    :   2020/04/15 10:25:22
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums[abs(i)] < 0:
                return i
            nums[i] = -nums[i]


    def findRepeatNumber1(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            else:
                return i


if __name__ == '__main__':
    pass