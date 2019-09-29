#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   twoSum.py
@Time    :   2019/09/29 20:54:21
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   简单难度
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
'''

# here put the import lib
def twoSum(nums, target):
    '''自己的解法,816 ms,14.9 MB'''
    for i in range(len(nums)):
        temp = nums[i+1:]
        m = target - nums[i]
        if m in temp:
                return [i,temp.index(m)+1+i]

def twoSum(nums, target):
    '''使用hash表求解，这里使用字典模拟哈希表 92 ms	15.1 MB'''
    hashmap = {}
    for i,num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i

if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    print(twoSum(nums,target))