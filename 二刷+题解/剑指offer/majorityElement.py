#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   majorityElement.py
@Time    :   2020/04/15 20:07:09
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ case 43 超时 """
        def quick_sort(l, left, right):
            if left >= right:
                return
            low = left
            high = right
            povit = l[left]
            while left < right:
                while left < right and l[right] >= povit:
                    right -= 1
                l[left] = l[right]
                while left < right and l[left] <= povit:
                    left += 1
                l[right] = l[left]
            l[left] = povit
            quick_sort(l, low, left-1)
            quick_sort(l, left+1, high)
            return l
        l = quick_sort(nums, 0, len(nums)-1)
        return l[(0+len(l)-1)//2]


    def majorityElement1(self, nums: List[int]) -> int:
        val = 0
        for i in nums:
            if val == 0:
                most = i
            if i != most:
                val -= 1
            else:
                val += 1
        return most

if __name__ == '__main__':
    s = Solution()
    c = s.majorityElement1([1, 2, 3, 2, 2, 2, 5, 4, 2])
    print(c)
