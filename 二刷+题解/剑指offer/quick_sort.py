#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   quick_sort.py
@Time    :   2020/04/16 14:18:40
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   快速排序
'''

# here put the import lib

def q_sort(l, left, right):
    if left < right:
        pivot = partition(l, left, right)

        q_sort(l, left, pivot-1)
        q_sort(l, pivot+1, right)
    return l


def partition(l, left, right):
    pivot = l[left]
    while left < right:
        while left < right and l[right] >= pivot:
            right -= 1
        l[left] = l[right]
        while left < right and l[left] <= pivot:
            left += 1
        l[right] = l[left]
    l[left] = pivot
    return left
if __name__ == '__main__':
    c = q_sort([5, 9, 1, 11, 6, 7, 2, 4], 0, len([5, 9, 1, 11, 6, 7, 2, 4])-1)
    print(c)