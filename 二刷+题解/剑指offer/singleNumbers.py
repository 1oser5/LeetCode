#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   singleNumbers.py
@Time    :   2020/04/23 14:01:27
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0
        a = 0
        b = 0
        for num in nums:
            ret ^= num
        h = 1
        while (h & ret == 0):
            h <<= 1
        for num in nums:
            print(h,num)
            if (h & num == 0):
                a ^= num
            else:
                b ^= num
        return [a, b]
if __name__ == '__main__':
    s = Solution()
    c = s.singleNumbers([1,2,5,2])
    print(c)