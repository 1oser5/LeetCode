#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   findMedianSortedArrays.py
@Time    :   2019/12/25 19:58:41
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = sorted(nums1 + nums2)
        n = len(nums1)        
        if n^1 == 1: # 奇数
            return nums1[(n-1)//2]
        else: # 偶数
            return (nums1[n//2] + nums1[(n-1)//2])/2



if __name__ == '__main__':
    pass