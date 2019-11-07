#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   majorityElement.py
@Time    :   2019/11/06 22:10:32
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# here put the import lib
def majorityElement(nums: [int]) -> int:
    '''216 ms	15.1 MB'''
    count = 0
    candidate = None
    for i in nums:
        if count == 0:
            candidate = i
        count += (1 if i == candidate else -1)
    return candidate
if __name__ == '__main__':
    print(majorityElement([3,2,3]))