#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   sortColors.py
@Time    :   2020/05/05 20:58:03
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size < 2:
            return
        zero, two = 0, size
        i = 0
        while i < two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
                continue
            else:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1



if __name__ == '__main__':
    pass