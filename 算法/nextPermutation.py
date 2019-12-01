#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   nextPermutation.py
@Time    :   2019/12/01 10:56:44
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstIndex = -1
        n = len(nums)
        def reverse(nums, i, j):
            while i < j:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                firstIndex = i
                break
        #print(firstIndex)
        if firstIndex == -1:
            reverse(nums, 0, n-1)
            return 
        secondIndex = -1
        for i in range(n-1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        nums[firstIndex],nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums, firstIndex+1, n-1)
        print(nums)
if __name__ == '__main__':
    s = Solution()
    # s.nextPermutation([3,2,1])
    # s.nextPermutation([1,2,3])
    s.nextPermutation([1,2,7,4,1,3])