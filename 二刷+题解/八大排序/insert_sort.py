#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   insert_sort.py
@Time    :   2020/04/24 14:28:28
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        temp = nums[i]
        for j in range(i-1, -1, -1):
            if nums[j] > temp:
                nums[j], nums[j+1] = temp, nums[j]
            else:
                break
    print(nums)
    return nums
if __name__ == '__main__':
    insert_sort([10,23,1,53,654,54,16,646,65,3155,546,31])
