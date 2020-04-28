#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   moveZeroes.py
@Time    :   2020/04/28 09:19:53
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pre = 0
        for i in range(n):
            if nums[i] != 0 and nums[pre] == 0:
                nums[i], nums[pre] = nums[pre], nums[i]
            while nums[pre] != 0 and pre < i:
                pre += 1
        print(nums)

    def moveZeroes1(self, nums: List[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        print(nums)

if __name__ == '__main__':
    s = Solution()
    s.moveZeroes1([0,1,0,3,12])
    s.moveZeroes1([1,0, 1])