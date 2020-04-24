#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   bubble_sort.py
@Time    :   2020/04/24 14:13:15
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   冒泡排序
'''

# here put the import lib
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(1, n - i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
    print(nums)
    return nums

if __name__ == '__main__':
    c = bubble_sort([10,23,1,53,654,54,16,646,65,3155,546,31])