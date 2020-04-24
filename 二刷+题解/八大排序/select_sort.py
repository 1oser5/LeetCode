#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   select_sort.py
@Time    :   2020/04/24 14:20:48
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   选择排序
'''

# here put the import lib
def select_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)
    return nums

if __name__ == '__main__':
    select_sort([10,23,1,53,654,54,16,646,65,3155,546,31])