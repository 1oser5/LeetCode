#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   jump.py
@Time    :   2020/04/17 09:17:23
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        end = 0
        _max = 0
        res = 0
        for i in range(n):
            _max = max(_max, i+nums[i])
            if i == end:
                res += 1
                end = _max
        return res



if __name__ == '__main__':
    pass