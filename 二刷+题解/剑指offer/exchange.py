#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   exchange.py
@Time    :   2020/04/16 14:59:46
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] & 1 == 1:
                left += 1
            while left < right and nums[right] & 1 == 0:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums


if __name__ == '__main__':
    s = Solution()
    c = s.exchange([1,2,3,4])
    print(c)