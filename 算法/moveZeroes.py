#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   moveZeroes.py
@Time    :   2019/11/11 21:51:59
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
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
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        264 ms	14.9 MB
        """
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                for j in range(i+1,length):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        return nums
    def moveZeroes2(self,nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes2([0,1,0,3,12]))