#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   merge_sort.py
@Time    :   2020/04/24 14:41:23
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
def merge(nums, start, mid, end, temp):
    i, j = start, mid+1
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
    while i <= mid:
        temp.append(nums[i])
        i += 1
    while j <= end:
        temp.append(nums[j])
        j += 1

    for i in range(len(temp)):
        nums[start+i] = temp[i]
    temp.clear()


def merge_sort(nums, start, end, temp):
    if start >= end:
        return
    mid = (start + end) >> 1
    merge_sort(nums, start, mid, temp)
    merge_sort(nums, mid + 1, end, temp)
    merge(nums, start, mid, end, temp)


if __name__ == '__main__':
    pass