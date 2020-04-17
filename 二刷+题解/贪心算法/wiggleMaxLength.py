#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   wiggleMaxLength.py
@Time    :   2020/04/17 10:36:15
@Author  :   Apus
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2020-2021, HB.Company
@Desc    :   None
'''

# here put the import lib
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """ n**2 """
        n = len(nums)
        if n < 2:
            return len(nums)
        up = [0] * n
        down = [0] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j]+1)
        return 1 + max(up[-1], down[-1])

    def wiggleMaxLength1(self, nums: List[int]) -> int:
        """ n """
        n = len(nums)
        if n < 2:
            return n
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                up[i] = up[i-1]
                down[i] = up[i] + 1
            elif nums[i] > nums[i-1]:
                down[i] = down[i-1]
                up[i] = down[i] + 1
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(down[-1], up[-1])

    def wiggleMaxLength1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = 1
        down = 1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                down = up + 1
            elif nums[i] > nums[i-1]:
                up = down + 1
        return max(down, up)





if __name__ == '__main__':
    pass