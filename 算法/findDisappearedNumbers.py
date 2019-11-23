#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   findDisappearedNumbers.py
@Time    :   2019/11/23 18:59:37
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        '''436 ms	21.4 MB'''
        for i in nums:
            index = abs(i) - 1
            nums[index] = -abs(nums[index])
        return [r + 1 for r,num in enumerate(nums) if num > 0]
if __name__ == '__main__':
    s  = Solution()
    print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))